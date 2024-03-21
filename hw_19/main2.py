def is_subset(a, b):
    for i in a:
        if i not in b:
            return False
    return True

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(is_subset(a, b))