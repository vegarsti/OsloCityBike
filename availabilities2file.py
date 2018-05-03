#!/usr/local/bin/python3

import requests

from secret import identifier

filename = 'data.txt'
url = 'https://oslobysykkel.no/api/v1/stations/availability'
headers = {'Client-Identifier': identifier}
r = requests.get(url, headers=headers)

result = r.json()
stations = result['stations']
timestamp = result['updated_at']
date, time = timestamp[:16].split('T')
stations = sorted(stations, key=lambda x: int(x['id']))

data_list = []
for station in stations:
    id_ = station['id']
    bikes = station['availability']['bikes']
    locks = station['availability']['locks']
    data_list.append(f"{date},{time},{id_},{bikes},{locks}")

with open(filename, 'a') as file:
    file.write('\n'.join(data_list))
    file.write('\n')