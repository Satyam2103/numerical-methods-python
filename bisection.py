def f(x):
    return x**3 - x - 2

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return

    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print("Root:", c)

bisection(1, 2, 0.001)
