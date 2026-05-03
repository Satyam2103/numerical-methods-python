def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol):
    while True:
        x1 = x0 - f(x0)/df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1

    print("Root:", x1)

newton_raphson(1.5, 0.001)
