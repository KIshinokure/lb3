#Класс «Студент» с методом вывода информации.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Студент: {self.name}, Возраст: {self.age}, Оценка: {self.grade}")


student1 = Student("Иван", 20, 4.5)
student2 = Student("Мария", 19, 4.8)

student1.display_info()
student2.display_info()