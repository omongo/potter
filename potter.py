def price(books):
    """ Calulate the lowest price of books. 
    >>> price([])
    0
    >>> price([0])
    8
    >>> price([1])
    8
    >>> price([2])
    8
    >>> price([3])
    8
    >>> price([4])
    8
    >>> price([0, 0])
    16
    >>> price([1, 1, 1])
    24
    >>> price([0, 1])
    15.2
    >>> price([0, 2, 4])
    21.6
    >>> price([0, 1, 2, 4])
    25.6
    >>> price([0, 1, 2, 3, 4])
    30.0
    >>> price([0, 0, 1])
    23.2
    >>> price([0, 0, 1, 1])
    30.4
    >>> price([0, 0, 1, 2, 2, 3])
    40.8
    >>> price([0, 1, 1, 2, 3, 4])
    38.0
    >>> price([0, 0, 1, 1, 2, 2, 3, 4])
    51.2
    >>> price([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4])
    141.2
    """
    result = 0
    price_per_unit = 8
    len_to_rate = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
    cheapest_sets = combine(books)

    for cheapest_set in cheapest_sets:
        cheapest_set_len = len(cheapest_set)
        result += price_per_unit * cheapest_set_len * len_to_rate[cheapest_set_len]

    return result


def combine(books):
    groups = ([], [], [])

    while len(books) != 0:
        largest_set = set(books)
        largest_set_len = len(largest_set)

        if largest_set_len == 5:
            groups[0].append(largest_set)
        elif largest_set_len == 3:
            groups[1].append(largest_set)
        else:
            groups[2].append(largest_set)

        for book in largest_set:
            books.remove(book)

    return match(groups)


def match(groups):
    sets_of_5, sets_of_3, cheapest_sets = groups
    min_len = min(len(sets_of_5), len(sets_of_3))

    for i in range(min_len):
        value = max(sets_of_5[i] - sets_of_3[i])
        sets_of_5[i].discard(value)
        sets_of_3[i].add(value)
        cheapest_sets.append(sets_of_5[i])
        cheapest_sets.append(sets_of_3[i])

    cheapest_sets.extend(sets_of_5[min_len:])
    cheapest_sets.extend(sets_of_3[min_len:])

    return cheapest_sets


if __name__ == '__main__':
    import doctest
    doctest.testmod()
