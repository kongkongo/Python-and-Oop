class   InstanceCounter(object):
    count=0

    def     __init__(self,val):
        self.val=val
        InstanceCounter.count+=1
    
    def     set_val(self,newval):
        self.val=newval

    def     get_val(self):
        print(self.val)

    def     get_count(self):
        print(InstanceCounter.count)

a=InstanceCounter(5)
b=InstanceCounter(10)
c=InstanceCounter(15)

for     obj     in  (a,b,c):
    print("value    of      obj:%s"%obj.get_val())
    print("Count:%s"%obj.get_count())
  
  结果：
5
value    of      obj:None
3
Count:None
10
value    of      obj:None
3
Count:None
15
value    of      obj:None
3
Count:None
