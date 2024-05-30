##in python actually method overloading is not there 
##if a method is written such that  it can perform more than one task it called method overloading


class Myclass:
    def sum(self,a,b,c):
        s=a+b+c
        return s
    

obj=Myclass()
#print(obj.sum(10,20,30))

print(obj.sum(10,20))