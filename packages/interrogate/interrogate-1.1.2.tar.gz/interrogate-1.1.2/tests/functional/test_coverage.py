# Copyright 2020 Lynn Root
"""Functional tests for interrogate/coverage.py."""

import os

import pytest

from interrogate import coverage


HERE = os.path.abspath(os.path.join(os.path.abspath(__file__), os.path.pardir))
SAMPLE_DIR = os.path.join(HERE, "sample")
FIXTURES = os.path.join(HERE, "fixtures")


@pytest.mark.parametrize(
    "paths,exp_results",
    (
        ([os.path.join(SAMPLE_DIR, "empty.py"),], (1, 0, 1, 0, "0.0")),
        ([SAMPLE_DIR,], (52, 24, 28, 0, "46.2")),
        ([os.path.join(SAMPLE_DIR, "partial.py")], (20, 7, 13, 0, "35.0")),
    ),
)
def test_coverage_simple(paths, exp_results):
    """Happy path - get expected results given a file or directory"""
    interrogate_coverage = coverage.InterrogateCoverage(paths=paths)

    results = interrogate_coverage.get_coverage()

    assert exp_results[0] == results.total
    assert exp_results[1] == results.covered
    assert exp_results[2] == results.missing
    assert exp_results[3] == results.skipped
    assert exp_results[4] == "{:.1f}".format(results.perc_covered)


def test_coverage_errors(capsys):
    """Exit when no Python files are found."""
    path = os.path.join(SAMPLE_DIR, "ignoreme.txt")
    interrogate_coverage = coverage.InterrogateCoverage(paths=[path])

    with pytest.raises(SystemExit, match="1"):
        interrogate_coverage.get_coverage()

    captured = capsys.readouterr()
    assert "E: Invalid file" in captured.err

    interrogate_coverage = coverage.InterrogateCoverage(paths=[FIXTURES])

    with pytest.raises(SystemExit, match="1"):
        interrogate_coverage.get_coverage()

    captured = capsys.readouterr()
    assert "E: No Python files found to interrogate in " in captured.err


@pytest.mark.parametrize(
    "level,exp_fixture_file",
    (
        (0, "expected_no_verbosity.txt"),
        (1, "expected_summary.txt"),
        (2, "expected_detailed.txt"),
    ),
)
def test_print_results(level, exp_fixture_file, capsys, monkeypatch):
    """Output of test results differ by verbosity."""
    monkeypatch.setattr(coverage.utils, "TERMINAL_WIDTH", 80)

    interrogate_coverage = coverage.InterrogateCoverage(paths=[SAMPLE_DIR])
    results = interrogate_coverage.get_coverage()
    interrogate_coverage.print_results(results, None, level)

    captured = capsys.readouterr()
    expected_fixture = os.path.join(FIXTURES, exp_fixture_file)
    with open(expected_fixture, "r") as f:
        expected_out = f.read()
    assert expected_out in captured.out
