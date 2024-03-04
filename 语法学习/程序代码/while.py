num1 = 1

while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        result = num1*num2
        print(num2, "*", num1, "=", result,end=" ")
        num2 += 1
    print()
    num1 += 1
