class Stitch:
	def __init__(self,x,y,flags,color):
		self.x = x
		self.y = y
		self.flags = flags
		self.color = color
	@staticmethod
	def dist(sA,sB):
		return (abs(sA.x - sB.x),abs(sA.y - sB.y))
		
class StitchFlags:
	def __init__(self,normal=None,jump=None,trim=None,stop=None,sequin=None,end=None):
		self._normal = normal
		self._jump = jump
		self._trim = trim
		self._stop = stop
		self._sequin = sequin
		self._end = end
	def setNormal(self,value = True):
		self._normal = value
	def getNormal(self):
		return self._normal
	normal = property(getNormal,setNormal,None,'Normal stitch flag')
	def setJump(self,value = True):
		self._jump = value
	def getJump(self):
		return self._jump
	jump = property(getJump,setJump,None,'Jump stitch flag')
	def setTrim(self,value = True):
		self._trim = value
	def getTrim(self):
		return self._trim
	trim = property(getTrim,setTrim,None,'Trim stitch flag')
	def setStop(self,value = True):
		self._stop = value
	def getStop(self):
		return self._stop
	stop = property(getStop,setStop,None,'Stop stitch flag')
	def setSequin(self,value = True):
		self._sequin = value
	def getSequin(self):
		return self._sequin
	sequin = property(getSequin,setSequin,None,'Sequin stitch flag')
	def setEnd(self,value = True):
		self._End = value
	def getEnd(self):
		return self._end
	end = property(getEnd,setEnd,None,'End stitch flag')
	
	def getFlags(self):
		return { 'normal': self._normal,
		'jump': self._jump,
		'trim': self._trim,
		'stop': self._stop,
		'sequin': self._sequin,
		'end': self._end
		}
	flags = property(getFlags)

