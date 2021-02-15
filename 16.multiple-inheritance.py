# In the example below, class `D` inherits from `B` and `C`.
# And both `B` and `C` inherits from `A`.
# Both `A` and `C` has the method `dothis()`.

# We instantiate `D` and requests the 'dothis()' method.
# By default, the lookup should go D -> B -> A -> C -> A.
# But from Python 2.3, in order to reduce the lookup time,
# the MRO skips the classes which occur multiple times in the path.

# Hence the lookup will be D -> B -> C -> A.

class   A(object):
    def     dothis(self):
        print("doing    this    in      A")

class   B(A):
    pass

class   C(A):
    def     dothis(self):
        print("doing    this    in  C")

class   D(B,C):
    pass

d_instance=D()
d_instance.dothis()

print("\nPrint    the   Method     Resolution   Order")
print(D.mro())



结果result:
doing    this    in  C

Print    the   Method     Resolution   Order
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
