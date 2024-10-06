def recursive_fibonacci(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)