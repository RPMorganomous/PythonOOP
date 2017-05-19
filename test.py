from mymod import var, dothis

print var
dothis()

myint = 5
mystr = 'hello'
mylist = ['a', 'b', 'c']
mybool = True
mynone = None

def myfunc():
    print 'hello'

print type(mylist)
print type(mybool)
print type(mynone)
print type(myfunc)

this_type = type(mylist)
print type(this_type)

print type(myint)
print type(mystr)

print; print