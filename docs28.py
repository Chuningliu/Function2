# Q27. Write a function for checking the speed of drivers.
# This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70),
# it should give the driver one demerit point and 
# print the total number of demerit points. For example, 
# if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, 
# the function should print: “License suspended”

def function(speed):
    if speed<70:  
        print("ok")
    elif speed>70:
        i=71
        b=0
        while i<=speed:
            if i%5==0:
                b+=1
            i+=1
        print(b)
        if b>12:
            print("License suspended")
        else:
            pass
speed=int(input("Enter the number:"))
function(speed)