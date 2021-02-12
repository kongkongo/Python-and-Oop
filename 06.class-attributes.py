class   YourClass(object):
    classy=10

    def     set_val(self):
        self.insty=100

dd=YourClass()
dd.classy   # This will fetch the class attribute 10.
dd.set_val()
print(dd.insty)         # This will fetch the instance attribute 100.

result:
100
