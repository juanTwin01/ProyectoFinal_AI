
import time

from tkinter import *
from tkinter import ttk
from turtle import bgcolor, pos

from open_csv import *


from dfs import *
from ucs import *
from bfs import *
from ids import ids
from _A import A_estrella
from greedy import greedy


class Labyrinth_Graphics:

    def __init__(self, root, G, start, end):

        self.root = root
        self.start = start
        self.end = end
        self.labyrinth_graph = G

        
        self.root.title("Example Fast")
        self.root.geometry('1000x1000+50+50')
        self.root.resizable(False, False)

        mainframe = ttk.Frame(self.root)

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        s = ttk.Style()
        s.configure('btnStyle.TFrame', background='green')

        btn_canvas = ttk.Frame(mainframe, style='btnStyle.TFrame')
        btn_canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        dfs_btn = ttk.Button(btn_canvas, text="DFS", command=self.dfs)
        dfs_btn.grid(column=0, row=0, padx=5, pady=5)

        bfs_btn = ttk.Button(btn_canvas, text="BFS", command=self.bfs)
        bfs_btn.grid(column=1, row=0, padx=5, pady=5)

        ucs_btn = ttk.Button(btn_canvas, text="Uniform Cost Search", command=self.ucs)
        ucs_btn.grid(column=2, row=0, padx=5, pady=5)

        ids_btn = ttk.Button(btn_canvas, text="IDS", command=self.ids)
        ids_btn.grid(column=3, row=0, padx=5, pady=5)

        Astar_btn = ttk.Button(btn_canvas, text="A*", command=self._A)
        Astar_btn.grid(column=4, row=0, padx=5, pady=5)

        greedy_btn = ttk.Button(btn_canvas, text="Greedy", command=self.greedy)
        greedy_btn.grid(column=5, row=0, padx=5, pady=5)


        frame_canvas = ttk.Frame(mainframe,padding='50 100 0 0')
        frame_canvas.grid(column=0, row=1, sticky=(N, W, E, S))

        self.cv = Canvas(frame_canvas, width=900, height=900, background='gray75' )
        self.cv.grid(column=0, row=0)

        width_Cv = 900
        height_Cv = 900


        self.labyrinth_ex, vertex = open_labyrinth()

        size_rectangles = width_Cv/len(self.labyrinth_ex)

        self.squares = []

        posY = 0
        for row in self.labyrinth_ex:
            posX = 0
            for col in row:

                fill_col = 'black'
                
                if(col != 'w'): 
                    fill_col = 'gray'
                    if(col == start): fill_col = 'green'
                    if(col == end): fill_col = 'white'
                    
                    a = self.cv.create_rectangle(posX, posY, size_rectangles+posX, size_rectangles+posY, fill=fill_col, tags=f'{col}')
                    self.squares.append(a)
                else:
                    a = self.cv.create_rectangle(posX, posY, size_rectangles+posX, size_rectangles+posY, fill=fill_col)
                
                
                posX += size_rectangles
                

            posY += size_rectangles

        
    def clean_squares(self):

        fill_col = 'gray'
        for i in self.squares:
            self.cv.itemconfigure(i, fill=fill_col)

        for i in self.squares:
            if(self.cv.gettags(i)[0] == self.start): 
                self.cv.itemconfigure(i, fill='green')
            elif self.cv.gettags(i)[0] == self.end: 
                self.cv.itemconfigure(i, fill='white')


    def get_canvas(self):
        return self.cv


    def paint_block(self, i, color):
        self.cv.itemconfigure(i, fill=color)


    def tags_squares(self):

        dicti = {}


        arr = []

        for i in self.squares:
            arr.append(self.cv.gettags( i )[0])

        for i in range(0, len(arr)):
            dicti[arr[i]] = self.squares[i]
        
        return dicti


    def dfs(self):
        
        v, v_nodes = dfs(self.labyrinth_graph, self.start, self.end)
        
        nodes = v_nodes
        dicti = self.tags_squares()

        for i in nodes:
            
            self.cv.itemconfigure(dicti[i], fill='red')
            self.root.update()
            time.sleep(0.1)
                

        time.sleep(2)    
        self.clean_squares()



        


    def ucs(self):

        all_paths_to_end, low_cost_path = ucs(self.labyrinth_graph, self.start, self.end)

        print(all_paths_to_end)

        color_list = ['red','blue','#45458B', '#A5A52A', '#CDCD33']
        cnt = 0

        dicti = self.tags_squares()
        for j in all_paths_to_end:
            nodes = list(j)

            for i in nodes:

                self.cv.itemconfigure(dicti[i], fill=color_list[cnt%len(color_list)])
                self.root.update()
                time.sleep(0.1)
            
            cnt += 1

        time.sleep(2)  
        self.clean_squares()      



    def bfs(self):

        v_nodes = bfs(self.labyrinth_graph, self.start, self.end)
        
        nodes = v_nodes
        dicti = self.tags_squares()

        for i in nodes:
            
            self.cv.itemconfigure(dicti[i], fill='red')
            self.root.update()
            time.sleep(0.1)
                

        time.sleep(2)    
        self.clean_squares()


    def ids(self):
        v_nodes = ids(self.labyrinth_graph, self.start, self.end, 8)

        nodes = v_nodes
        dicti = self.tags_squares()

        for i in nodes:
            
            self.cv.itemconfigure(dicti[i], fill='red')
            self.root.update()
            time.sleep(0.1)
                

        time.sleep(2)    
        self.clean_squares()




    def _A(self):

        labyrinth_matrix, vertex_labyrinth = open_labyrinth()

        r_start = 0
        c_start = 0

        for i in labyrinth_matrix:

            if self.start in i:
                c_start = i.index(self.start)
                break

            r_start += 1

        r_end = 0
        c_end = 0 

        for i in labyrinth_matrix:

            if self.end in i:
                c_end = i.index(self.end)
                break

            r_end += 1

        



        v_nodes = A_estrella( alt_open_labyrinth(), (r_start, c_start), (r_end, c_end), len(labyrinth_matrix))

        nodes = []
        dicti = self.tags_squares()

        for i in v_nodes:
            nodes.append(labyrinth_matrix[i[0]][i[1]])


        for i in nodes:
            
            self.cv.itemconfigure(dicti[i], fill='red')
            self.root.update()
            time.sleep(0.1)
                

        time.sleep(2)    
        self.clean_squares()

    def greedy(self):

        labyrinth_matrix, vertex_labyrinth = open_labyrinth()

        r_start = 0
        c_start = 0

        for i in labyrinth_matrix:

            if self.start in i:
                c_start = i.index(self.start)
                break

            r_start += 1

        r_end = 0
        c_end = 0 

        for i in labyrinth_matrix:

            if self.end in i:
                c_end = i.index(self.end)
                break

            r_end += 1


        v_nodes = greedy( alt_open_labyrinth(), (r_start, c_start), (r_end, c_end), len(labyrinth_matrix))

        nodes = []
        dicti = self.tags_squares()

        for i in v_nodes:
            nodes.append(labyrinth_matrix[i[0]][i[1]])
            

        for i in nodes:
            
            self.cv.itemconfigure(dicti[i], fill='red')
            self.root.update()
            time.sleep(0.1)
                

        time.sleep(2)    
        self.clean_squares()