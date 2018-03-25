def x_pow(x):
    def pow(n):
        print(x ** n)
    return pow


def fibonacci(nth):
    # 1,1,2,3,5,8,13,21,34,55
    if nth == 1 or nth == 2:
        return 1
    else:
        return fibonacci(nth - 1) + fibonacci(nth - 2)