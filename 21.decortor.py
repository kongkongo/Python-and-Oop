# This is an updated version of 20-decorators-2.py.
# Here, the `decorated()` function takes an argument
# and prints it back on terminal.

# When the decorator `@my_decorator` is called, it
# takes the function `decorated()` as its argument, and
# the argument of `decorated()` as the argument of `inner_decorator()`.
# Hence the arg `number` is passed to `num_copy`.
import  datetime

def     my_decorator(inner):
    def     inner_decorator(num_copy):
        print(datetime.datetime.utcnow())
        inner(int(num_copy)+1)
        print(datetime.datetime.utcnow())

    return  inner_decorator

@my_decorator
def     decorated(number):
    print("This     happened:"+str(number))

if  __name__=="__main__":
    decorated(5)

结果result：
2021-02-16 14:17:54.119861
This     happened:6
2021-02-16 14:17:54.120038
