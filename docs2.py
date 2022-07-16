# Q2.Write a Python function to find the Max of three numbers.

def max(num1,num2,num3):
    if num1>num2 and num1> num3:
        print(num1,"is the greatest")
    elif num2>num3 and num2>num1:
        print(num2,"is the greatest")
    else:
        print(num3,"is the greatest")
max(23,45,67)