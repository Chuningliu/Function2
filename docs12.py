# Q13.Write a function to check if a number is even or not.
def function(n):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
n=int(input("Enter the number:"))
function(n)