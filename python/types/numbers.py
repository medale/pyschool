import math


def numbers():

    int1 = 12

    #      2147483647 Java int max value
    #      9223372036854775807 Java long max value
    # Look ma, no overflow
    int_bigger_than_long = 1234567891011121314151617

    float1 = 1.2
    little_float = 3.14e-2

    hexadecimal_literal = 0xc
    binary_literal = 0b1100

    # comparison operators: ==, !=, <, >, <=, >=
    if hexadecimal_literal == binary_literal:
        print("Int 12 is Hex {} is binary {}!".format(hex(12), bin(12)))

    star_pow_of_lf = little_float ** 0.5

    # built-in math functions like pow, abs, round etc.
    pow_pow_of_lf = pow(little_float, 0.5)

    # math module for even more math functions
    sqrt_of_lf = math.sqrt(little_float)

    float_div = 1 / 2

    int_div = 1 // 2

    remainder_of_int_div = 1 % 2

