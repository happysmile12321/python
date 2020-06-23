from multiprocessing import Pool
def demo(i):
	s='sfddsf%04d'%i
	print(s)




if __name__ == '__main__':
	#创建线程池对象
	pool = Pool (20)
	for i in range(100):
		pool.apply_async(demo,(i,))
	pool.close()
	pool.join()



