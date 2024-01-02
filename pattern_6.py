# 12345
# 1234
# 123
# 12
# 1

def pattern(size):
    for i in range(size):
        for j in range(1,size - i+1):
            print(j, end = " ")
        print()    
pattern(5)         