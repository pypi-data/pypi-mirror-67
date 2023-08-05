from __future__ import print_function
from random import shuffle

import boto3
import netifaces
import os
import requests
import sys
import time

if len(sys.argv) < 2:
    print('No DNS address given.', file=sys.stderr)
    exit(1)

ip = None
dns = sys.argv[1]
public = os.environ.get('PUBLIC_IP', False)

if public:

    public_ip_urls = [
        'http://icanhazip.com',
        'http://myip.dnsomatic.com/',
        'http://ipinfo.io/ip'
    ]
    shuffle(public_ip_urls)

    for url in public_ip_urls:
        try:
            ip = requests.get(url).text.rstrip()
            break
        except Exception:
            continue

else:

    prefix_list = os.environ.get("INTERFACE_PREFIX", "en,eth,wl")
    prefixes = prefix_list.split(',')

    interface = os.environ.get("INTERFACE_NAME", None)

    if not interface:
        interfaces = []

        for prefix in prefixes:
            for i in netifaces.interfaces():
                if i.startswith(prefix):
                    interfaces.append(i)
                    break

        for interface in interfaces:
            try:
                inet = netifaces.ifaddresses(interface)[netifaces.AF_INET]
                ip = inet[0]['addr']
                break
            except KeyError:
                continue
        else:
            print('No interface found.', file=sys.stderr)
            exit(1)


skip_check = os.environ.get('SKIP_CHECK', False)
if not skip_check:

    from dns.resolver import Resolver, NXDOMAIN, Timeout
    resolver = Resolver()
    nameservers = os.environ.get('NAMESERVERS', '8.8.8.8,8.8.4.4')
    resolver.nameservers = nameservers.split(',')

    for _ in range(3):
        try:
            answers = resolver.query(dns)
            for rdata in answers:
                if rdata.address == ip:
                    exit(0)  # No need to update
        except NXDOMAIN:
            break
        except Timeout:
            time.sleep(1)


client = boto3.client('route53')

zone_name = ''
zone_id = None
hosted_zones = client.list_hosted_zones_by_name()['HostedZones']

for zone in hosted_zones:
    name = zone['Name'][:-1]
    if dns.endswith(name) and len(name) > len(zone_name):
        zone_name = name
        zone_id = zone['Id'].split('/')[-1]

if not zone_id:
    print('No zone found.', file=sys.stderr)
    exit(1)


def main():
    try:
        client.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                'Comment': '%s -> %s' % (dns, ip),
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': dns,
                            'Type': 'A',
                            'TTL': 30,
                            'ResourceRecords': [
                                {
                                    'Value': ip
                                }
                            ]
                        }
                    }
                ]
            }
        )
    except Exception:
        print('DNS record update failed.', file=sys.stderr)
        exit(1)

    print('Updated %s -> %s.' % (dns, ip))
    exit(0)
