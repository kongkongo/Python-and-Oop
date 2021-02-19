# The @classmethod decorator marks the function/method as bound to the
# class and not to an instance.    使用classmethod这个装饰器将这个函数绑定到类上

# Remember that we used 'self' in a function within a class, which denoted
# the instance. In class methods, we use `cls` which denotes the class
# rather than the instance.

# The following example is a very simple explanation of class-methods.

# class_1() is a class method while class_2() is an instance method.

# Class methods can be accessed by the class as well as the instance.

# Instance methods can only be accessed by the Instance. That's why in this example, MyClass.class_2() will fail with an error.

# NOTE : For the class MyClass:
# 	MyClass is the class itself     MyClass是类本身
#	MyClass() is an instance          MyClass（）是一个实例
class   MyClass(object):
    @classmethod
    def    class_1(cls):
        print("Class    method  1")
    
    def     class_2(self):
        print("Self/Instance    method  1")

print("Calling      the     class   `MyClass`   directly    without    an   instance")
MyClass.class_1()
#MyClass.class_2()

#NOTE: You will want to comment `MyClass.class_2()` once you hit the `TypeError`
# to continue with the examples below.

print("\nCalling    the     instance    `MyClass()`:")
MyClass().class_1()
MyClass().class_2()

结果：
Calling      the     class   `MyClass`   directly    without    an   instance
Class    method  1

Calling    the     instance    `MyClass()`:
Class    method  1
Self/Instance    method  1
