class Nowcoder:
    name = ''
    ID = 0
    num = 0
    def __init__(self,n,i,m):
        self.name = n
        self.ID = i
        self.num = m

    def printlnformation(self):
        print("{}'s ID is {},and his or her number of signing in is {}.".format(self.name,self.ID,self.num))

class IT(Nowcoder):
    language = ''
    def __init__(self,n,i,m,l):
        #调用父类的构函
        Nowcoder.__init__(self,n,i,m)
        self.language = l

    #覆写父类的方法
    def printlnformation(self):
        print("{}'s ID is {},and his or her number of signing in is {}.".format(self.name,self.ID,self.num))
        print(self.language)


class Designer(Nowcoder):
    color = ''
    def __init__(self,n,i,m,c):
        #调用父类的构函
        Nowcoder.__init__(self,n,i,m)
        self.color = c

    #覆写父类的方法
    def printlnformation(self):
        print("{}'s ID is {},and his or her number of signing in is {}.".format(self.name,self.ID,self.num))
        print(self.color)   

x = input().split()
coder1 = IT(x[0],int(x[1]),int(x[2]),x[3])
coder1.printlnformation()
     
y = input().split()
coder2 = Designer(x[0],int(x[1]),int(x[2]),x[3])
coder2.printlnformation()
