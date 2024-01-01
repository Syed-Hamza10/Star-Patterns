# *
# **
# ***
# ****
# *****


#way 1
def pattern(size):
    for i in range(size):
        print('* ' * (i+1))

pattern(5) 

def way2(size):
    for i in range(size):
        for j in range(i+1):
            print('*', end=' ')
        print()    
way2(5)