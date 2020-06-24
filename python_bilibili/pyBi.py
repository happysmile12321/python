#!/usr/bin/env python
import re
import requests
headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
user = 'https://space.bilibili.com/295405620/'
fans = user + 'fans/fans'
html = requests.get(fans, headers=headers, verify=False).text
print(html)
