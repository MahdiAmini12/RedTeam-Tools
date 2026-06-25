# Ping Scanner Pro

A multithreaded ICMP ping scanner written in Python.

## Features

* Scan multiple IP addresses
* Read targets from a file
* Multithreaded scanning using ThreadPoolExecutor
* Generate scan reports
* Save results to output files
* Validate IP addresses before scanning

## Usage

### Scan a single host

```bash
python ping_scanner.py 192.168.1.1
```

### Scan multiple hosts

```bash
python ping_scanner.py 192.168.1.1 192.168.1.2 192.168.1.3
```

### Read targets from file

```bash
python ping_scanner.py -f targets.txt
```

### Save report

```bash
python ping_scanner.py -f targets.txt -o report.txt
```

## Example Output

```text
[+] 192.168.1.1 is Alive
[-] 192.168.1.10 is Down
```

## Technologies

* Python
* subprocess
* argparse
* ipaddress
* concurrent.futures

## Disclaimer

This tool is intended for educational purposes and authorized network testing only.
