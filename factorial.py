"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal

def factorial_recursive(n):
    # n * (n-1) * (n-2) * ... until n = 0
    if n == 0:
        return 1

    else:
        recursion = factorial_recursive(n-1)
        product = recursion * n
        return product    



def test_factorial():
    assert_equal(factorial_recursive(0), 1)
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(2), 2)
    assert_equal(factorial_recursive(3), 6)
    


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
