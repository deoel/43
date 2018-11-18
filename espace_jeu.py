import os

class EspaceJeu:

    def __init__(self):
        self.tab_line = []
        self.load_lines()

    def load_lines(self):
        all_lines = list()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_file = os.path.join(dir_path, 'level1.txt')
        with open(path_file, 'r') as f:
            content = f.readlines()
            content = content[1:]
            for line in content:
                if line.strip() == '':
                    continue
                t = [int(x) for x in line.strip().split(',')]
                all_lines.append(t)
        self.tab_line = all_lines

    def draw(self, canvas):
        for line in self.tab_line:
            x1, y1, x2, y2 = line
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)

    def draw_start_end(self, canvas):
        pass