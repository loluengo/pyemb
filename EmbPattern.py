from Stitch import *
from EmbGeom import *
from jefAux import Hoop 

class EmbPattern:
	def __init__(self):
		self.hoop = Hoop()
		self.home = (0.0,0.0)
		self.stitchList = []
		
		self.arcList = []
		self.circleList = []
		self.ellipseList = []
		self.lineList = []
		self.pathList = []
		self.pointList = []
		self.polygonList = []
		self.polylineList = []
		self.rectList = []
		self.splineList = []
		
		self.currentColorIndex = 0
		self.lastX = None
		self.lastY = None
	def read(self,filename):
		pass
	def write(self,filename):
		pass
	def addStitchRel(self,dx,dy,flags,isAutoColorIndex):
		if not self.stitchList:
			x = self.home[0] + dx
			y = self.home[1] + dy
		else:
			x = self.stitchList[-1].x + dx
			y = self.stitchList[-1].y + dy
		self.addStitchAbs(x,y,flags,isAutoColorIndex)
	
	def addStitchAbs(self,x,y,flags,isAutoColorIndex):
		if flags.end:
			if not self.stitchList:
				return
			if self.stitchList[-1].flags.end == True:
				raise EmbPatternExc('Multiple END stitches')
			self.fixColorCount()
		if flags.stop:
			if not self.stitchList:
				return
			if isAutoColorIndex:
				self.currentColorIndex +=1
		if not self.stitchList:
			sf = StitchFlags(jump = True)
			self.stitchList.append(Stitch(*self.home,sf,self.currentColorIndex))
		self.stitchList.append(Stitch(x,y,flags,self.currentColorIndex))
		self.lastX = x
		self.lastY = y
	def correctForMaxStitchLength(self,maxStitch,maxJump):
		if len(self.stitchList) > 1:
			for i,(sA,sB) in enumerate(zip(self.stitchList[:-1],self.stitchList[1:])):
				dx,dy = Stitch.dist(sA,sB)
				if dx > maxStitch or dy > maxStitch:
					maxXY = max(dx,dy)
					if sB.flags.jump or sb.flags.trim: maxLen = maxJump
					else: maxLen = maxStitch
					
					splits = maxXY//maxLen +1
					
					if splits > 1:
						flags = sB.flags
						color = sB.color
						addX = dx/splits
						addY = dy/splits
						newStitch = []
						for j in range(splits):
							newX = sB.x + addX*(j+1)
							newY = sB.x + addY*(j+1)
							newStitch.append(Stitch(newX,newY,flags,color))
						for s in newStitch[::-1]:
							self.stitchList.insert(i,s)
		ls = self.stitchList[-1]
		if ls.flags.end != True:
			self.stitchList.append(Stitch(ls.x,ls.y,StitchFlags(end=True),1))
			
	def jumpStopCount(self):
		js = [x for x in self.stitchList if (x.flags.stop or x.flags.trim or x.flags.jump)]
		return len(js)
		
	def calcBoundingBox(self):
		if not (self.stitchList and self.arcList and self.circleList and self.ellipseList and self.lineList and self.pointList and self.polygonList and self.polylineList and self.rectList and self.splineList):
			return EmbRect(0,0,1,1)
		bboxes = {}
		sl = [s for s in self.stitchList if s.flags.trim == False]
		l = min([s.x for s in sl])
		r = max([s.x for s in sl])
		t = max([s.y for s in sl])
		b = min([s.y for s in sl])
		bboxes['stitches'] = EmbRect(l,r,t,b)
		
		bboxes['arcs'] = None # TODO: method for arcs bbox
		
		l = min([c.centerX-c.radius for c in circleList])
		r = max([c.centerX+c.radius for c in circleList])
		t = max([c.centerY+c.radius for c in circleList])
		l = min([c.centerY-c.radius for c in circleList])
		
		bboxes['circles'] = EmbRect(l,r,t,b)
		
		bboxes['ellipses'] = None # TODO: method for elipse bbox
		
		bboxes['points'] = None # TODO: method for points bbox
		bboxes['polygons'] = None # TODO: method for points bbox
		bboxes['polylines'] = None # TODO: method for points bbox
		bboxes['rectangles'] = None # TODO: method for points bbox
		bboxes['splines'] = None # TODO: method for points bbox
		
		l = min([r.left for r in bboxes.values() if r is not None])
		r = max([r.right for r in bboxes.values() if r is not None])
		t = max([r.top for r in bboxes.values() if r is not None])
		b = min([r.bottom for r in bboxes.values() if r is not None])
		
		return EmbRect(l,r,t,b)