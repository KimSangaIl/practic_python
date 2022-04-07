instr = ''

if __name__ == "__main__" :
    instr = input("input string : ")
    for i in range (len(instr) - 1, -1, -1) :
        print(instr[i], end = '')
