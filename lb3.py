#Класс со статическим методом.
# class Calculator:
#     def add():
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         return a + b
#
# print(Calculator.add())

#Класс-счётчик (увеличение/уменьшение)

# class Counter:
#     count = 0
#
#     def increment():
#         Counter.count += 1
#
#     def decrement():
#         Counter.count -= 1
#
#     def get_count():
#         return Counter.count
#
#
# Counter.increment()
# Counter.increment()
# print(Counter.get_count())
#
# Counter.decrement()
# print(Counter.get_count())

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