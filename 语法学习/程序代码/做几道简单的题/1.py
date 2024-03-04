num = int(input("请输入分数的个数："))
while num > 0:
    score = int(input("请输入0~100之间的分数："))
    if score >= 90 and score <= 100:
        print("A")
    elif score > 75 and score < 90:
        print("B")
    elif score >= 60 and score <= 75:
        print("C")
    elif score < 60 and score >= 0:
        print("F")
    else:
        print("请输入0~100之间的数字")
        num += 1

    num -= 1
    
