class MaxSizeList(object):

    def __init__(self, val):
        self.the_list = []
        self.val = val

    def push(self, item):
        self.the_list.append(item)
        if len(self.the_list)>self.val:
            self.the_list.pop(0)

    def get_list(self):
        return self.the_list