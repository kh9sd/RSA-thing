import math
# yes yes yes i know these functions have probably been implemented in some
# python library in C by some pro 10x more experienced than me but lemme have some fun


def gcf(a, b):
    """
    Implements the Euclidean Algorithm to find the greatest
    common divisor of two numbers

    Parameters:
        a: natural number
        b: natural number

    Returns a natural number, the GCD of a and b
    """
    if a % b == 0:
        return b
    return gcf(b, a % b)


def chinese_rem_thrm(res_array, base_array):
    """
    Implements the Chinese Remainder Theorem on a list of
    residues and a list of modular bases, returns the least residue

    Assumes that all the numbers in the base_array are relatively prime
    to each other

    Parameters:
        res_array: list of natural numbers
        base_array: list of natural numbers

    Raises ValueError if inputted lists don't have same number of elements
    Returns a natural number
    """
    if len(res_array) != len(base_array):
        raise ValueError("Inputted lists are not the same length")

    total = 0
    base_product = math.prod(base_array)

    for res, base in zip(res_array, base_array):
        other_base_prod = base_product//base
        mod_inv = modular_inv(other_base_prod, base)
        total += res * other_base_prod * mod_inv

    return total % base_product


def modular_inv(a, b):
    """
    Finds the modular inverse of a mod b.

    Parameters:
        a: natural number, number we want to find the modular inverse of
        b: natural number, value of the modular base

    Raises ValueError if a and b aren't relatively prime
    Returns a^-1 (mod b), a natural number
    """
    if gcf(a, b) == 1:
        x, __ = ext_euc_alg(a, b)
        return x % b  # makes sure its positive
    else:
        raise ValueError("Numbers must be relatively prime for modular inverse")


def ext_euc_alg(a, b):
    """
    Implements Extended Euclidean Algorithm to get linear combination of
    a and b, such that am+bn = gcd(a,b)

    Parameters:
        a: natural number
        b: natural number

    Returns m,n tuple
    """
    # we want a to be greater than b
    if a < b:
        x, y = ext_euc_alg(b, a)
        return y, x

    # base case
    if a % b == 0:
        return 0, 1
    else:
        # form is am + bn = a%b
        m = 1
        n = -1 * ((a - a % b) // b)
        x, y = ext_euc_alg(b, a % b)  # recursion on equation bm + a%bn = ~~~
        return (m * y), (n * y + x)  # this basically just does substitution


def num_to_binary_list(x):
    """
    Produces a representation of a number in binary as a list

    Parameter:
        x: positive integer

    Raises a ValueError if x is non-positive
    Returns a list of 0's and 1's
    """
    if x <= 0:
        return ValueError("x must be positive")

    full = math.floor(math.log(x, 2))
    result = []

    for i in range(full, 0-1, -1):
        if x >= 2**i:
            x -= 2**i
            result.append(1)
        else:
            result.append(0)

    return result


def mod_expo(a, m, b):
    """
    Finds the value of a^m mod b with square-then-multiply algorithm

    Parameters:
        a: positive integer
            the base of the exponent
        m: positive integer
            the power of the exponent
        b: positive integer
            the modular base

    Raises a ValueError if any of the values are non-positive
    Returns a positive integer
    """
    if a <= 0 or m <= 0 or b <= 0:
        raise ValueError("All values must be positive")

    binary = num_to_binary_list(m)
    past = a
    result = 1
    # initialize a value for past
    if binary[-1] == 1:
        result = past

    for bit in binary[-2::-1]:  # loop through list in reverse, except the last element
        current = (past**2) % b
        if bit == 1:
            result = (current * result) % b
        past = current

    return result
