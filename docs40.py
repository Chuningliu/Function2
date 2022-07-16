# Q40. Write a function For example, if we give 9119 
# the function should return  811181, as the  square of 9 is 81 
# and square of 1  is 1.

def square(a):
    b=str(a)
    i=0
    while i<len(b):
        print(int(b[i])**2,end="")
        i+=1
square(9119)