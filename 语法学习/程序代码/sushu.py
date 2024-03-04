total = 0
for each in range(2,10000):
    num = 2
    flag = 1

    while num <= each/2:
        if(each % num == 0):
            flag = 0
            break
        num += 1  
    if(flag == 1):
        total += 1

print(total)
    
    
