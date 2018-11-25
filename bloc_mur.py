import os

COLOR = "pink"

class BlocMur:

    def __init__(self, fichier_bloc_mur):
        self.tab_bloc_mur = []
        self.fichier_bloc_mur = fichier_bloc_mur
        self.load_bloc_mur()

    def load_bloc_mur(self):
        all_bloc_mur = list()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_file = os.path.join(dir_path, self.fichier_bloc_mur)
        with open(path_file, 'r') as f:
            content = f.readlines()
            content = content[1:]
            for line in content:
                if line.strip() == '':
                    continue
                t = [int(x) for x in line.strip().split(',')]
                all_bloc_mur.append(t)
        self.tab_bloc_mur = all_bloc_mur

    def draw(self, canvas):
        tab_id = list()
        for line in self.tab_bloc_mur:
            x0, y0, x1, y1 = line
            id = canvas.create_rectangle(x0, y0, x1, y1,fill=COLOR, outline=COLOR)
            tab_id.append(id)
        return tab_id
