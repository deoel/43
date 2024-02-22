
from tkinter import *
import tkinter.font as tkFont
from enemy import Enemy
from espace_jeu import EspaceJeu
from coin import Coin
from carre_joueur import CarreJoueur
from coord_xy_xy import Coord_XY_XY
from bloc_mur import BlocMur
from threading import Thread
import time, random

WIDTH = 900
HEIGHT = 500
BG = "#b388ff"
COLOR_COIN = "yellow"
COLOR_WHITE = "white"
COLOR_BLACK = "black"
COLOR_YELLOW = "yellow"
COLOR_VIOLET = "#b388ff"
FONT = "Comic Sans MS"
TITRE_GAME= "The Easyest Game EVER"
GAME_OVER = "Game Over!\nVous avez perdu"
GAME_WIN = "Bingo!\nVous avaz gagné"

class Game:
    
    def __init__(self, tab_enemy=None):
        tab_enemy = [] if tab_enemy is None else tab_enemy
        self.flag = False
        self.t = None
        self.points = 0
        self.game_over = False
        self.tab_id_coins = list()
        self.all_id_widget = list()
        self.tab_enemy = tab_enemy
        self.creer_game_window()
        self.creer_canvas_game()
        self.creer_boutons_options()
        self.afficher_texte_sur_canvas(TITRE_GAME)
    
    def creer_game_window(self):
        self.root = Tk()
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        x = (self.w - WIDTH) // 2
        y = (self.h - HEIGHT) // 2
        self.root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))
    
    def lancer_game_window(self):
        self.root.mainloop()

    def creer_canvas_game(self):
        self.can = Canvas(self.root, width=700, height=HEIGHT, bg=BG)
        self.can.grid(row=0,column=0,rowspan=10)
    
    def creer_boutons_options(self):
        self.score = Label(self.root, text='Score : 0', font=(FONT, 18), width=10)
        self.score.grid(row=0,column=1,sticky=N,padx=5)
        self.bouton_jouer = Button(self.root,text="JOUER",font=("Comic Sans MS",16),bg=COLOR_VIOLET, command=self.start, width=10)
        self.bouton_jouer.grid(row=2,column=1,sticky=N,padx=5,pady=5)
        Button(self.root,text="QUITTER",font=("Comic Sans Ms",16),bg=COLOR_VIOLET,command=self.root.destroy, width=10).grid(row=3,column=1,sticky=N,padx=5,pady=5)
    
    # avant de jouer : afficher "The easyest game ever"
    # game over      : afficher "Game over, vous avez perdu"
    # bingo game     : afficher "Bingo, vous avez gagné"

    def afficher_texte_sur_canvas(self, texte):
        self.clean()
        f = tkFont.Font(size=30,family=FONT, weight="bold")
        id = self.can.create_rectangle(0, 0, 700, HEIGHT, fill=BG, outline=COLOR_VIOLET)
        self.all_id_widget.append(id)
        id = self.can.create_text(350,200,text=texte, fill=COLOR_BLACK, activefill=COLOR_YELLOW, font=f, justify="center")
        self.all_id_widget.append(id)

    def start(self):
        self.clean()
        self.score['text'] = "Score : 0"
        self.points = 0
        self.bouton_jouer['text'] = "Recommencer"
        
        self.creer_espace_jeu()
        self.creer_coins()
        self.creer_joueur()

        if not self.flag:
            self.creer_ennemis()
            self.flag = True
        
        if self.game_over:
            self.game_over = False
    
    def clean(self):
        for id in self.all_id_widget:
            self.can.delete(id)
    
    def creer_espace_jeu(self):
        self.bloc_mur = BlocMur("bloc_mur1.txt")
        self.bloc_mur.draw(self.can)
        self.espace_jeu = EspaceJeu()
        self.espace_jeu.draw(self.can)

    def creer_coins(self):
        self.coin = Coin("coins1.txt")        
        self.tab_id_coins = self.coin.draw(self.can)
        for id in self.tab_id_coins:
            self.all_id_widget.append(id)
    
    def deplacer_joueur(self, a):
        self.collision_coin()
        if a.keysym == 'Down':
            a, b, c = self.c.go_down()
            if self.collision_mur():
                self.c.go_up()
            else:
                self.can.move(a, b, c)
        elif a.keysym == "Up":
            a, b, c = self.c.go_up()
            if self.collision_mur():
                self.c.go_down()
            else:
                self.can.move(a, b, c)
        elif a.keysym == "Left":
            a, b, c = self.c.go_left()
            if self.collision_mur():
                self.c.go_right()
            else:
                self.can.move(a, b, c)
        elif a.keysym == "Right":
            a, b, c = self.c.go_right()
            if self.collision_mur():
                self.c.go_left()
            else:
                self.can.move(a, b, c)
        self.win()
    
    def creer_joueur(self, x0=20, y0=20, x1=40, y1=40):
        self.c = CarreJoueur(x0,y0,x1,y1)
        id = self.c.draw(self.can)
        self.all_id_widget.append(id)
        self.root.bind('<Key>', self.deplacer_joueur)
    
    def creer_ennemis(self):
        for e in self.tab_enemy:
            e.draw(self.can)
        self.t = Thread(target=self.deplacer_ennemis)
        self.t.daemon = True
        self.t.start()

    def deplacer_ennemis(self):
        while True:
            if not self.game_over:
                for e in self.tab_enemy:
                    a, b, c = e.moving_around(700, HEIGHT)
                    try:
                        self.can.move(a, b, c)
                        self.collision_ennemi()
                    except:
                        exit()
                time.sleep(0.015)
            else:
                continue

    def collision_coin(self):
        for c in self.coin.tab_coins:
            x0, y0, x1, y1 = c[0], c[1], c[0]+15, c[1]+15
            coord_coin = Coord_XY_XY(x0,y0, x1, y1)
            coord_joueur = Coord_XY_XY(self.c.x0, self.c.y0, self.c.x1, self.c.y1)
            if coord_coin.collision(coord_joueur):
                self.points += 10
                self.score['text'] = "Score : %d" %(self.points)
                id = self.can.create_oval(x0,y0, x1, y1, outline=COLOR_VIOLET, fill=COLOR_VIOLET)
                self.all_id_widget.append(id)
                self.creer_joueur(self.c.x0, self.c.y0, self.c.x1, self.c.y1)

    def collision_mur(self):
        for bm in self.bloc_mur.tab_bloc_mur:
            x0, y0, x1, y1 = bm
            coord_bloc_mur = Coord_XY_XY(x0, y0, x1, y1)
            coord_joueur = Coord_XY_XY(self.c.x0, self.c.y0, self.c.x1, self.c.y1)
            if coord_bloc_mur.in_limite(coord_joueur):
                return False
        return True
    
    def collision_ennemi(self):
        for e in self.tab_enemy:
            coord_ennemi = Coord_XY_XY(e.x0, e.y0, e.x1, e.y1)
            coord_joueur = Coord_XY_XY(self.c.x0, self.c.y0, self.c.x1, self.c.y1)
            if coord_ennemi.collision(coord_joueur):
                self.game_over = True
                self.afficher_texte_sur_canvas(GAME_OVER)
    
    def win(self):
        coord_fin = Coord_XY_XY(600,400,650,450)
        coord_joueur = Coord_XY_XY(self.c.x0, self.c.y0, self.c.x1, self.c.y1)
        if coord_fin.in_limite(coord_joueur):
            self.game_over = True
            self.afficher_texte_sur_canvas(GAME_WIN)

# launch the game itself
if __name__ == '__main__':   
    tab_enemy = list()
    i = 1
    for i in range(1,5):
        x0 = 10
        y0 = 100 * i
        x1 = x0 + 20
        y1 = y0 + 20
        e = Enemy(x0, y0, x1, y1, 5, 5, "enemy"+str(i))
        tab_enemy.append(e)
    j = 1
    for i in range(5,10):
        x0 = 600
        y0 = 50 * j
        x1 = x0 + 20
        y1 = y0 + 20
        e = Enemy(x0, y0, x1, y1, -5, 0, "enemy"+str(i))
        tab_enemy.append(e)
        j += 2

    g = Game(tab_enemy)
    g.lancer_game_window()
    


