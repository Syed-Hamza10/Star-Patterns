#    *
#   ***    
#  *****
# *******
# *******
#  *****
#   ***
#    *

#Combine pattern 8 and 7.

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
    for i in range(size):
        #spaces
        for j in range(1):
            print(" " * (i), end = "")
        #stars    
        for k in range(1):
            print('*' * ((2*size) - (2 * i + 1)), end = "")    
        #spaces
        for l in range(1):
            print(" " * (i), end = "")  
        print()    

pattern(5)        