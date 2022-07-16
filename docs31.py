# Q30. Write a function that prints all the prime numbers between 0 
# and limit where limit is a parameter.


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