def func_max(number, *elements, low=10, hi=100):

    mass = (number, ) + elements
    maximum = max(mass)

    if maximum > hi:
        return f"Так как {maximum} > {hi}, то ответ: {hi}"
    elif maximum < low:
        return f"Так как {maximum} < {low}, то ответ: {low}"
    else:
        return maximum
