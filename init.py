class MyNum(object):
    def __init__(self, value):
        print 'calling __init__'
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1

aa = MyNum('hello') # calling __init__
bb = MyNum(100)

aa.increment()
aa.increment()
bb.increment()

print aa.val
print bb.val

dd = MyNum(5)    # calling __init__
dd.increment()
dd.increment()

print dd.val    # 7
