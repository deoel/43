
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s) " % (self.x, self.y)
    
class Coord_XY_XY:

    def __init__(self, x0,y0,x1,y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.creer_point()
    
    def __str__(self):
        return self.A.__str__() + self.B.__str__() + self.C.__str__() + self.D.__str__()

    def creer_point(self):
        A = Point(self.x0, self.y0)
        B = Point(self.x1, self.y0)
        C = Point(self.x0, self.y1)
        D = Point(self.x1, self.y1)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    
    def collision(self, CXY):
        if self.A.y > CXY.C.y:
            return False
        elif self.B.x < CXY.A.x:
            return False
        elif self.D.y < CXY.B.y:
            return False
        elif self.C.x > CXY.D.x:
            return False
        else: 
            return True
    
    def in_limite(self, CXY):
        if self.A.x <= CXY.A.x and CXY.A.x <= self.B.x:
            if self.A.x <= CXY.B.x and CXY.B.x <= self.B.x:
                if self.A.y <= CXY.A.y and CXY.A.y <= self.C.y:
                    if self.A.y <= CXY.C.y and CXY.C.y <= self.C.y:
                        return True
        return False

