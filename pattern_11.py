# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


def pattern(size):
    for i in range(size):
        start = 1 if i%2 == 0 else 0
        for j in range(i+1):
            print(start, end = " ")
            start = 1 - start
        print()    
pattern(5)            
