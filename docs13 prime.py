# Q14.Write a function to check if a number is prime or not.
def prime(a): 
    count=0
    for i in range(2,a//2+1):
        count+=1
        break
    if count==0 and a!=1:
        print(a,"is a prime number")
    else:
        print(a, "is not a prime number")
prime(3)
