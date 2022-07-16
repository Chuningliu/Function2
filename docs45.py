# Q45. Draw a flowchart to Take 10 numbers as input and 
# create a list of the numbers from the user and update each element 
# of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
# 	23
# 	42 
# 	41 
# 	1
# Sample Output:
# 	-23 
# 	4200 
# 	-41 
# 	-1

def even_odd():
    a=[]
    i=1
    while i<=10:
        num=int(input("enter number"))
        a.append(num)
        i=i+1
    print(a)
    j=0
    while j<len(a):
        if a[j]%2==0:
            print(a[j]*100)
        elif a[j]%2!=0:
            print(a[j]*-1)
        j=j+1
    # else:
    #     print("ntg")
even_odd()
    
    
    
