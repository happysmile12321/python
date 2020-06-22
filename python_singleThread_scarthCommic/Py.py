import requests
import re
import sys
import os
from lxml import etree
import time
#要爬取的漫画主站url
url = "https://www.dm5.com/m823766"
headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
#处理https,获得get对象
response = requests.get(url, headers=headers)
#处理乱码
response.encoding = 'utf-8'
#获取html文本对象
html = response.text
#专门讲response赋值给html好后面操作
if response.status_code == 404:
    print(response.status_code)
    sys.exit(0)
# 获取章节，下一页的章节
title = re.findall('<title>(.*)</title>?', html)
next_title = re.findall('<a href="/(\w[0-9]+)', html)[1]
next_url = "https://www.dm5.com/" + next_title + "/"
pageroot = etree.HTML(html)
imgs = pageroot.xpath(u'//div[contains(@id,"barChapter")]/img/@data-src')
#通过遍历的形式组装数组
imgs_url = []
for i in imgs:
    imgs_url.append(i)
for index, img_url in enumerate(imgs_url[2:]):
    #    time.sleep(3)
    response = requests.get(img_url)
    with open('%s.%s' % (index, "jpg"), 'wb') as f:
        f.write(response.content)
