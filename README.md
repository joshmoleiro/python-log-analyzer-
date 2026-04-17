# Python Log Analyzer 

## Overview
In this project I built a Python script that automates the analysis of SSH authentication logs. The script then parses the log files to detect the failed login attempts, suspicious IPs that are showing brute force behavior, and then creates a structured report which is replicating a fundamental task that is done by SOC analysts during incident investigation. 

## Tools Used 
- Python 3
- Log analysis scripts

## Objectives 
- automate the detection of failed login attempts from the raw log files
- Identify the suspicious IPs that exceed a defined request threshold
- Generate a structured analysis report from unstructured log data 
## Skills Demonstrated 
- Python scripting/automation
- Log parsing/pattern matching using regex
- Using threat detection logic to identify suspected brute force actions
- Security automation concepts 

## How it Works
The script reads a log file line by line, extracts the IP addresses using regex, counts each request per the IPs, flags any IP that is exceeding 10 requests as suspicious, and identifies the failed login events. After that it outputs a structured report showing total lines analyzed, failed login attempts, suspicious IPs and then the top 5 most active IPs. 

## Sample Output 
```
==================================================
LOG ANALYSIS REPORT
==================================================
Total lines analyzed: 23
Failed login attempts: 17

[!] Suspicious IPs (more than 10 requests):
  203.0.113.42 - 11 requests

[*] Top 5 Most Active IPs:
  203.0.113.42 - 11 requests
  192.168.1.105 - 3 requests
  10.0.0.5 - 3 requests
  198.51.100.7 - 2 requests
  45.33.32.156 - 1 requests
```
