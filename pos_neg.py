# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def pos_neg(a, b, negative):
    if a or b < 0:
        return True
    elif a and b < 0:
        return True

print(pos_neg(1, -1, False))
print(pos_neg(-1, -1, False))
print(pos_neg(-4, -5, True))

#I wrote the following code after writing the above code. This is simplified.
def pos_neg(a, b, negative):
    return (a or b <0) and (a and b < 0)
print(pos_neg(1, -1, False))
print(pos_neg(-1, -1, False))
print(pos_neg(-4, -5, True))

#why is the 3rd parameter from above function necessary? I removed it and get the same results.
def pos_neg(a, b):
    return (a or b <0) and (a and b < 0)
print(pos_neg(1, -1))
print(pos_neg(-1, -1))
print(pos_neg(-4, -5))
