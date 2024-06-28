# fib(n) = fib(n - 1) + fib(n - 2)
# fib(0) = 0
# fib(1) = 1

def fib_slow(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_slow(n - 1) + fib_slow(n - 2)


def fib(n, result={0: 0, 1: 1}):
    if n not in result:
        result[n] = fib(n - 1) + fib(n - 2)
    return result[n]


# Vyskusajte, aky pomaly je fib_slow(n)
for i in range(1000):
    print(f'fib({i}) = {fib(i)}')
