import os

COLOR_YELLOW = "yellow"

class Coin:

    def __init__(self, fichier_coin):
        self.tab_coins = []
        self.fichier_coin = fichier_coin
        self.load_coins()

    def load_coins(self):
        all_coins = list()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_file = os.path.join(dir_path, self.fichier_coin)
        with open(path_file, 'r') as f:
            content = f.readlines()
            content = content[1:]
            for line in content:
                if line.strip() == '':
                    continue
                t = [int(x) for x in line.strip().split(',')]
                all_coins.append(t)
        self.tab_coins = all_coins

    def draw(self, canvas):
        for line in self.tab_coins:
            x, y= line
            canvas.create_oval(x,y,x+15,y+15,fill=COLOR_YELLOW)
