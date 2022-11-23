import Lab2


def test_find_min_max():
    entered = [3, 4, 10]
    result = Lab2.find_min_max(entered)

    assert (result == [3, 10])


def test_calc_average():
    entered = [1, 2]
    result = Lab2.calc_average(entered)

    assert (result == 1, 5)


def test_median_temperature():
    entered = [2, 4, 6]
    result = Lab2.calc_average(entered)

    assert (result == 4)

    entered = [4, 6]
    result = Lab2.calc_average(entered)

    assert (result == 5)
