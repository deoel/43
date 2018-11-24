
class Enemy:

    def __init__(self, x0, y0, x1, y1, speedx=10, speedy=10, tag="enemy", couleur="blue"):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.tag = tag
        self.couleur = couleur
        self.speedx = speedx
        self.speedy = speedy
    
    def moving_around(self, limitx1, limity1):
        if self.x0 >= limitx1:
            self.speedx *= (-1)
        elif self.x0 <= 0:
            self.speedx *= (-1)
        elif self.y0 >= limity1:
            self.speedy *= (-1)
        elif self.y0 <= 0:
            self.speedy *= (-1)
        self.x0 += self.speedx
        self.x1 += self.speedx
        self.y0 += self.speedy
        self.y1 += self.speedy
        m = (self.tag, self.speedx, self.speedy)
        return m
    
    def draw(self, canvas):
        id = canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.couleur, tags=(self.tag))
        return id

    
