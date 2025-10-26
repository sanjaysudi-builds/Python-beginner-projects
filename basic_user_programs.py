# basic_user_programs.py
# Created by Sanju Sudi
# Collection of beginner Python programs

# 1️⃣ Full Name Program
first_name = input("First name: ")
middle_name = input("Middle name: ")
last_name = input("Last name: ")
print(f"{first_name} {middle_name} {last_name}")
print(first_name + " " + middle_name + " " + last_name + " .")



# 2️⃣ User Login Program
correct_username = "kiran"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print(" Login Successful!")
else:
    print(" Invalid credentials!")



# 3️⃣ Future Age Program
name = input("Enter your name: ")
age = int(input("Enter your current age: "))
future_year = int(input("Enter a future year: "))
future_age = age + (future_year - 2025)
print(f"{name}, you will be {future_age} years old in {future_year}.")
