import csv

with open('day2_input.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pc = 0
    sum = 0
    prod = 0
    for row in csv_reader:
        row[1]=12
        row[2]=2
        while (row[pc] != '99'):
            print(pc,row[pc],row[pc+1],row[pc+2],row[pc+3])
            op1 = int(row[int(row[pc+1])])
            op2 = int(row[int(row[pc+2])])
            if row[pc]=='1':
                sum = op1 + op2
                row[int(row[pc+3])] = sum
                print ('sum',op1,op2,sum, row[pc+3] )
            elif row[pc]=='2':
                prod = op1*op2
                row[int(row[pc+3])] = prod
                print ('prod',op1,op2,prod, row[pc+3] )
            pc += 4
        print("The Answer is",row[0])