# Instance methods are also known as Bound methods since the methods
# within a class are bound to the instance created from the class, via
# 'self'.

class  A(object):
    def    method(*argv):
        return  argv
    
    a=A()
    print(a.method)


结果result:
Traceback (most recent call last):
  File "/home/zhang/桌面/Python-and--oop/17.instance-methods.py", line 1, in <module>
    class  A(object):
  File "/home/zhang/桌面/Python-and--oop/17.instance-methods.py", line 5, in A
    a=A()
NameError: name 'A' is not defined
