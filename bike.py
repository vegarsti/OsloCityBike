#!/usr/local/bin/python3

import requests

from secret import identifier

url = 'https://oslobysykkel.no/api/v1/stations/availability'
headers = {'Client-Identifier': identifier}
r = requests.get(url, headers=headers)
r.status_code # should be 200

result = r.json()
stations = result['stations'] # list
station = stations[0]

for key, value in station.items():
	print(key, value)