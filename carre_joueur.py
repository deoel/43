class CarreJoueur:

    def __init__(self, x0, y0, x1, y1, tag="joueur", couleur="red"):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.tag = tag
        self.couleur = couleur
    
    def go_down(self):
        x = 0
        y = 10
        m = (self.tag, x, y)
        self.y0 += y
        self.y1 += y
        return m
    
    def go_up(self):
        x = 0
        y = -10
        m = (self.tag, x, y)
        self.y0 += y
        self.y1 += y
        return m
    
    def go_left(self):
        x = -10
        y = 0
        m = (self.tag, x, y)
        self.x0 += x
        self.x1 += x
        return m

    def go_right(self):
        x = 10
        y = 0
        m = (self.tag, x, y)
        self.x0 += x
        self.x1 += x
        return m
    
    def display(self):
        print(self.x0, self.y1, self.x1, self.y1)

    def draw(self, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.couleur, tags=(self.tag))
