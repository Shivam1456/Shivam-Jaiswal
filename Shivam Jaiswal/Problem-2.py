def odd_series_upto_a(a):
    series = [2 * i + 1 for i in range(a)]
    return series


print(odd_series_upto_a(4))  # Output: [1, 3, 5, 7]