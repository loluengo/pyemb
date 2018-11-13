
def hoopSize(w,h):
    if w < 500 and h < 500: return 1
    elif w < 1260 and h < 1100: return 3
    elif w < 1400 and h< 2000: return 2
    elif w < 2000 and h < 2000: return 4
    else: return 0

from jefAux import Bounds,Hoop
import struct
import EmbPattern
from Stitch import *
from Thread import jefThreads, EmbThread
from datetime import datetime

class jefPattern(EmbPattern.EmbPattern):
    def __init__(self):
        super().__init__()
                
    def read(self, filename):
        f = open(filename,'rb')
        # read header
        head = 'ii 8s8s iii iiii iiii iiii iiii iiii'
        buf = f.read(struct.calcsize(head))
        data = struct.unpack(head,buf)
        self.stitchOffset = data[0]
        self.formatFlags = data[1]
        self.date = data[2]
        self.time = data[3]
        self.numberOfColors = data[4]
        self.numberOfStitchBytes = data[5]*2
        self.hoopSize = data[6]
        self.setHoopFromId(data[6])
        self.bounds = Bounds(*data[7:11])
        self.rectFrom110x110 = Bounds(*data[11:15])
        self.rectFrom50x50 = Bounds(*data[15:19])
        self.rectFrom200x140 = Bounds(*data[19:23])
        self.rectFromCustom = Bounds(*data[23:27])
        
        thr = 'i'*32
        buf = f.read(struct.calcsize(thr))
        data = struct.unpack(thr,buf)
        self.threadList= [jefThreads[x % 79] for x in data]
        
        f.seek(self.stitchOffset)
        
        stitchBytes = 0
        while stitchBytes < self.numberOfStitchBytes:
            flags = StitchFlags(normal=True)
            buf = f.read(2)
            b0,b1 = struct.unpack('BB',buf)
            stitchBytes += 2
            if b0 == 0x80:
                if b1 & 0x01:
                    buf = f.read(2)
                    b0,b1 = struct.unpack('BB',buf)
                    stitchBytes +=2
                    flags = StitchFlags(stop=True) # STOP
                elif b1 in (0x02,0x04,0x06):
                    flags = StitchFlags(trim=True) # TRIM
                    buf = f.read(2)
                    b0,b1 = struct.unpack('BB',buf)
                    stitchBytes +=2
                elif b1 == 0x10:
                    self.stitchList.append(Stitch(0,0,StitchFlags(end=True),1))
                    stitchBytes +=1
                    break
            b0,b1 = struct.unpack('bb',buf)
            dx = b0 / 10.0
            dy = b1 / 10.0
            self.addStitchRel(dx,dy,flags,1)
        f.close()
        
        if self.stitchList[-1].flags.end != True:
            self.stitchList.append(Stitch(0,0,StitchFlags(end=True),1))
            
    def write(self, filename):
        if self.stitchList[-1].flags.end != True:
            self.stitchList.append(Stitch,0.0,0.0,StitchFlags(end=True),1)
        f = open(filename,'wb')
        self.correctForMaxStitchLength(12.7,12.7)
        colorListSize = len(self.threadList)
        f.write(struct.pack('I',0x74 + colorListSize*8))
        f.write(struct.pack('I',0x14))
        
        dt = datetime.now().strftime('%Y%m%d%H%M%S') + '\x00\x00'
        f.write(bytes(dt,'latin1'))
        
        f.write(struct.pack('I',len(self.threadList)))
        
        f.write(struct.pack('I',len(self.stitchList)+self.jumpStopCount()))
        
        bb = self.calcBoundingBox()
        
        f.write(struct.pack('I',jefPattern.getHoopSizeCode(bb.width,bb.height)))
        
        w = 10*bb.width
        h = 10*bb.height
        print('w',w)
        print('h',h)
        print(bb,bb.width,bb.height)
        # distance from center
        f.write(struct.pack('4I',w//2,h//2,w//2,h//2))
        
        # distance from 110x110 hoop
        if min(550-w/2,550-h/2) >= 0:
            f.write(struct.pack('4I',550-w//2,550-h//2,550-w//2,550-h//2))
        else:
            f.write(struct.pack('4I',-1,-1,-1,-1))
        # distance from 50x50 hoop
        if min(250-w/2,250-h/2) >= 0:
            f.write(struct.pack('4I',250-w//2,250-h//2,250-w//2,250-h//2))
        else:
            f.write(struct.pack('4I',-1,-1,-1,-1))
            
        #distance from 140x200 hoop
        f.write(struct.pack('4I',
                            max(-1,700-w//2),
                            max(-1,1000-h//2),
                            max(-1,700-w//2),
                            max(-1,1000-h//2)))
        #distance from custom (140x200) hoop
        f.write(struct.pack('4I',
                            max(-1,700-w//2),
                            max(-1,1000-h//2),
                            max(-1,700-w//2),
                            max(-1,1000-h//2)))
        
        for th in self.threadList:
            index,color = EmbThread.findNearestColor(th.color,jefThreads)
            f.write(struct.pack('I',index))
            
        f.write(struct.pack('%dI'%colorListSize,*[0x0D]*colorListSize))
        
        xx = 0
        yy = 0
        
        for st in self.stitchList:
            dx = int(st.x*10 - xx)
            dy = int(st.y*10 - yy)
            xx = st.x*10
            yy = st.y*10
            if st.flags.stop:
                f.write(struct.pack('BBbb',0x80,0x01,dx,dy))
            elif st.flags.end:
                f.write(struct.pack('BBBB',0x80,0x10,0,0))
            elif st.flags.trim:
                f.write(struct.pack('BBbb',0x80,0x02,dx,dy))
            elif st.flags.jump:
                f.write(struct.pack('BBbb',0x80,0x04,dx,dy))
            else:
                f.write(struct.pack('bb',dx,dy))
        f.close()
                
    @staticmethod
    def getHoopSizeCode(w,h):
        w *= 10
        h *= 10
        if(w <  500 and h <  500) : return Hoop.SIZE_50x50
        elif(w < 1260 and h < 1100) : return Hoop.SIZE_126x110
        elif(w < 1400 and h < 2000) : return Hoop.SIZE_140x200
        elif(w < 2000 and h < 2000) : return Hoop.SIZE_200x200
        else: return Hoop.SIZE_110x110

        
        
    def setHoopFromId(self,hoopCode):
        if hoopCode == 3:
            self.hoop.height = 126.0
            self.hoop.width = 110.0
        elif hoopCode == 1:
            self.hoop.height = 50.0
            self.hoop.width = 50.0
        elif hoopCode == 0:
            self.hoop.height = 110.0
            self.hoop.width = 110.0
        elif hoopCode == 2:
            self.hoop.height = 140.0
            self.hoop.width = 200.0
        elif hoopCode == 4:
            self.hoop.height = 200.0
            self.hoop.width = 200.0
    def listFlags(self):
        return [fn for s in self.stitchList for fn,fv in s.flags.flags.items() if fv==True]