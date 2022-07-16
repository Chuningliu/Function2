# Q5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : 

def duplicate(num):
    i=0
    b=[]
    while i<len(num):
        if num[i] not in b:
            b.append(num[i])
        i+=1
    print(b)
duplicate([1,2,3,3,3,3,4,5])
