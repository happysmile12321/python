#!/usr/bin/env python
import requests
import json
r_json = requests.get('https://myip.ipip.net/json').text
weather_dict = json.loads(r_json)
location = weather_dict.get('data').get('location')


#    print('我的国家是:[' + country + ']')
#    print('我的省份是:[' + province + ']')
#    print('我的城市是:[' + city + ']')
#    print('我的运营商是:[' + isp + ']')
def toString(location):
    country = location[0]
    province = location[1]
    city = location[2]
    isp = location[4]
    return city
