day = 1
week = 0
while day <= 7:
    answer = input("今天有好好爱憨宝子吗？")
    if answer != "有":
        print("憨宝子要生气了！！！")
        break
    print("今天也是好爱憨宝子的一天！！！！")
    day += 1
else:
    week += 1
    print("爱宝子进度+1")
