class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
print "count: %s" % (a.get_count())
b = InstanceCounter(13)
print "count: %s" % (b.get_count())
c = InstanceCounter(17)
print "count: %s" % (c.get_count())

for obj in (a, b, c):
    print "val of obj: %s" % (obj.get_val()) # initialized value (5,13,etc.)
    print "InstanceCount: %s" % (obj.get_count()) # always 3
    print "obj.count: %s" %(obj.count)
