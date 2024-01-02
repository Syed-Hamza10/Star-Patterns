# 1
# 22
# 333
# 4444
# 55555

def pattern(size):
    for i in range(size):
        for j in range(i+1):
            print(i+1, end = " ")
        print()    

pattern(5)            