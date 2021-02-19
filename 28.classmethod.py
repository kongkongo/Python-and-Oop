# Reference: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

# Classmethods are decorators which are inbuilt in Python.
# We decorate a function as a classemethod using the decorator
# @classmethod.

# Class methods are used for functions which need not be
# called via an instance. Certain use cases may be:

# a) Creating instances take resources, hence the methods/functions
# which need necessarily

class   MyClass(object):
    count=0
    def     __init__(self,val):
        self.val=val
        MyClass.count+=1
    
    def     set_val(self,newval):
        self.val=newval
    
    def     get_val(self):
        return  self.val
    @classmethod
    def     get_count(cls):
        return   cls.count

object_1=MyClass(10)
print("\nValue   of     object:%s"%object_1.get_val())
print(MyClass.get_count())

结果：
Value   of     object:10
1
