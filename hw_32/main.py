class Counter:

    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return self.value + int(other)

    def __sub__(self, other):
        return self.value - int(other)

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)


counter = Counter()
counter += 7
counter -= 4
print(int(counter))

