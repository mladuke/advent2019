import csv

# Opcodes
ADD = 1
MULT = 2
HALT = 99

# Target Answer
ANS = 19690720

noun = 0
verb = 0

with open('day2_input.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for ROM in csv_reader:
        ROM = list(map(int, ROM))

        for i in range(100):
            for j in range(100):
                RAM = ROM.copy()
                ip = 0
                sum = 0
                prod = 0
                RAM[1] = i
                RAM[2] = j
                while (RAM[ip] != HALT):
                    # print(ip, RAM[ip], RAM[ip+1], RAM[ip+2], RAM[ip+3])
                    opcode = RAM[ip]
                    op1 = (RAM[(RAM[ip+1])])
                    op2 = (RAM[(RAM[ip+2])])
                    result_p = RAM[ip+3]
                    if opcode == ADD:
                        sum = op1 + op2
                        RAM[result_p] = sum
                        # print('sum', op1, op2, sum)
                    elif opcode == MULT:
                        prod = op1*op2
                        RAM[result_p] = prod
                        # print('prod', op1, op2, prod)
                    ip += 4
                # print(i, j, "The Answer is", RAM[0])
                if RAM[0] == ANS:
                    noun = i
                    verb = j
    print("Noun",noun, "Verb",verb, "Answer", 100*noun + verb)