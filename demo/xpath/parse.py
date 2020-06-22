#!/usr/bin/env python
from lxml import etree
# 1. starts-with函数
# 获取以xxx开头的元素
# 例子：xpath(‘//div[stars-with(@class,”test”)]’)
#
# 2 contains函数
# 获取包含xxx的元素
# 例子：xpath(‘//div[contains(@id,”test”)]’)
#
# 3 and
# 与的关系
# 例子：xpath(‘//div[contains(@id,”test”) and contains(@id,”title”)]’)
#
# 4 text()函数
# 例子1：xpath(‘//div[contains(text(),”test”)]’)
# 例子2：xpath(‘//div[@id=”“test]/text()’)
html = '''

<html>
　　<head>
　　　　<meta name="content-type" content="text/html; charset=utf-8" />
　　　　<title>友情链接查询 - 站长工具</title>
　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
　　　　<meta name="Keywords" content="友情链接查询" />
　　　　<meta name="Description" content="友情链接查询" />

　　</head>
　　<body>
　　　　<h1 class="heading">Top News</h1>
　　　　<p style="font-size: 200%">World News only on this page</p>
　　　　Ah, and here's some more text, by the way.
　　　　<p>... and this is a parsed fragment ...</p>

　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a> 
　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a> 
　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a> 
　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a> 
　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a>

　　</body>
</html>

'''
# xml.xpath(“bookstore”)表示选取 bookstore 元素的所有子节点
# xml.xpath(“/bookstore”) 表示选取根元素 bookstore。
# xml.xpath(“bookstore/book”) 选取属于 bookstore 的子元素的所有 book 元素。
# xml.xpath(“//book”) 选取所有 book 子元素，而不管它们在文档中的位置。
# xml.xpath(“bookstore//book”) 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
# xml.xpath(“//@lang”) 选取名为 lang 的所有属性。

page = etree.HTML(html)
hrefs = page.xpath(u"//a")
for href in hrefs:
    print(href.attrib)
