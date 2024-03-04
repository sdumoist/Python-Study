
import random
counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("猜数字:")
    guess = int(temp)

    if guess == answer:
        print("你是我肚子里的蛔虫吗？！")
        print("哼，就算猜中了也没有奖励")
        break
    else:
        if guess<8:
            print("小啦" )
        else:
            print("大啦")
        counts = counts - 1

print("游戏结束！！")


