def logistic_map(r, x):
    '''
    quadratic recurrence equation

    :param r: positive constant that: r != 0, r != 1, r <= 4
    :param x: x value
    :return:
    '''
    return r * x * (1 - x)