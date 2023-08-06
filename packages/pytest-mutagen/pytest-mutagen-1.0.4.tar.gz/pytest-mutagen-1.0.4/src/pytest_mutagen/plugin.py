from pytest_mutagen.mutagen import *
from _pytest.reports import TestReport
from _pytest.runner import runtestprotocol
from _pytest.config import ExitCode
from _pytest.terminal import TerminalReporter
import sys

import pytest

MUTAGEN_OPTION = "--mutate"
QUICK_MUTATIONS = "--quick-mut"

all_test_passed = True
failed_mutants = {}

def pytest_addoption(parser):
    group = parser.getgroup("mutagen", "Mutagen")
    group.addoption(
        MUTAGEN_OPTION,
        action="store_true",
        help="activate the mutation testing tool",
    )
    group.addoption(
        QUICK_MUTATIONS,
        action="store_true",
        help="each mutant stops after the first failed test"
    )

def pytest_report_header(config):
    return 'pytest-mutagen-1.0 : Mutations ' + ('enabled' if config.getoption(MUTAGEN_OPTION) else 'disabled')

def pytest_report_teststatus(report, config):
    global all_test_passed
    if report.when == "call":
        if report.outcome == "mutpassed":
            return "mut_passed", "m", ("MUT", {"purple": True})
        elif report.outcome == "mutfailed":
            all_test_passed = False
            return "mut_failed", "M", ("MUTF", {"red": True})


def pytest_runtest_makereport(item, call):
    report = TestReport.from_item_and_call(item, call)
    if g_current_mutant and report.when == "call":
        report.outcome = "mut" + report.outcome
    return report

def check_cache_and_rearrange(module_name, session, mutant_name, collection):
    cached_failures = session.config.cache.get("mutagen/" + module_name + "/" + mutant_name, None)
    expected_failures = []
    expected_successes = []
    if not cached_failures is None:
        for item in collection:
            if get_func_from_item(item).__qualname__ in cached_failures:
                expected_failures.append(item)
            else:
                expected_successes.append(item)
        session.config.cache.set("mutagen/" + module_name + "/" + mutant_name, [])
        return expected_failures + expected_successes
    return collection

def write_in_cache(module_name, session, item, mutant_name):
    l = session.config.cache.get("mutagen/" + module_name + "/" + mutant_name, None)
    new_val = get_func_from_item(item).__qualname__
    session.config.cache.set("mutagen/" + module_name + "/" + mutant_name, ([] if l is None else l) + [new_val])


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    global g_mutant_registry
    global g_current_mutant
    global all_test_passed
    global failed_mutants

    if not session.config.getoption(MUTAGEN_OPTION):
        return

    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    reporter._tw.line()
    reporter.write_sep("=", "mutation session starts", bold=True)
    reporter.showfspath = False

    for module in session.collect():
        basename = path.basename(module.name)
        collection = module.collect()

        if not isinstance(collection, list):
            continue

        failed_mutants[basename] = []
        reporter._tw.line()
        reporter.write_line("Module " + basename + ":")

        for mutant in filter(lambda x: x.file == basename, g_mutant_registry[basename].values()):
            g_current_mutant = mutant
            all_test_passed = True

            collection = check_cache_and_rearrange(basename, session, mutant.name, collection)

            def f():
                skip = False
                for item in collection:
                    if not skip:
                        saved_globals = modify_environment(item, mutant)
                        reports = runtestprotocol(item)
                        if any(report.outcome == "mutfailed" for report in reports):
                            write_in_cache(basename, session, item, mutant.name)
                            if session.config.getoption(QUICK_MUTATIONS):
                                skip = True
                        restore_environment(item, mutant, saved_globals)
                    else:
                        reporter.write(" ")

            mutant.apply_and_run(f)
            g_current_mutant = None

            if all_test_passed:
                reporter.write_line("\t" + mutant.name + "\t/!\ ALL TESTS PASSED")
                failed_mutants[basename].append(mutant.name)
                session.exitstatus = ExitCode.TESTS_FAILED
            else:
                reporter.write_line("\t" + mutant.name)

def pytest_terminal_summary(terminalreporter):
    terminalreporter.section("Mutagen")

    for module in failed_mutants:
        if failed_mutants[module] != []:
            terminalreporter.write("[ERROR]   ", **{"red": True})
            terminalreporter.write_line(module + ": The following mutants passed all tests: " + str(failed_mutants[module]))
        else:
            terminalreporter.write("[SUCCESS] ", **{"green": True})
            terminalreporter.write_line(module + ": All mutants made at least one test fail")

def get_func_from_item(item):
    if hasattr(item.function, "is_hypothesis_test") and getattr(item.function, "is_hypothesis_test"):
        return getattr(item.function, "hypothesis").inner_test
    return item.function

def get_object_to_modify(func_name, f, repl):
    obj_to_modify = None
    if func_name in f.__globals__:
        obj_to_modify = f.__globals__[func_name]
    elif func_name in repl.__globals__:
        obj_to_modify = repl.__globals__[func_name]
    return obj_to_modify

def modify_environment(item, mutant):
    saved = {}

    for func_name, repl in mutant.function_mappings.items():
        f = get_func_from_item(item)

        if not "." in func_name:
            func_to_modify = get_object_to_modify(func_name, f, repl)

            if not func_to_modify is None:
                saved[func_name] = func_to_modify.__globals__[func_name].__code__
                func_to_modify.__globals__[func_name].__code__ = repl.__code__
        else:
            l = func_name.split(".", 1)
            class_to_modify = get_object_to_modify(l[0], f, repl)

            if not class_to_modify is None:
                saved[func_name] = class_to_modify.__dict__[l[1]]

                if isinstance(saved[func_name], staticmethod):
                    setattr(class_to_modify, l[1], staticmethod(repl))
                elif isinstance(saved[func_name], property):
                    new_prop = property(fget=repl, fset=saved[func_name].fset, fdel=saved[func_name].fdel)
                    setattr(class_to_modify, l[1], new_prop)
                else:
                    setattr(class_to_modify, l[1], repl)

    return saved

def restore_environment(item, mutant, saved):
    if hasattr(item.function, "is_hypothesis_test") and getattr(item.function, "is_hypothesis_test"):
        f = getattr(item.function, "hypothesis").inner_test
    else:
        f = item.function

    for func_name in saved:
        if not "." in func_name:
            if func_name in f.__globals__:
                f.__globals__[func_name].__code__ = saved[func_name]
            else:
                mutant.function_mappings[func_name].__globals__[func_name].__code__ = saved[func_name]
        else:
            l = func_name.split(".", 1)
            if l[0] in f.__globals__:
                setattr(f.__globals__[l[0]], l[1], saved[func_name])
            else:
                setattr(mutant.function_mappings[func_name].__globals__[l[0]], l[1], saved[func_name])