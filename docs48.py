# Q48. Two numbers are entered through the keyboard. Write a flowchart
#  -pto find the value of the   
# first number raised to the power of another.
# Sample Input
# 3
# 4
# Sample Output
# 81 (3x3x3x3)


def my_function():
    n=int(input("enter the number"))
    num=int(input("enter the number"))
    i=1
    c=1
    while i<=num:
        a=n
        c=c*a
        i=i+1
    print(c)
my_function()