import  datetime


def     my_decortor(inner):
    def     inner_decorator():
        print(datetime.datetime.utcnow())
        inner()
        print(datetime.datetime.utcnow())
    return  inner_decorator()

@my_decortor
def     decorated():
    print("This     happened!")

if     __name__=="__main__":
    decorated                 #!!!不能加括号，不然报错
    
    结果result：
    2021-02-16 14:07:44.981073
This     happened!
2021-02-16 14:07:44.981361
