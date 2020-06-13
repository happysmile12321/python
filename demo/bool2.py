score = 69
if type(score)!=int:
    print("请输入整数")
    exit(0)
if (score >=0) & (score <=100):
    if (score > 90) & score <=100:
        print("优秀")
        pass
    elif (score > 80) & (score <= 90):
        print("良好")
        pass
    elif (score > 70) & score <= 80:
        print("加油")
    elif (score > 60) & score <= 10:
        print("及格")
else:
    print("输入不合法")
