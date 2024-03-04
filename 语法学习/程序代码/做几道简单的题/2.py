num = input()
list1 = map(int,num.split())
x = input() 
list2 = map(float,x.split())
d = dict(zip(list1,list2))
number = input()
num_list = map(float,number.split())
v = d[num_list[0]] * d[num_list[1]] * d[num_list[2]]
print(v)
