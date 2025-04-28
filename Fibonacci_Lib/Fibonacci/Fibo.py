def fibonacci_series(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series