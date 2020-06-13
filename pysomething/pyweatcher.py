import re
import requests
html = requests.get('https://www.ip138.com/').text
print(html)
