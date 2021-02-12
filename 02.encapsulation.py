class   Myclass(object):
    def     set_val(self,val):
        self.value=val
    
    def     get_val(self):
        print(self.value)
        # return  self.value

a=Myclass()
b=Myclass()

a.set_val(66)
b.set_val(666)
a.value=100

a.get_val()
b.get_val()




result:
zhang@ubuntu:~/桌面/Python-and--oop$ /usr/bin/python3 /home/zhang/桌面/Python-and--oop/02.encapsulation.py
100
666
