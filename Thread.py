from numpy import array,sqrt
import random

class EmbColor:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        
    def __sub__(self,y):
        return self.asArray() - y.asArray()
        
    def asArray(self):
        return array((self.r,self.g,self.b))
        
    @staticmethod
    def dist(colorA,colorB):
        return sqrt(sum((colorA-colorB)**2))
        
    @staticmethod
    def randColor():
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        return EmbColor(r,g,b)
        
        
    
class EmbThread:
    def __init__(self,color,description,catalogNumber):
        self._color = color
        self._description = description
        self._catN = catalogNumber
    def getColor(self):
        return self._color
    def setColor(self,color):
        self._color = color
    color = property(getColor,setColor,None,'Thread color')
    def getDescription(self):
        return self._description
    def setDescription(self,description):
        self._description = description
    description = property(getDescription,setDescription,None,'Thread description')
    def getCatalogNumber(self):
        return self._catN
    def setCatalogNumber(self,catN):
        self._catN = catN
    description = property(getCatalogNumber,setCatalogNumber,None,'Thread catalog number')
    
    @staticmethod
    def findNearestColor(color,threadList):
        d = [EmbColor.dist(color,x.color) for x in threadList]
        i = min(enumerate(d),key = lambda x: x[1])[0]
        return (i,threadList[i])
    
    @staticmethod
    def getRandom():
        return EmbThread(EmbColor.randColor(),'random','')
        
