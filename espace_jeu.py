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
        self.draw_start_end(canvas)

    def draw_start_end(self, canvas):
        canvas.create_rectangle(10,10,50,50, fill="yellow")
        canvas.create_rectangle(600,400,650,450, fill="green")