from collections import namedtuple
def student(students, midl_bal):
    my_list = []
    for student in students:
        if student[-1] >= midl_bal:
            my_list.append(student[0])
        else:
            continue
    return my_list
a = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
b = 90
print(student(a, b))

