import math
# yes yes yes i know these functions have probably been implemented in some
# python library in C by some pro 10x more experienced than me but lemme have some fun


def gcf(a, b):
    """Implements the Euclidean Algorithm to find the greatest
    common divisor of two numbers

    Parameters:
        a: natural number
        b: natural number

    Returns a natural number, the GCD of a and b
    """
    if a % b == 0:
        return b
    return gcf(b, a % b)


# Precondition: b1, b2, and b3 are all relatively prime to each other
# resArray and baseArray have same num of elements
def chinese_rem_thrm(res_array, base_array):
    """Implements the Chinese Remainder Theorem on a list of
    residues and a list of modular bases, returns the least residue

    Parameters:
        res_array: list of natural numbers
        base_array: list of natural numbers

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
    Finds the modular inverse of a mod b. If a and b aren't relatively prime,
    throws a ValueError

    Parameters:
        a: natural number, number we want to find the modular inverse of
        b: natural number, value of the modular base

    Returns a^-1 (mod b), a natural number
    """
    if gcf(a, b) == 1:
        x, __ = ext_euc_alg(a, b)
        return x % b  # makes sure its positive
    else:
        raise ValueError("Numbers are not relatively prime for modular inverse")


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
