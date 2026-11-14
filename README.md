# Security Log Analyzer

## Project Overview

Security Log Analyzer is a Python-based cybersecurity tool designed to analyze SSH authentication logs, identify failed login attempts, and flag IP addresses that may require further investigation.

I developed this project to strengthen my practical understanding of cybersecurity, particularly log analysis, threat detection, and security monitoring.

## Features

- Analyzes SSH authentication log files.
- Identifies failed password authentication attempts.
- Extracts and tracks source IPv4 addresses.
- Counts failed login attempts for each IP address.
- Flags IP addresses that reach a configurable threshold.
- Displays an easy-to-read summary of findings.

## Technologies Used

- **Python 3.9+** – Core programming language
- **Regular Expressions (Regex)** – Identifying patterns within log files
- **Command-Line Interface (CLI)** – Running the analyzer
- **Python unittest** – Automated testing

## How It Works

1. The program reads a specified SSH authentication log file.
2. It searches for failed password authentication events.
3. It extracts the source IP address associated with each event.
4. It counts the number of failed attempts from each IP address.
5. It flags IP addresses that meet or exceed the configured review threshold.

## Installation and Usage

**Step 1:** Download or clone the repository.

**Step 2:** Open a terminal in the project directory.

**Step 3:** Run the analyzer using the included sample log file.

```bash
python log_analyzer.py sample_auth.log
```

To set a custom review threshold:

```bash
python log_analyzer.py sample_auth.log --threshold 2
```

To run the automated tests:

```bash
python -m unittest discover -v
```

No third-party Python packages are required.

## Example Output

```text
Failed SSH logins by source IP:
192.0.2.10: 3 [REVIEW]
198.51.100.8: 1
```

The `[REVIEW]` indicator identifies IP addresses that have reached the configured threshold. It does not automatically mean an attack has occurred.

## Cybersecurity Applications

Analyzing authentication logs is an important part of security monitoring and incident investigation.

This project demonstrates concepts commonly used by security professionals, including:

- Monitoring failed authentication attempts
- Recognizing patterns that may indicate brute-force activity
- Identifying IP addresses for additional investigation
- Understanding the value of system logs in cybersecurity

## Current Limitations

This tool currently supports common OpenSSH failed-password log entries containing IPv4 addresses. It does not monitor live systems, support every authentication log format, automatically verify malicious activity, or block suspicious connections.

## Future Improvements

- Add support for IPv6 addresses.
- Export results to CSV or JSON.
- Analyze additional authentication event types.
- Add timestamps and time-based detection.
- Develop a dashboard to visualize authentication activity.

## What I Learned

This project helped me build experience using Python to process security-related data. It also reinforced the importance of analyzing system logs, recognizing suspicious authentication patterns, and distinguishing potential security threats from confirmed incidents.

As I continue developing my IT and cybersecurity skills, I plan to expand this project with additional detection and reporting capabilities.

## Author

**Adam Jefferson**

IT and cybersecurity enthusiast transitioning into the technology field, with a CompTIA Project+ certification and ongoing CompTIA Network+ studies.
