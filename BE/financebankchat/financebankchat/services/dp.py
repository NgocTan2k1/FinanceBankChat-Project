import numpy
import numbers
import random


def add_laplace_noise(x, sensitivity=1, epsilon=0.1):
    if x == 0: return x
    scale = sensitivity / epsilon
    noise = numpy.random.laplace(loc=0.0, scale=scale)
    return x + noise


def flip_coin():
    random_number = random.randint(0, 1)
    if random_number == 1:
        return True
    random_number = random.randint(0, 1)
    return random_number == 1


def filter_rows(data):
    return [row for row in data if flip_coin()]


def noise_rows(data):
    rows = []
    ban_list = ['id', 'stock_id', 'year', 'provider_id']
    for row in data:
        if not flip_coin():
            for property in row:
                if isinstance(row.get(property), numbers.Number) and property not in ban_list:
                    row[property] = add_laplace_noise(row.get(property))
        rows.append(row)
    return rows
