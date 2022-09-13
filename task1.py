class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


    def __str__(self):
        return f'You can call me as {self.first_name} {self.last_name} and my age is  {self.age}'

class Student(Person):
    def __init__(self, name, surname,age):
        super().__init__(name, surname,age)

    def __str__(self):
        return f"\n\tName/Surname: {self.name} {self.surname}\n" \
               f"\tAge: {self.age}\n"


class Teacher(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

student = Student('John', 'Smith', 13)
teacher = Teacher('Michael', 'Jackson', 'He is not teaching anymore', 20000)

print(Person)