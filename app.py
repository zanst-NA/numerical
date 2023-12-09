def equation(x):
    return x ** 2 - 4


def bisection_method(a, b, tol=1e-6, max_iter=10):
    iterations = []

    for i in range(max_iter):
        c = (a + b) / 2
        fa = equation(a)
        fb = equation(b)
        fc = equation(c)
        error = b - a

        iterations.append([i + 1, a, b, c, fa, fb, fc, error, fa * fc, fb * fc])

        if fc == 0 or error < tol:
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c

    return iterations


# Initial interval
a = 1
b = 3

# Run bisection method
results = bisection_method(a, b)

# Display the results table
print("| Iteration |  a    |  b    |  c    |  f(a)  |  f(b)  |  f(c)  | b-a  | f(a)*f(c) | f(b)*f(c) |")
print("|-----------|-------|-------|-------|--------|--------|--------|------|-----------|-----------|")
for row in results:
    print(
        f"|{row[0]:^11}|{row[1]:^7.4f}|{row[2]:^7.4f}|{row[3]:^7.4f}|{row[4]:^8.4f}|{row[5]:^8.4f}|{row[6]:^8.4f}|{row[7]:^6.4f}|{row[8]:^11.4f}|{row[9]:^11.4f}|")
