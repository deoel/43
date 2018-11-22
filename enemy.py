
class Enemy:

    def __init__(self, posx, posy, w, h, speedx=10, speedy=10, tag="enemy", couleur="blue"):
        self.posx = posx
        self.posy = posy
        self.w = w
        self.h = h
        self.tag = tag
        self.couleur = couleur
        self.speedx = speedx
        self.speedy = speedy
    
    def moving_around(self, limitw, limith):
        if self.posx >= limitw:
            self.speedx *= (-1)
        elif self.posx <= 0:
            self.speedx *= (-1)
        elif self.posy >= limith:
            self.speedy *= (-1)
        elif self.posy <= 0:
            self.speedy *= (-1)
        self.posx += self.speedx
        self.posy += self.speedy
        m = (self.tag, self.speedx, self.speedy)
        return m
    
    def draw(self, canvas):
        id = canvas.create_oval(self.posx, self.posy, self.w, self.h, fill=self.couleur, tags=(self.tag))
        return id

    
