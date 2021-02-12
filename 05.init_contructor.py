class   MyNum(object):
    def     __init__(self,value):
        try:
            value=int(value)
        except      ValueError:
            value=0
        self.value=value

    def     incremement(self):
        self.value=self.value+1
        print(self.value)

a=MyNum(10)
a.incremement()
a.incremement()


result:
11
12
