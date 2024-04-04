class Student(object):

    def __init__(self, name, afe):
        self.name = name
        self.afe = afe

    def __str__(self):
        return f"Student name: {self.name}, afe: {self.afe}"

    def __repr__(self):
        return f"Student name: {self.name} afe: {self.afe}"


s = Student("Kolya", 33)
print(s)
# Без display_info(). но думаю и так пойдлет )