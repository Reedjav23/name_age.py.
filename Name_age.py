from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = date.today().year
birth_year = current_year - age

print(f"{name}, you were born in {birth_year}.")
