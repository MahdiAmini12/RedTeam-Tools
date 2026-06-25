from concurrent.futures import ThreadPoolExecutor
import subprocess
import ipaddress
import argparse

parser = argparse.ArgumentParser(prog="Ping Scanner Pro", description="ّّFind Alive IP Address or Alive Hosts in network")

parser.add_argument("-c", "--count", default=2, type=int, help="Number of pings")
parser.add_argument("-f", "--file", help="Input file containing IP addresses")
parser.add_argument("IP_Address", nargs="*", help="Enter IP target")
parser.add_argument("-o", "--output", help="Save results to output file")

args = parser.parse_args()

targets = []

targets.extend(args.IP_Address)

if args.file:
    try:
        with open(args.file, "r") as f:
            for line in f:
                ip = line.strip()

                if ip:
                    targets.append(ip)
    except FileNotFoundError:
        print(f"File not found: {args.file}")

if not targets:
    parser.error("No targets specified")

targets = list(dict.fromkeys(targets))

for ip in targets:
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f'{ip} is not valid')
        exit()

Alive_IP = []
Down_IP = []

def ping(target):            
    result = subprocess.run(
        ["ping", "-n", str(args.count), target],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
                print(f"[+] {target} is Alive")
                Alive_IP.append(target)
    else:
                print(f"[-] {target} is Down")
                Down_IP.append(target)
    

with ThreadPoolExecutor(max_workers=50) as exe:
    futures = []

    for target in targets:
        futures.append(exe.submit(ping, target))

    for future in futures:
         future.result()

def report():

    report_text = f"""
Ping Scanner Pro Report
====================

Total Targets: {len(targets)}
Alive Hosts: {len(Alive_IP)}
Down Hosts: {len(Down_IP)}

Alive Hosts
------------------------------
{chr(10).join(Alive_IP)}

Down Hosts
------------------------------
{chr(10).join(Down_IP)}
"""

    return report_text

if args.output:

    with open(args.output, "w") as f:
         f.write(report())

    print(f"\n[+] Results saved to {args.output}\n")

print(report())
