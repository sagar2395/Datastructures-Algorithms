def factorial_recursive(num):
    if num <= 1:
        return 1
    else:
        return  num * factorial_recursive(num - 1)
    
    
def factorial_iterative(num):
    f = 1
    for i in range(1, num+1):
        f = f * i
    return f