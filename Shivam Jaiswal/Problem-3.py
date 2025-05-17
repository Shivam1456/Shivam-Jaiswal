def odd_series_limited(a):
    series = []
    i = 1
    while len(series) < a:
        series.append(i)
        i += 2
        if len(series) == a or i > a * 2:  
            break
    return series[:a if a % 2 == 1 else a - 1]


print(odd_series_limited(4))  # Output: [1, 3, 5]