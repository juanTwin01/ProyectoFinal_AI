from graphics_tkinter import Labyrinth_Graphics
from open_csv import *

from graph import EdgeSetGraph, UndirectedEdgeSetGraph
from collections import Counter

from dfs import dfs
import ucs

from tkinter import *

# Imprimir Grafo

def print_Graph(labyrinth):

    for i in labyrinth:
        for j in i:
            print(f"{j}\t", end="")
        print()



# Construccion Grafo

#labyrinth = []


'''with open("maze_5x5.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row) != 0:
            labyrinth.append(row)'''


cnt = 1

#vertex = []
edges = []

'''for i in range(len(labyrinth)):
    for j in range(len(labyrinth[i])):
        if labyrinth[i][j] == 'c':
            labyrinth[i][j] = f'{cnt}'
            vertex.append(labyrinth[i][j])
            cnt += 1
'''
labyrinth, vertex = open_labyrinth()





for i in range(len(labyrinth)):
    for j in range(len(labyrinth[i])):
        if labyrinth[i][j] != 'w':
            
            if i == 0:

                # Esq. superior izquierda
                if j == 0:
                    if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                    if labyrinth[i+1][j] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i+1][j]]) )

                # Esq. superior derecha
                elif j == len(labyrinth[0])-1:
                    if labyrinth[i+1][j] != 'w':
                        edges.append( list( [labyrinth[i][j], labyrinth[i+1][j]] ) )

                    if labyrinth[i][j-1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j-1]]) )


                # Lateral superior
                else:
                    if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                    if labyrinth[i][j-1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j-1]]) )
                    
                    if labyrinth[i+1][j] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i+1][j]]) )


                  
            
            elif i == len(labyrinth)-1:
                
                # Esquina inferior izquierda
                if j == 0: 
                    if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                    if labyrinth[i-1][j] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i-1][j]]) )


                # Esq. inferior derecha
                elif j == len(labyrinth[0])-1:
                    if labyrinth[i][j-1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j-1]]) )

                    if labyrinth[i-1][j] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i-1][j]]) )

                # Lateral inferior
                else:
                    
                    if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                    if labyrinth[i][j-1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j-1]]) )
                    
                    if labyrinth[i-1][j] != 'w':
                        edges.append(list( [labyrinth[i][j], labyrinth[i-1][j]]) )

            # Lateral izquierda
            elif j == 0:
                if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                if labyrinth[i-1][j] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i-1][j]]) )
                    
                if labyrinth[i+1][j] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i+1][j]]) )

            # Lateral derecha
            elif j == len(labyrinth[0])-1:
                if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                if labyrinth[i-1][j] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i-1][j]]) )
                    
                if labyrinth[i+1][j] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i+1][j]]) )

            # Centrales
            else:
                if labyrinth[i][j+1] != 'w':
                        edges.append( list([labyrinth[i][j], labyrinth[i][j+1]]) )

                if labyrinth[i+1][j] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i+1][j]]) )
                    
                if labyrinth[i-1][j] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i-1][j]]) )

                if labyrinth[i][j-1] != 'w':
                    edges.append( list([labyrinth[i][j], labyrinth[i][j-1]]) )    



for a in edges:
    for b in edges:
        
        if a != b and Counter(a)==Counter(b):
            edges.remove(b)


labyrinth_graph = UndirectedEdgeSetGraph(vertex, edges)


# Construccion Grafo, Concluida

# ALGORITMOS
start = '1'
end = '18'
# DFS


# Tkinter Build Labyrinth


if __name__ == '__main__':
    root = Tk()
    labyrinth_Widget = Labyrinth_Graphics(root, labyrinth_graph, start, end)

    canvas = labyrinth_Widget.get_canvas()

    root.mainloop()


    



    


