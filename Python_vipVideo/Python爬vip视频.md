### 思路

用视频解析接口，然后下载视频解析服务器的缓存文件，

最终拼接为一个文件。

---

`视频地址`  https://www.iqiyi.com/v_19rrso72d4.html 

---

`视频解析网站`  http://vip.vipbuluo.com/

---

#### UA欺骗

```python
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}	
response=requests.get(url,headers=headers)
```

---

![1](./screenCapture/1.jpg)

![2](./screenCapture/2.jpg)

---

分析可以看出需要得到的从后面小数点后4位之前的都不变。

---

#### python中的函数

> 函数就像魔盒，你放进去什么，他会随机的吐出来什么。
>
> python这个魔盒内可以放0~多个，同样可以吐出0~多个。
>
> ```python
> def 函数名(形参列表):
>     //由零条到多条可执行语句组成的代码块
>     [return [返回值]]
> ```
>
> >  其中，用 [] 括起来的为可选择部分，即可以使用，也可以省略。
>
> >  **形参列表**：用于定义该函数可以接收的参数。形参列表由多个形参名组成，多个形参名之间以英文逗号（,）隔开。**一旦在定义函数时指定了形参列表，调用该函数时就必须传入相应的参数值**，也就是说，谁调用函数谁负责为形参赋值。
>
> *注意，在创建函数时，即使函数不需要参数，也必须保留一对空的“()”，否则 Python 解释器将提示“invaild syntax”错误。另外，如果想定义一个没有任何功能的空函数，可以使用 pass 语句作为占位符。*
>
> ---

#### python --format

```python
"{}曰：学而时习之，不亦说乎。".format("孔子")
>>> '孔子曰：学而时习之，不亦说乎。'
```

```python
"{}曰：学而时习之，不亦{}。".format("孔子","说乎")
>>> '孔子曰：学而时习之，不亦说乎。'
```

```python
"{1}曰：学而时习之，不亦{0}。".format("说乎","孔子")
>>> '孔子曰：学而时习之，不亦说乎。'
```

---

#### 视频 Cache url处理

`url='https://dapian.video-yongjiu.com/20190804/6193_fbf8b213/800k/hls/c195545768100`0001`.ts'`

没有选中的区域一直在变

>  从0001到1154

---

#### python主函数

```python
if __name__ == '__main__'：
    main（）
```

python文件引用方式

1. 作为脚本执行
2. 在其他文件中被import执行

`if __name__ == '__main__'：`下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的。

> 如果自己调用自己，那么在本文件中`__name__`属性就是`__main__`
>
> 如果其他文件import 本文件名，然后再调用本文件的某个函数，打印本文件的名，就是本文件名而不是`__main__`
>
> 简而言之就是文件内部调用`__name__`==`__main__`,反之就是False
>
> ---

#### 创建mp4文件夹

因为将来要爬取的内容很多，因此要专门准备一个文件夹

---

#### 开始向文件夹中写

首先要起合适的文件名，为了以后统一，因此要根据规律适当选择。

> 从0001到1154

`
url='https://dapian.video-yongjiu.com/20190804/6193_fbf8b213/800k/hls/c195545768100`0001`.ts`

`url='https://dapian.video-yongjiu.com/20190804/6193_fbf8b213/800k/hls/c195545768100`1154`.ts`



---

#### 格式符

```
格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:

%s    字符串 (采用str()的显示)

%r    字符串 (采用repr()的显示)

%c    单个字符

%b    二进制整数

%d    十进制整数

%i    十进制整数

%o    八进制整数

%x    十六进制整数

%e    指数 (基底写为e)

%E    指数 (基底写为E)

%f    浮点数

%F    浮点数，与上相同

%g    指数(e)或浮点数 (根据显示长度)

%G    指数(E)或浮点数 (根据显示长度)

%%    字符"%"
```

---

#### range()

内置的函数`range()`是对一系列数字进行迭代的函数。它生成一个算术进化的迭代器。

#### %03d

0n(n=1,2,3...) 宽度至少为n位，不够左边以0填充

%3d--可以指定宽度，不足的左边补空格

%表示这个位置上有一个占位符

%d表示十进制整数

url=https://dapian.video-yongjiu.com/20190804/6193_fbf8b213/800k/hls/c195545768100`1154`.ts`

新url=https://dapian.video-yongjiu.com/20190804/6193_fbf8b213/800k/hls/c195545768100%04d.ts

---

#### pool

多进程并发操作池

```python
from multiprocessing import Pool
```

```python
if __name__ == '__main__':
	#创建线程池对象
	pool = Pool (20)
	for i in range(100):
        #开启线程池
		pool.apply_async(demo,(i,))
	pool.close()
	pool.join()
```

#### 完整代码

```python
import requests
from multiprocessing import Pool
#创建py_video()函数
def py_video(i):
	#用占位符，待会用循环来表示
	url='https://dapian.video-yongjiu.com/20190804/6193_fbf8b213/800k/hls/c195545768100%04d.ts'%i
	print(url)
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}	
	response=requests.get(url,headers=headers)
	print(response)
	with open('./mp4/{}'.format(url[-7:]),'wb') as f:
		f.write(response.content)




if __name__ == '__main__':
	pool = Pool(20)
	for i in range(1154):
		#启动进程
		pool.apply_async(py_video,(i,))
	pool.close()
	pool.join()
```

#### 最后拼接

```CQL
copy /b *.ts 1.mp4
```

