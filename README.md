# DNS Zone File Migrator

## Overview

`migrate_dns.py` is a Python script designed to migrate DNS records from a Wix JSON formatted zone file into an RFC-compliant DNS zone file format. This script is particularly useful for system administrators and network engineers looking to automate the management of DNS records.

## Author

Robert Misior

## Date

2024-05-08

## Description

This script reads a JSON file containing DNS records as exported from a Wix DNS configuration and converts it into a standard DNS zone file format. The output is formatted according to RFC standards for DNS zone files, which can be used directly in DNS server configurations.

## Features

- Read DNS configuration from a JSON file.
- Convert JSON formatted DNS records into an RFC-compliant zone file.
- Print the formatted DNS zone file, ready for redirection to a file.

## Usage

To use `migrate_dns.py`, follow these steps:

1. Ensure you have Python installed on your system.
2. Place the JSON file containing the Wix DNS zone data in the same directory as the script or specify the path.
3. Modify the `file_path` variable in the script if necessary to point to the location of your JSON file.
4. Run the script using the following command:

```bash
python migrate_dns.py > your_output_zone_file.zone
