#    *
#   ***    
#  *****
# *******
#*********


def pattern(size):
    for i in range(size):
        #spaces
        for j in range(1):
            print(" " * (size - i - 1), end = "")
        #stars    
        for k in range(1):
            print('*' * (2*i+1), end = "")    
        #spaces
        for l in range(1):
            print(" " * (size - i - 1), end = "")  
        print()
pattern(6)   
    