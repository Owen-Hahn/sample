#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='Parse web logs and return various statistics, expected format is <url path><ip address>\nusage: SP_answer.py [--sort-order N] file [file ...]  ')

parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F',
                    type=str,nargs='+',
                    help='List of files to process')

parser.add_argument('--sort-order',
                    choices=['Ascending','Descending'],
                    default='Ascending',
                    help='Order to sort output')

parser.add_argument('--verbose',
                    default=False,
                    action='store_true',
                    help='Display process information')

args =parser.parse_args()
stats = {}

if args.sort_order == 'Ascending':
    reverse = False
else:
    reverse = True

for filename in args.files:
    count = 0
    if (args.verbose):
        print('Parsing file {}'.format(filename))
    with open(filename) as weblog:
        for line in weblog:
            count += 1

            data = line.split()
            assert len(data) == 2, 'Expected format is <url path><ip address>'
            (url_path,ip_address) = data

            record = stats.setdefault(url_path,{'count':0,'users':set()})
            record['count'] += 1
            record['users'].add(ip_address)
        if(args.verbose):
            print('Finished file {} processed {} entries'.format(filename,count))

for url_path,count in sorted(stats.items(), 
                             key=lambda rec: rec[1]['count'], 
                             reverse=reverse):
    print('{} {} visits'.format(url_path,count['count']))

for url_path,count in sorted(stats.items(),
                             key=lambda rec: len(rec[1]['users']),
                             reverse=reverse):
    print('{} {} unique views'.format(url_path,len(count['users'])))

