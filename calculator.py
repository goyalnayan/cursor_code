def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Both arguments must be integers')
    return a + b
