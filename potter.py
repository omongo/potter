def combine(books):
    lowest_groups = []
    groups_of_5 = []
    groups_of_3 = []

    while len(books) != 0:
        largest_unique = set(books)
        largest_unique_len = len(largest_unique) 

        if largest_unique_len == 5:
            groups_of_5.append(largest_unique)
        elif largest_unique_len == 3:
            groups_of_3.append(largest_unique)
        else:
            lowest_groups.append(largest_unique)

        for book in largest_unique:
            books.remove(book)

    return lowest_groups, groups_of_5, groups_of_3


def match(groups):
    lowest_groups, groups_of_5, groups_of_3 = groups
    common_length = min(len(groups_of_5), len(groups_of_3))

    for i in range(common_length):
        value = max(groups_of_5[i] - groups_of_3[i])
        groups_of_5[i].discard(value)
        groups_of_3[i].add(value)
        lowest_groups.append(groups_of_5[i])
        lowest_groups.append(groups_of_3[i])

    lowest_groups.extend(groups_of_5[common_length:])
    lowest_groups.extend(groups_of_3[common_length:])

    return lowest_groups


def price(books):
    result = 0
    price_per_unit = 8
    length_to_rate = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}

    groups = combine(books)
    lowest_groups = match(groups)

    for group in lowest_groups:
        result += price_per_unit * len(group) * length_to_rate[len(group)]

    return result


if __name__ == '__main__':
    assert 0 == price([])
    assert 8 == price([0])
    assert 8 == price([1])
    assert 8 == price([2])
    assert 8 == price([3])
    assert 8 == price([4])
    assert 8 * 2 == price([0, 0])
    assert 8 * 3 == price([1, 1, 1])
    assert 8 * 2 * 0.95 == price([0, 1])
    assert 8 * 3 * 0.9 == price([0, 2, 4])
    assert 8 * 4 * 0.8 == price([0, 1, 2, 4])
    assert 8 * 5 * 0.75 == price([0, 1, 2, 3, 4])
    assert 8 + (8 * 2 * 0.95) == price([0, 0, 1])
    assert 2 * (8 * 2 * 0.95) == price([0, 0, 1, 1])
    assert (8 * 4 * 0.8) + (8 * 2 * 0.95) == price([0, 0, 1, 2, 2, 3])
    assert 8 + (8 * 5 * 0.75) == price([0, 1, 1, 2, 3, 4])
    assert 2 * (8 * 4 * 0.8) == price([0, 0, 1, 1, 2, 2, 3, 4])
    assert 3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8) == price([0, 0, 0, 0, 0,
                                                            1, 1, 1, 1, 1,
                                                            2, 2, 2, 2,
                                                            3, 3, 3, 3, 3,
                                                            4, 4, 4, 4])
