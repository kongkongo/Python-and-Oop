class   Date(object):
    def     get_date(self):
        print("2016-05-14")

class   Time(Date):
    def     get_time(self):
        print("07:00:00")
#creating       an  instance    from    "Date"  
dt=Date()
dt.get_date()   #Acesing    the    "get_date()"     method  of      "Date"
print("---------")

#creating       an      instance    from    "time"
tm=Time()
tm.get_time()
tm.get_date()


结果：
2016-05-14
---------
07:00:00
2016-05-14
