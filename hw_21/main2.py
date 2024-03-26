from collections import namedtuple

def information(*arg):

    Person = namedtuple('Person', ['name', 'age', 'city'])
    person = Person(arg[0], arg[1], arg[2])
    return person

invite = int(input('how many people are you inviting? '))
my_persons = []
for i in range(1, invite+1):
    user_input = input(f'Enter your name age and city separated by a space fo the person number {i}: ')
    my_persons.append(information(*user_input.split()))

for person in my_persons:
    print(f'Name: {person.name}, Age: {person.age}, City {person.city}')