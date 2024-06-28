# f(n) = 1 * 2 * 3 * ... * n
# f(n) = n * f(n - 1)
# f(0) = 1 (bazovy pripad)

# f(4) = 1 * 2 * 3 * 4
# f(5) = 1 * 2 * 3 * 4 * 5
# f(5) = f(4) * 5

# Nedava zmysel
# f(0) = f(-1) * 0
# f(-1) = f(-2) * -1
# ---

# f(0) = 1
# f(1) = f(0) * 1 = 1 * 1 = 1
# f(2) = f(1) * 2 = 2
# f(3) = f(2) * 3 = 6


# f(n) = n * f(n - 1)
# f(0) = 1
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_dyn(n, mezivysledky={0:1}):
    """Vypočítá faktoriál pomocí dynamického programování.

    Args:
        n: přirozené číslo, které je vstupem algoritmu.
        mezivysledky: slovník s mezivýsledky bude aktualizován při každém volání funkce.
    Returns:
        faktoriál čísla n.
    """
    if n in mezivysledky:
        return mezivysledky[n]
    else:
        mezivysledky[n] = n * factorial_dyn(n-1)
        return mezivysledky[n]


for i in range(10):
    print(factorial_dyn(i))
