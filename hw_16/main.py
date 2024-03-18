def calculate(matrix):
    result = 0
    for i in matrix:
        result += sum(i)
    return result


a = [[1, 2, 3],
     [4 ,5, 6],
     [7, 8, 9]]
print(calculate(a))