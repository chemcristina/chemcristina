# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

# The abs() method returns the absolute value of a number (the number's distance from zero)

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

userinput = input('Enter a number: ')
n = float(userinput)

def diff21(n):
    if n >= 0:
        return n
    elif n < 0:
        return abs(n)

print(diff21(n))
