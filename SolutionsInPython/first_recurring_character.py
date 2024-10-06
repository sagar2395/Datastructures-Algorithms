def simple_frc(array):
    dict = {}
    
    for item in array:
        if item in dict:
            return item
        else:
            dict[item] = True
    return None
