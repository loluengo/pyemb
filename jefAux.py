class Hoop:
    SIZE_110x110 = 0
    SIZE_50x50 = 1
    SIZE_140x200 = 2
    SIZE_126x110 = 3
    SIZE_200x200 = 4
    width = None
    height = None
    
class Bounds:
    def __init__(self,left,top,right,bottom):
        self._left = left
        self._right = right
        self._top = top
        self._bottom = bottom
    def setLeft(self,left):
        self._left = left
    def getLeft(self):
        return self._left
    left = property(getLeft,setLeft,None,'')
    def setRight(self,right):
        self._right = right
    def getRight(self):
        return self._Right
    right = property(getRight,setRight,None,'')
    def setTop(self,top):
        self._top = top
    def getTop(self):
        return self._top
    top = property(getTop,setTop,None,'')
    def setBottom(self,bottom):
        self._bottom = bottom
    def getBottom(self):
        return self._bottom
    bottom = property(getBottom,setBottom,None,'')
    
