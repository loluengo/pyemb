class EmbArc:
	pass
class EmbCircle:
	pass
class EmbEllipse:
	pass
class EmbLine:
	pass
class EmbPoint:
	pass
class EmbRect:
	def __init__(self,left,right,top,bottom):
		self._left = left
		self._right = right
		self._top = top
		self._bottom = bottom
	def getLeft(self):
		return self._left
	def setLeft(self,left):
		self._left = left
	left = property(getLeft,setLeft,None,'')
	
	def getRight(self):
		return self._right
	def setRight(self,right):
		self._right = right
	right = property(getRight,setRight,None,'')
	
	def getTop(self):
		return self._top
	def setTop(self,top):
		self._top = top
	top = property(getTop,setTop,None,'')
	
	def getBottom(self):
		return self._bottom
	def setBottom(self,bottom):
		self._bottom = bottom
	bottom = property(getBottom,setBottom,None,'')
	
	def getWidth(self):
		return self._right - self._left
	width = property(getWidth,None,None,'Rectangle width')
	def getHeight(self):
		return self._top - self._bottom
	height = property(getHeight,None,None,'Rectangle height')
	
class EmbBezier:
	pass
