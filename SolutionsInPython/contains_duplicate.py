def contains_duplicate(arr):
    if len(set(arr)) != len(arr):
        return True
    return False

arr = [1, 3, 5, 7, 8, 9]

print(contains_duplicate(arr))
    