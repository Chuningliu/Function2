# Q17. Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )


def voter(num):
    if num>=18:
        print("Eligible to vote")
    else:
        print("Not eligible")
voter(16)