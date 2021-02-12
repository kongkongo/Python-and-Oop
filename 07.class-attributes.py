class      YourClass(object):
    classy="class value"

dd=YourClass()
print(dd.classy)

dd.classy="Instance     value"
print(dd.classy)    # This should return the string "Instance value"

#This will delete the value set for 'dd.classy' in the instance.
del     dd.classy

print(dd.classy)


结果：
class value
Instance     value
class value
