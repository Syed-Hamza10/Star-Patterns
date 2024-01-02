# *****
# ****
# ***
# **
# *

def pattern(size):
    for i in range(size,0,-1):
        for j in range(i):
            print('*', end = " ")
        print()           
pattern(5)        