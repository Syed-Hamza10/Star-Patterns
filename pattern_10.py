# *                     i= 1
# **                    i = 2
# ***                      3
# ****                      4
# *****                     5
# ****              2*size - i 
# ***
# **
# *


def pattern(size):
    for i in range(2*size):
        if i > size:
            print('*' * (2*size-i))
        else:
            print('*' * i)

pattern(5)            