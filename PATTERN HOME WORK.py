#PATTERN - 1
for i in range(5, 0, -1):
    for space in range(5 - i):
        print(" ", end="") 
    for star in range(i):
        print("*", end=" ")
    print()


#PATTERN-2  
for i in range(1, 5 + 1):
    for space in range(5 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end=" ")
    print() 



#PATTERN-3  
# UPPER TRIANGLE
for i in range(5, 0, -1):
    for space in range(5 - i):
        print(" ", end="") 
    for star in range(i):
        print("*", end=" ")
    print()
# BELOW TRIANGLE
for i in range(2, 5 + 1):
    for space in range(5 - i):
        print(" ", end="")  
    for star in range(i):
        print("*", end=" ")
    print()  


#PATTERN-4
for i in range(1,5+1):
    print("*"*i,end=" ")
    print(" "*(2*(5-i)),end="")
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i,end=" ")
    print(" "*(2*(5-i)),end=" ")
    print("*"*i)  

#PATTERN-5    
    for i in range(5):
        for j in range(i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
zero_one_triangle(5)   

#PATTERN-6

def floyds_triangle(5):
    number = 1
    for i in range(1, 5 + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()
floyds_triangle(5)

#PATTERN-7

n = 4
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

#PATTERN-8   

H="ABCDE"
for i in range(1,len(H)+1):
    print(H[:i]) 
