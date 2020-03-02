def addtodict(dict,x,y):
    coor = (str(x)+','+str(y))
    dist = abs(x) + abs(y)
    dict.update({coor:dist})

def searchindict(dict,list,x,y):
        coord = (str(x)+','+str(y))
        if coord in grid.keys():
            list.append(dict[coord])

import csv

with open('day3_input.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    grid={}
    intersection =[]
    rows = 0
    for row in csv_reader:
        x = 0
        y = 0
        rows += 1
        for item in row:
            dir =item[0]
            length = int(item[1:])
            x_orig = x
            y_orig = y
            if dir == 'U':
                y = y_orig + length
                for i in range(length+1):
                    if rows ==1:
                        addtodict(grid,x_orig,y_orig+i)
                    else:
                        searchindict(grid,intersection,x_orig,y_orig+i)
            elif dir =='D':
                y = y_orig - length
                for i in range(length+1):
                    if rows == 1:
                        addtodict(grid,x_orig,y_orig-i)
                    else:
                        searchindict(grid,intersection,x_orig,y_orig-i)
            elif dir == 'R':
                x = x_orig + length
                for i in range(length+1):
                    if rows == 1:
                        addtodict(grid,x_orig+i,y_orig)
                    else:
                        searchindict(grid,intersection,x_orig+i,y_orig)
            elif dir == 'L':
                x = x_orig - length
                for i in range(length+1):
                    if rows == 1:
                        addtodict(grid,x_orig-i,y_orig)
                    else:
                        searchindict(grid,intersection,x_orig-i,y_orig)
intersection.sort()
print(intersection[1])