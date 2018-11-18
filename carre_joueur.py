class CarreJoueur:

    def __init__(self, posx, posy, w, h, tag="joueur", couleur="red"):
        self.posx = posx
        self.posy = posy
        self.w = w
        self.h = h
        self.tag = tag
        self.couleur = couleur
    
    def go_down(self):
        x = 0
        y = 10
        m = (self.tag, x, y)
        return m
    
    def go_up(self):
        x = 0
        y = -10
        m = (self.tag, x, y)
        return m
    
    def go_left(self):
        x = -10
        y = 0
        m = (self.tag, x, y)
        return m

    def go_right(self):
        x = 10
        y = 0
        m = (self.tag, x, y)
        return m

    def draw(self, canvas):
        canvas.create_rectangle(self.posx, self.posy, self.w, self.h, fill=self.couleur, tags=(self.tag))
