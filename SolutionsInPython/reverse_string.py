def reverse_string(str1):
    new_string = []
    for i in range(len(str1) - 1, -1, -1):
        new_string.append(str1[i])
    return ''.join(new_string)

print(reverse_string("hey My name is sagar chhabra"))