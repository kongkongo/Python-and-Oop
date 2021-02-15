class   A(object):
    def     dothat(self):
        print("Doing    this    in      A")

class   B(A):
    pass

class   C(object):
    def     dothis(self):
        print("\nDoing     this     in  C")

class   D(B,C):
    """Multiple     inheritance,
    D   inheriting      from    both    B   and     C"""
    pass
d_instance=D()

d_instance.dothis()

print("\nPrint      the     Method      Resolution      Order")
print(D.mro())

结果result:
Doing     this     in  C

Print      the     Method      Resolution      Order
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
