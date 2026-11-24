
# =====================================================
# PROJECT: PYTHON OBJECT-ORIENTED PROGRAMMING (OOP)
# AUTHOR: Dheeraj Sharma
# DESCRIPTION: Complete Python OOP Learning Project
# =====================================================


# 1. CLASS AND OBJECT

class Student:

    def show_details(self):
        print("Name: Dheeraj")
        print("Course: B.Tech CSE")
        print("College: IET Sitapur")


student1 = Student()
student1.show_details()


# 2. CONSTRUCTOR AND INSTANCE METHODS

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


emp1 = Employee("Dheeraj", 25000)
emp1.display_details()


# 3. CLASS METHOD AND STATIC METHOD

class Calculator:

    company = "ABC Company"

    @classmethod
    def show_company(cls):
        print("Company:", cls.company)

    @staticmethod
    def add(a, b):
        return a + b


Calculator.show_company()
print("Addition:", Calculator.add(10, 20))


# =====================================================
# 4. FOUR PILLARS OF OOP
# =====================================================


# 4.1 ENCAPSULATION
# Encapsulation protects data inside a class.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Money withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def show_balance(self):
        print("Current Balance:", self.__balance)


account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
account.show_balance()


# 4.2 INHERITANCE
# Child class can access parent class methods.

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()
dog.eat()
dog.bark()


# 4.3 POLYMORPHISM
# Same method name with different behaviours.

class Cat:

    def sound(self):
        print("Cat says Meow")


class Cow:

    def sound(self):
        print("Cow says Moo")


class Bird:

    def sound(self):
        print("Bird says Chirp")


animals = [Cat(), Cow(), Bird()]

for animal in animals:
    animal.sound()


# 4.4 ABSTRACTION
# Hides implementation details from the user.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car engine started")


class Bike(Vehicle):

    def start(self):
        print("Bike engine started")


car = Car()
bike = Bike()

car.start()
bike.start()


# =====================================================
# 5. CLEAN CODE PRINCIPLES
# =====================================================

# 1. Use meaningful variable names.
# 2. Avoid duplicate code (DRY).
# 3. Keep code simple (KISS).
# 4. Use proper indentation.
# 5. Create reusable functions.
# 6. Handle errors properly.
# 7. Write comments where needed.


def calculate_total(price, quantity):
    total = price * quantity
    return total


total_amount = calculate_total(500, 3)
print("Total Amount:", total_amount)


# =====================================================
# 6. PRACTICAL PROJECT
# STUDENT MANAGEMENT SYSTEM
# =====================================================

class StudentRecord:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.__marks = marks

    def display_details(self):
        print("\nStudent Information")
        print("-------------------")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.__marks)

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks. Enter marks between 0 and 100.")

    def get_result(self):
        if self.__marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


class CollegeStudent(StudentRecord):

    def course_details(self):
        print("Course: B.Tech CSE")
        print("College: IET Sitapur")


student = CollegeStudent("Dheeraj", 101, 85)

student.display_details()
student.course_details()
student.get_result()

student.update_marks(95)
student.display_details()


# =====================================================
# 7. EXCEPTION HANDLING WITH OOP
# =====================================================

class Division:

    def divide(self, a, b):
        try:
            result = a / b
            print("Division Result:", result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

        except TypeError:
            print("Error: Please enter valid numbers")

        finally:
            print("Division operation completed")


division = Division()
division.divide(20, 5)
division.divide(20, 0)


# =====================================================
# END OF PYTHON OOP PROJECT
# =====================================================

print("\nThank you for exploring Python OOP!")
