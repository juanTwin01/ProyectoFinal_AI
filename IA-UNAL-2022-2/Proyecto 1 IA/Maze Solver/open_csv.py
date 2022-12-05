import csv

def open_labyrinth():
    labyrinth = [ ]
    vertex = []

    with open("maze_10x10.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) != 0:
                labyrinth.append(row)

    
    cnt = 1 

    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 'c':
                labyrinth[i][j] = f'{cnt}'
                vertex.append(labyrinth[i][j])
                cnt += 1

    return labyrinth, vertex

def alt_open_labyrinth():
    labyrinth = []

    with open("maze_10x10.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) != 0:
                labyrinth.append(row)

    cnt = 1
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 'c':
                labyrinth[i][j] = 'C'
                cnt += 1
            else:
                labyrinth[i][j] = 'M'

    return labyrinth