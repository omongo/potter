def price(books):
    result = 0
    price_per_unit = 8
    len_to_rate = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
    groups = combine(books)
    cheapest_sets = combine_cheapest(groups)

    for cheapest_set in cheapest_sets:
        cheapest_set_len = len(cheapest_set)
        result += price_per_unit * cheapest_set_len * \
            len_to_rate[cheapest_set_len]

    return result


def combine(books):
    groups = [], [], []

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

    return groups


def combine_cheapest(groups):
    sets_of_5, sets_of_3, cheapest_sets = groups
    len_min = min(len(sets_of_5), len(sets_of_3))

    for i in range(len_min):
        value = max(sets_of_5[i] - sets_of_3[i])
        sets_of_5[i].discard(value)
        sets_of_3[i].add(value)
        cheapest_sets.append(sets_of_5[i])
        cheapest_sets.append(sets_of_3[i])

    cheapest_sets.extend(sets_of_5[len_min:])
    cheapest_sets.extend(sets_of_3[len_min:])

    return cheapest_sets
