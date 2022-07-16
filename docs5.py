# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : 
# Expected Result : [2, 4, 6, 8].

def even(num):
    i=0
    b=[]
    while i<len(num):
        if num[i]%2==0:
            b.append(num[i])
        else:
            pass
        i+=1
    print(b)
even([1, 2, 3, 4, 5, 6, 7, 8, 9])