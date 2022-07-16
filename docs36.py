# Q36. I would like to be able to pass an array with two
# elements to my swapValues function to swap the values. 
# However it appears that the values aren't changing.
# Can you figure out what's wrong here?



def swap_values(args):
    temp = args
    args[0] = args[1]
    args[1] = temp
    return args
args=int(input("Enter"))

print(swap_values(args))


