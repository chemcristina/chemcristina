# Given two int values, return their sum.
# Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

# create error message for input that is not a number
ainput = input('Input a number: ')
binput = input('Input a number: ')

a = float(ainput)
b = float(binput)
sum = a + b

if a != b:
    print(sum)
elif a == b:
    print(sum * 2)
