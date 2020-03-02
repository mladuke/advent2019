def addtodict(dict,x,y,counter):
    coor = (str(x)+','+str(y))
    dict.update({coor:counter})

def searchindict(dict,list,x,y,counter):
        coord = (str(x)+','+str(y))
        if coord in grid.keys():
            #print(counter,dict[coord], counter+dict[coord])
            list.append(dict[coord] + counter)

import csv

with open('day3_input.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    grid={}
    intersection =[]
    rows = 0
    counter_1 = 0
    counter_2 = 0
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
                for i in range(1,length+1):
                    if rows ==1:
                        counter_1 += 1
                        addtodict(grid,x_orig,y_orig+i, counter_1)
                    else:
                        counter_2 += 1
                        searchindict(grid,intersection,x_orig,y_orig+i, counter_2)
            elif dir =='D':
                y = y_orig - length
                for i in range(1,length+1):
                    if rows == 1:
                        counter_1 += 1                        
                        addtodict(grid,x_orig,y_orig-i, counter_1)
                    else:
                        counter_2 += 1
                        searchindict(grid,intersection,x_orig,y_orig-i,counter_2)
            elif dir == 'R':
                x = x_orig + length
                for i in range(1,length+1):
                    if rows == 1:
                        counter_1 += 1                        
                        addtodict(grid,x_orig+i,y_orig, counter_1)
                    else:
                        counter_2 += 1
                        searchindict(grid,intersection,x_orig+i,y_orig, counter_2)
            elif dir == 'L':
                x = x_orig - length
                for i in range(1,length+1):
                    if rows == 1:
                        counter_1 += 1                        
                        addtodict(grid,x_orig-i,y_orig, counter_1)
                    else:
                        counter_2 += 1
                        searchindict(grid,intersection,x_orig-i,y_orig, counter_2)
intersection.sort()
print(intersection[0])