jefThreads = [
    EmbThread(EmbColor(0, 0, 0), "Black", ""),
    EmbThread(EmbColor(0, 0, 0), "Black", ""),
    EmbThread(EmbColor(255, 255, 255), "White", ""),
    EmbThread(EmbColor(255, 255, 23), "Yellow", ""),
    EmbThread(EmbColor(250, 160, 96), "Orange", ""),
    EmbThread(EmbColor(92, 118, 73), "Olive Green", ""),
    EmbThread(EmbColor(64, 192, 48), "Green", ""),
    EmbThread(EmbColor(101, 194, 200), "Sky", ""),
    EmbThread(EmbColor(172, 128, 190), "Purple", ""),
    EmbThread(EmbColor(245, 188, 203), "Pink", ""),
    EmbThread(EmbColor(255, 0, 0), "Red", ""),
    EmbThread(EmbColor(192, 128, 0), "Brown", ""),
    EmbThread(EmbColor(0, 0, 240), "Blue", ""),
    EmbThread(EmbColor(228, 195, 93), "Gold", ""),
    EmbThread(EmbColor(165, 42, 42), "Dark Brown", ""),
    EmbThread(EmbColor(213, 176, 212), "Pale Violet", ""),
    EmbThread(EmbColor(252, 242, 148), "Pale Yellow", ""),
    EmbThread(EmbColor(240, 208, 192), "Pale Pink", ""),
    EmbThread(EmbColor(255, 192, 0), "Peach", ""),
    EmbThread(EmbColor(201, 164, 128), "Beige", ""),
    EmbThread(EmbColor(155, 61, 75), "Wine Red", ""),
    EmbThread(EmbColor(160, 184, 204), "Pale Sky", ""),
    EmbThread(EmbColor(127, 194, 28), "Yellow Green", ""),
    EmbThread(EmbColor(185, 185, 185), "Silver Grey", ""),
    EmbThread(EmbColor(160, 160, 160), "Grey", ""),
    EmbThread(EmbColor(152, 214, 189), "Pale Aqua", ""),
    EmbThread(EmbColor(184, 240, 240), "Baby Blue", ""),
    EmbThread(EmbColor(54, 139, 160), "Powder Blue", ""),
    EmbThread(EmbColor(79, 131, 171), "Bright Blue", ""),
    EmbThread(EmbColor(56, 106, 145), "Slate Blue", ""),
    EmbThread(EmbColor(0, 32, 107), "Nave Blue", ""),
    EmbThread(EmbColor(229, 197, 202), "Salmon Pink", ""),
    EmbThread(EmbColor(249, 103, 107), "Coral", ""),
    EmbThread(EmbColor(227, 49, 31), "Burnt Orange", ""),
    EmbThread(EmbColor(226, 161, 136), "Cinnamon", ""),
    EmbThread(EmbColor(181, 148, 116), "Umber", ""),
    EmbThread(EmbColor(228, 207, 153), "Blonde", ""),
    EmbThread(EmbColor(225, 203, 0), "Sunflower", ""),
    EmbThread(EmbColor(225, 173, 212), "Orchid Pink", ""),
    EmbThread(EmbColor(195, 0, 126), "Peony Purple", ""),
    EmbThread(EmbColor(128, 0, 75), "Burgundy", ""),
    EmbThread(EmbColor(160, 96, 176), "Royal Purple", ""),
    EmbThread(EmbColor(192, 64, 32), "Cardinal Red", ""),
    EmbThread(EmbColor(202, 224, 192), "Opal Green", ""),
    EmbThread(EmbColor(137, 152, 86), "Moss Green", ""),
    EmbThread(EmbColor(0, 170, 0), "Meadow Green", ""),
    EmbThread(EmbColor(33, 138, 33), "Dark Green", ""),
    EmbThread(EmbColor(93, 174, 148), "Aquamarine", ""),
    EmbThread(EmbColor(76, 191, 143), "Emerald Green", ""),
    EmbThread(EmbColor(0, 119, 114), "Peacock Green", ""),
    EmbThread(EmbColor(112, 112, 112), "Dark Grey", ""),
    EmbThread(EmbColor(242, 255, 255), "Ivory White", ""),
    EmbThread(EmbColor(177, 88, 24), "Hazel", ""),
    EmbThread(EmbColor(203, 138, 7), "Toast", ""),
    EmbThread(EmbColor(247, 146, 123), "Salmon", ""),
    EmbThread(EmbColor(152, 105, 45), "Cocoa Brown", ""),
    EmbThread(EmbColor(162, 113, 72), "Sienna", ""),
    EmbThread(EmbColor(123, 85, 74), "Sepia", ""),
    EmbThread(EmbColor(79, 57, 70), "Dark Sepia", ""),
    EmbThread(EmbColor(82, 58, 151), "Violet Blue", ""),
    EmbThread(EmbColor(0, 0, 160), "Blue Ink", ""),
    EmbThread(EmbColor(0, 150, 222), "Solar Blue", ""),
    EmbThread(EmbColor(178, 221, 83), "Green Dust", ""),
    EmbThread(EmbColor(250, 143, 187), "Crimson", ""),
    EmbThread(EmbColor(222, 100, 158), "Floral Pink", ""),
    EmbThread(EmbColor(181, 80, 102), "Wine", ""),
    EmbThread(EmbColor(94, 87, 71), "Olive Drab", ""),
    EmbThread(EmbColor(76, 136, 31), "Meadow", ""),
    EmbThread(EmbColor(228, 220, 121), "Mustard", ""),
    EmbThread(EmbColor(203, 138, 26), "Yellow Ochre", ""),
    EmbThread(EmbColor(198, 170, 66), "Old Gold", ""),
    EmbThread(EmbColor(236, 176, 44), "Honeydew", ""),
    EmbThread(EmbColor(248, 128, 64), "Tangerine", ""),
    EmbThread(EmbColor(255, 229, 5), "Canary Yellow", ""),
    EmbThread(EmbColor(250, 122, 122), "Vermillion", ""),
    EmbThread(EmbColor(107, 224, 0), "Bright Green", ""),
    EmbThread(EmbColor(56, 108, 174), "Ocean Blue", ""),
    EmbThread(EmbColor(227, 196, 180), "Beige Grey", ""),
    EmbThread(EmbColor(227, 172, 129), "Bamboo", "")
    ]
