import re
from collections import Counter

def analyze_log(filename):
    failed_logins = []
    suspicious_ips = []
    ip_counts = Counter()

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    for line in lines:
        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        if ip_match:
            ip = ip_match.group()
            ip_counts[ip] += 1

        if 'Failed password' in line or 'FAILED LOGIN' in line:
            failed_logins.append(line.strip())

    for ip, count in ip_counts.items():
        if count > 10:
            suspicious_ips.append((ip, count))

    print("=" * 50)
    print("LOG ANALYSIS REPORT")
    print("=" * 50)
    print(f"\nTotal lines analyzed: {len(lines)}")
    print(f"Failed login attempts: {len(failed_logins)}")

    if failed_logins:
        print("\n[!] Failed Login Events:")
        for event in failed_logins[:5]:
            print(f"  {event}")

    if suspicious_ips:
        print("\n[!] Suspicious IPs (more than 10 requests):")
        for ip, count in suspicious_ips:
            print(f"  {ip} - {count} requests")
    else:
        print("\n[*] No suspicious IPs detected.")

    print("\n[*] Top 5 Most Active IPs:")
    for ip, count in ip_counts.most_common(5):
        print(f"  {ip} - {count} requests")

analyze_log('sample.log')
