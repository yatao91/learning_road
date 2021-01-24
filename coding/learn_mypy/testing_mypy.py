# -*- coding: utf-8 -*-
from typing import List


class Person():
    def __init__(self, surname, firstname, age, job):
        self.surname = surname
        self.firstname = firstname
        self.age = age
        self.job = job


# def display_doctors(persons: List[Person]) -> None:
#     for person in persons:
#         if person.job.lower()in['gp', 'dentist', 'cardiologist']:
#             print(f'{person.surname} {person.name}')
def display_doctors(persons: List[Person]) -> None:
    for person in persons:
        if person.job.lower()in['gp', 'dentist', 'cardiologist']:
            print(f'{person.surname} {person.firstname}')


mike = Person('Davis', 'Mike', '45', 'dentist')
john = Person('Roberts', 'John', 21, 'teacher')
lee = Person('Willams', 'Lee', 'gp', 56)

# display_doctors(mike)
# display_doctors([mike, john, 'lee'])
display_doctors([mike])
display_doctors([mike, john, lee])
