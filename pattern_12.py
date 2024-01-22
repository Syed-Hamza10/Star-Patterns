# 1             1
# 1 2         2 1
# 1 2 3     3 2 1 
# 1 2 3 4 4 3 2 1


def pattern(size):
    space = 2 * (size-1)
    for i in range(1, size+1):

        #numbers
        for j in range(1, i+1):
            print(j, end = " ")
        

        #space
        for j in range(space):
            print(' ', end = " ")

        #numbers
        for j in range(i,0,-1):
            print(j, end = " ")
        space -= 2    
        print()    
pattern(4)            