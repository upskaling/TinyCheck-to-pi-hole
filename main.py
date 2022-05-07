#!/usr/bin/env python3

import json
import os
import requests

url_source = 'https://raw.githubusercontent.com/felixaime/TinyCheck-1/main/assets/iocs.json'
ficher_source = 'iocs.json'
ficher_target = 'iocs'


def download_file(url, filename):
    file = requests.get(url, allow_redirects=True)
    with open(filename, 'wb') as f:
        f.write(file.content)


download_file(url_source, ficher_source)

with open(ficher_source) as f:
    data_source = json.load(f)

i = 0
with open('iocs', 'w') as f:
    for iocs in data_source['iocs']:
        
        if iocs['type'] != 'domain':
            continue

        f.write('0.0.0.0 ' + iocs['value'] + '\n')

        i += 1

print(f'There are {i} areas')
