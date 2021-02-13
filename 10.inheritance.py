class   Animal(object):
    def     __init__(self,name):
        self.name=name

    def     eat(self,food):
        print("%s   is      eating     %s"%(self.name,food))

class   Dog(Animal):
    def     fetch(self,thing):
        print("%s   goes    after   the %s" %(self.name,thing))

class   Cat(Animal):
    def     swatstring(self):
        print("%s   shred   the     string!"%self.name)

d=Dog("Roger")
c=Cat("Fluffy")

d.fetch("paper")
d.eat("dog  food")
print("-------")
c.eat("cat  food")
c.swatstring()

# The below methods would fail, since the instances doesn't have
# have access to the other class.
c.fetch("frizbee")
d.swatstring()


结果：
Roger   goes    after   the paper
Roger   is      eating     dog  food
-------
Fluffy   is      eating     cat  food
Fluffy   shred   the     string!
Traceback (most recent call last):
  File "/home/zhang/桌面/Python-and--oop/10.inheritance.py", line 27, in <module>
    c.fetch("frizbee")
AttributeError: 'Cat' object has no attribute 'fetch'
