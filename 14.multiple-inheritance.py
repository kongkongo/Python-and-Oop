class   A(object):
    def     dothis(self):
        print("doing   this   in   A")

class   B(A):
    pass

class   C(object):
    def     dothis(self):
        print("doing    this    in  C")

class   D(B,C):
    pass

d_instance=D()
d_instance.dothis()

print("\nPrint      the     Method     Resolution   Order")
print(D.mro())


结果result：
doing   this   in   A

Print      the     Method     Resolution   Order
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
