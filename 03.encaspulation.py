class   MyInteger(object):
    def    set_val(self,val):
        try:
            val=int(val)
        except  ValueError:
            return 
        self.val=val
    def     get_val(self):
        print(self.val)
    def     increment_val(self):
        self.val=self.val+1
        print(self.val)

a=MyInteger()
a.set_val(10)
a.get_val()
a.increment_val()
print("\n")


# Trying to break encapsulation in a new instance with an int
c = MyInteger()
c.val = 15
c.get_val()
c.increment_val()
print("\n")


# Trying to break encapsulation in a new instance with a str
b=MyInteger()
b.val="MyString"
b.get_val()
b.increment_val()   # This will fail, since str + int wont work
print("\n")
