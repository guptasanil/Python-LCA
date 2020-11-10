class node:
    def _init_(self, data, parent):
        self.data = data
        self.parent = parent
        if parent is None:
            self.level = 0
        else :
            self.level = self.parent.level + 1

@staticmethod
def getlca(a, b):
    if a.parent != None and b.parent != None:
         if a.parent.data == b.parent.data:
            return a.parent.data
         elif a.level < b.level:
            return getlca(a, b.parent)
         else:
            return getlca(b, a.parent)
    return 'none'
