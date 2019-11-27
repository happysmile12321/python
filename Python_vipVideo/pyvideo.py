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
	pool = Pool(100)
	for i in range(1154):
		#启动进程
		pool.apply_async(py_video,(i,))
	pool.close()
	pool.join()