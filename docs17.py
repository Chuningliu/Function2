# Q16.Print multiplication table of 12 using function.

def table(n):
    for i in range (1, 11):
        print(n,"*",i,"=",n*i)
n = 12
table(n)
