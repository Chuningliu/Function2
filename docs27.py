# Q26. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def number(n):
    
    if n%3==0:
        if n%5==0:
            if n%3==0 and n%5==0:
                return "FizzBuzz"
            else:
                return "Buzz"
        else: 
            return "Fizz"
    else:
        return n
n=int(input("Enter the number:"))
print(number(n))


# def solve(n):
#    s = 0
#    while(n > 0 or s > 9):
#       if n == 0:
#          n = s
#          s = 0

#       s += n % 10
#       n //= 10

#    return s

# n = 513682
# print(solve(n))