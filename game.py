
from tkinter import *
from carre_joueur import CarreJoueur
from enemy import Enemy 
from threading import Thread
import time
from espace_jeu import EspaceJeu


WIDTH = 700
HEIGHT = 500

class GameWindow:
    
    def __init__(self, tab_enemy=[]):
        self.tab_enemy = tab_enemy
    
    def start(self):
        #create the frame tk
        self.root = Tk()
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        x = (self.w - WIDTH) // 2
        y = (self.h - HEIGHT) // 2
        self.root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

        #create the player
        self.c = CarreJoueur(10,10,30,30)

        #create canvas
        self.create_canvas()

        #draw espace de jeu
        self.create_espace_jeu()

        #draw player on the canvas
        self.c.draw(self.can)

        #create enemies
        self.draw_enemy_in_canvas()
        self.loop_enemy()

        #add events
        self.bind_event_to_root()

        #launch the app
        self.root.mainloop()

    def create_canvas(self):
        self.can = Canvas(self.root, width=WIDTH, height=HEIGHT, bg="white")
        self.can.pack()
    
    def create_espace_jeu(self):
        self.espace_jeu = EspaceJeu()
        self.espace_jeu.draw(self.can)
    
    def draw_enemy_in_canvas(self):
        for e in self.tab_enemy:
            e.draw(self.can)
    
    def move_enemy_in_canvas(self):
        while True:
            for e in self.tab_enemy:
                a, b, c = e.moving_around(WIDTH, HEIGHT)
                try:
                    self.can.move(a, b, c)
                except:
                    exit()
            time.sleep(0.025)
    
    def loop_enemy(self):
        t = Thread(target=self.move_enemy_in_canvas)
        t.start()

    #events
    def bind_event_to_root(self):
        self.root.bind('<Key>', self.press_arrow_move)


    def press_arrow_move(self, a):
        if a.keysym == 'Down':
            a, b, c = self.c.go_down()
            self.can.move(a, b, c)
        elif a.keysym == "Up":
            a, b, c = self.c.go_up()
            self.can.move(a, b, c)
        elif a.keysym == "Left":
            a, b, c = self.c.go_left()
            self.can.move(a, b, c)
        elif a.keysym == "Right":
            a, b, c = self.c.go_right()
            self.can.move(a, b, c)


# launch the game itself
if __name__ == '__main__':
    
    tab_enemy = [
        Enemy(460, 130, 480, 150, 5, 5, "enemy1"),
        Enemy(90, 90, 110, 110, -5, 5, "enemy2")
    ]

    g = GameWindow(tab_enemy)
    g.start()

    

