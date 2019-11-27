# import requests 
# import re
# #设置url
# url='http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%99%BE%E9%87%8C%E5%AE%88%E7%BA%A6'
# #url = "https://mhpic.dongzaojiage.com/images/comic/280/559081/1562872247tkSWVuxQ5675SvHa."
# #处理https,获得get对象
# response = requests.get(url,verify=False)
# #处理乱码
# response.encoding='utf-8'
# #专门讲response赋值给html好后面操作
# html=response.text
# #开始写正则表达式过滤规则
# imgs=re.findall(r'"thumbURL":"(.*?)"',html)
# #用for循环保存到本地
# for index,img_url in enumerate(imgs):
#     response = requests.get(img_url)
#     with open('%s.%s'%(index,img_url.split('.')[-1]),'wb') as f:
#       f.write(response.content)


###### modified
import requests 
import re
#设置url
url = "https://www.mh1234.com//comic//9329//559080.html"
#处理https,获得get对象
response = requests.get(url,verify=False)
#处理乱码
response.encoding='utf-8'
#专门讲response赋值给html好后面操作
html=response.text
#开始写正则表达式过滤规则


#'https://mhpic.dongzaojiage.com/'+



#这个是chapterPath
chapterPath=re.findall(r'var chapterPath = "(.*)";var pageTitle',html)[0]

#这个text是chapterImages
chapterImages = re.findall(r'([1][5][6][2][8][7].*[.])["]+',html).pop(0).split('","')


#for index,img in enumerate(chapterImages):
#	with open('%s.%s'%(index,"txt"),'wb') as f:
#		f.write(bytes(img.encode('utf-8')))
# 现在，所有的bytes(img.encode('utf-8'))就都是合理的结果了
arraylist = list();
#通过遍历的形式组装数组
for index,img in enumerate(chapterImages):
	arraylist.append('https://mhpic.dongzaojiage.com/'+chapterPath+img)

for index,img_url in enumerate(arraylist):
 	response=requests.get(img_url)	
 	with open('%s.%s'%(index,"jpg"),'wb') as f:
	  f.write(response.content)

print('-------------------------------------------------------')
print(arraylist)