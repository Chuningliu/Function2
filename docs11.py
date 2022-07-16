# Q12.Numbers ending with zeros are boring.
# # They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def zero(n):
    i=0
    while i<1:
        if n%10==0:
            a=n//10
            i+=1
        print(a)
n=int(input("Enter the number:"))
zero(n)



