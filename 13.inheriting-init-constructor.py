class   Animal(object):
    def     __init__(self,name):
        self.name=name
    
class   Dog(Animal):
    def     fetch(self,thing):
        print('%s   goes    after   the     %s'%(self.name,thing))

d=Dog("Roger")
print("The  dog's   name    is",d.name)
d.fetch("frizbee")

结果result:
The  dog's   name    is Roger
Roger   goes    after   the     frizbee
