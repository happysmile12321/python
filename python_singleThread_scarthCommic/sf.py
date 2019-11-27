import requests
import re
page_url = 'https://www.xin99r2.com/player/html.php?adv_id=start_html&video_id=110399&cs_id=0&referer=https%3A%2F%2Fwww.xin99r2.com%2Findex.php&rnd=1565009267325'
response = requests.get(page_url, verify=False)
response.encoding='utf-8'
html=response.text
imgs=re.findall(r'"thumbURL":"(.*?)"',html)
print(imgs)

for index,img_url in enumerate(imgs):

        
    response = requests.get(img_url)
    with open('%s.%s'%(index,img_url.split('.')[-1]),'wb') as f:
      f.write(response.content)
