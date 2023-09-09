# custom_reports.py

import pytest


# Define a custom pytest hook to generate custom reports
def pytest_terminal_summary(terminalreporter):
    # Access test outcomes and markers here
    critical_tests = terminalreporter.stats.get("critical", [])
    high_priority_tests = terminalreporter.stats.get("high", [])
    # Generate custom report based on the data
    generate_custom_report(critical_tests, high_priority_tests)


# Define a function to generate custom reports
def generate_custom_report(critical_tests, high_priority_tests):
    # Implement your custom reporting logic here
    # You can generate HTML, JSON, or any other format of report
    # Example: write to a custom report file
    with open("custom_report.txt", "w") as report_file:
        report_file.write("Custom Report\n")
        report_file.write(f"Critical Tests: {len(critical_tests)}\n")
        report_file.write(f"High Priority Tests: {len(high_priority_tests)}\n")
        # Include more details as needed
