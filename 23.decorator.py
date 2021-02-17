# Reference : https://www.youtube.com/watch?v=bxhuLgybIro
from    __future__ import   print_function

#2.Decorator    function
def     handle_exception(func_name):
    def     inner(*args, **kwargs):
        try:
            return  func_name(*args,**kwargs)
        except     Exception:
            print("An   exception   was     thrown:",Exception)
    return     inner

#1.Main     function    主函数
@handle_exception
def     divide(x,y):
    return    x/y

print(divide(8,0))

结果：
An   exception   was     thrown: <class 'Exception'>
None
