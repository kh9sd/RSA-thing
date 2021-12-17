import math


def gcf(a, b):
    if (a % b == 0):
        return b
    return gcf(b, a % b)


# Precondition: b1, b2, and b3 are all relatively prime to each other
# resArray and baseArray have same num of elements
def chineseRemThrm(resArray, baseArray):
    total = 0

    bProduct = 1
    for x in baseArray:
        bProduct *= x

    for i in range(len(resArray)):
        otherBP = bProduct // baseArray[i]
        modInv = modularInv(otherBP, baseArray[i])
        print("{}*{}*{}".format(resArray[i], otherBP, modInv))
        total += resArray[i] * otherBP * modInv

    print("Final output is " + str(total))


# Precondition: a and b are relatively prime
# finds a^-1 congruent to 1 mod b
def modularInv(a, b):
    x, __ = ExtEucAlg(a, b)
    return x


def ExtEucAlg(a, b):
    # if the two numbers are the same, otherwise the thing breaks
    if (a == b):
        return (1, 0)
    # we want a to be greater than b
    if (a < b):
        x, y = ExtEucAlg(b, a)
        return y, x

    # form is am + bn = a%b
    m = 1
    n = -1 * ((a - a % b) // b)

    # base case
    if (b % (a % b) == 0):
        return m, n
    else:
        x, y = ExtEucAlg(b, a % b)  # recursion on equation bm + a%bn = ~~~
        return (m * y), (n * y + x)  # this basically just does substitution


a = 17
b = 23
x, y = modularInv(a, b)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

resArray = [3, 4, 78]
baseArray = [41, 5, 79]

chineseRemThrm(resArray, baseArray)
# print("modular inverse of {} base {} is {}".format(a,b,test))
# print("{} times {} plus {} times {} equals {}".format(a, x, b, y, gcf(a,b)))

