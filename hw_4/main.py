A = False
B = True
C = True
D = False

formula1 = not((A or B) and (C or D))
formula2 = ((not A and not B) or (not C and not D))

ч
if formula1 == formula2:
    print("Формулы эквивалентны.")
else:
    print("Формулы не эквивалентны.")
