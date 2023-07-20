def rosenbrock(x: list[float]):
    d = len(x)
    sum = 0
    for i, xi in enumerate(x[:d-1]):
        first_term = 100 * (x[i+1] - (xi*xi))*(x[i+1] - (xi*xi))
        second_term = (xi - 1)*(xi - 1)
        sum += first_term + second_term

    return sum