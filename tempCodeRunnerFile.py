class checkin:
    
    def __init__(self,num):
        self.num=num
    def __eq__(self,other):
        return self.num==other.num
    
n=checkin(1)
m=checkin(2)

print(n==m)