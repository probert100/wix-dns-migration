# File: migrate_dns.py
# Author: Robert Misior
# Date: 2024-05-08
# Description:
# This script migrates Wix DNS JSON Zone file into   RFC complaint DNS zone
#
# Usage:
# Set the value of  file_path  and run this script from the command line. Pipe output to a new zone file name

import json


def read_wix_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def convert_to_dns_zone(json_data):
    dns_zone = json_data['dnsZone']
    domain_name = dns_zone['domainName']
    records = dns_zone['records']

    # Begin constructing the zone file content
    zone_file_content = f"; Zone file for {domain_name}\n"
    zone_file_content += "$TTL 3600\n"  # Default TTL for all records

    # Loop through records to format them correctly
    for record in records:
        for value in record['values']:
            if record['type'] == "MX":
                priority, mx_record = value.split(maxsplit=1)
                zone_file_content += f"{record['hostName']} {record['ttl']} IN MX {priority} {mx_record}\n"
            else:
                zone_file_content += f"{record['hostName']} {record['ttl']} IN {record['type']} {value}\n"

    # Print out the zone file content
    print(zone_file_content)


def main():
    file_path = "./wix_dns_export.json"
    json_data = read_wix_json(file_path)
    convert_to_dns_zone(json_data)


if __name__ == "__main__":
    main()
