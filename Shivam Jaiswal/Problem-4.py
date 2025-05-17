def count_multiples(lst):
    result = {}
    for i in range(1, 10):
        result[i] = sum(1 for num in lst if num % i == 0)
    return result


nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(nums))

# Output:
# {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
