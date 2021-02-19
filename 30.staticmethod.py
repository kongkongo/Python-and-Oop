# Refer
# https://arvimal.wordpress.com/2016/06/12/instance-class-static-methods-object-oriented-programming/

# Static methods are functions/methods which doesn’t need a binding to a class or an instance.
# Static methods, as well as Class methods, don’t require an instance to be called.
# Static methods doesn’t need  self or cls as the first argument since it’s not bound to an instance or class.
# Static methods are normal functions, but within a class.
# Static methods are defined with the keyword @staticmethod above the function/method.
# Static methods are usually used to work on Class Attributes.
from    __future__  import  print_function

class   MyClass(object):
    count=0

    def     __init__(self,name):
        print("An   instance    is  created!")
        self.name=name
        MyClass.count+=1

        #Our    class   method
    @staticmethod
    def    status():
        print("The  total   number  of  instances   are ",MyClass.count)
    
print(MyClass.count)

my_func_1=MyClass("MyClass1")
my_func_2=MyClass("MyClass2")
my_func_3=MyClass("MyClass3")

MyClass.status()
print(MyClass.count)

结果：
0
An   instance    is  created!
An   instance    is  created!
An   instance    is  created!
The  total   number  of  instances   are  3
3

