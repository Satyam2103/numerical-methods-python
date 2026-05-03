def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return

    c = a
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print("Root:", c)

regula_falsi(1, 2, 0.001)
