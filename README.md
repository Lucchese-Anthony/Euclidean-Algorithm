# Euclidean Algorithm

euclidAlgo.py was made in tandem with my Chaos and Fractals course, MATH320, where we were to solve greatest common demoninator (GCD) using the [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)

This system has 3 states:

                |   Euc(m,n)        if n < m
    Euc(n,m) if |   (n,0)           if m == 0
                |   (m,n % m)       if n[0] = 'b'


So as an example we will assume the formula Euc(520221547, 498672943)

[520221547, 498672943, 21548604, 3055051, 163247, 116605, 46642, 23321, 0]

    520221547 % 498672943 = 21548604
    498672943 % 21548604 = 3055051
    21548604 % 3055051 = 163247
    3055051 % 163247 = 116605
    163247 % 116605 = 46642
    116605 % 46642 = 23321
    46642 % 23321 = 0

meaning 23321 is the GCD / Greatest Common Denominator

uses:

`python3 euclidAlgo.py (arg1) (arg2)`
or
`python3 euclidAlgo.py`
