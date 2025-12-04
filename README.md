# Python Simulation Projects

A collection of Python simulation projects demonstrating various system implementations.

## Projects List

1. **ATM Simulator** (ATM_simulator.py) - ATM banking system simulation
2. **Grading System** (grading_system.py) - Student grading management system
3. **Hospital System** (hospital_system.py) - Hospital management simulation
4. **HR Management System** (HR_management_system.py) - Human resources management system for mainatain employees records
5. **MTB System** (MTB_system.py) - Movie Ticket booking system
6. **Music App** (music_app.py) - Music application/player simulation

 # 📌 HR Employee Management System — README
📖 Project Overview

The HR Employee Management System is a simple Python project demonstrating Object-Oriented Programming (OOP) concepts such as:

Classes

Inheritance

Polymorphism

Abstraction

The system manages multiple employee types:

Full-Time Employees

Part-Time Employees

Interns

Each employee type has a different salary calculation method, showcasing runtime polymorphism.

✨ Features

Add different types of employees (Full-Time, Part-Time, Intern)

Automatically calculate salary based on employee type

View employee details with salary

Calculate total monthly payroll

Clean, modular OOP design

🧠 OOP Concepts Used
1. Classes & Objects

Employees are created as objects from classes.

2. Inheritance

FullTime, PartTime, and Intern classes inherit from the Employee base class.

3. Polymorphism

Each employee type overrides calculate_salary() with its own logic.

4. Abstraction

Common employee structure is abstracted into the Employee class.

🧩 Code Explanation Summary
✔ Employee (Base Class)
Stores common attributes: ID, name, role
Has an abstract method calculate_salary()
(forces child classes to implement it)

✔ FullTime
Salary = base + benefits + performance bonus percentage

✔ PartTime
Salary = regular pay + overtime (1.5x after 40 hrs)

✔ Intern
Salary = stipend + bonus (if project completed)

✔ HRSystem
Stores a list of employees
Displays employees and salaries
Calculates total payroll

Screen Short of Output:-
![alt text](image-1.png)

# Movie Ticket Booking With Seat Reservation

Simple Python program to manage movie seat bookings (5 rows × 10 seats by default).
Features include seat reservation, front-row premium pricing, student discount, ticket printing, and saving bookings to a CSV file.

Project files

movie_booking.py — main program containing the Theater class and demo usage (provided).
bookings.csv — generated at runtime, stores saved bookings in CSV format (name,row,seat,price,student).

Features

2D seat map (rows × seats per row)
Book a seat and mark it as X in the seat map
Front row seats cost extra
Student discount (%) applied when booking
Print a simple ticket on the console when booking succeeds
Save each booking into bookings.csv

Example output screenshots:-
![alt text](image-3.png)
![alt text](image-4.png)

<h1>File Format</h1>
![alt text](image-5.png)

<h2>Code overview (brief)</h2>
class Theater
Constructor:
def __init__(self, rows=5, seats_per_row=10, base_price=200.0,
             front_row_extra=100.0, student_discount_pct=20.0,
             bookings_file="bookings.csv")
Builds self.seats: a 2D list of seat labels ("row-seat").
Creates bookings.csv with header if missing.

Key methods:
show_seats() — prints current seat map; booked seats display as X.
seat_is_available(row, seat) — returns True if seat is not "X".
calculate_price(row, is_student) — computes price: base_price + front_row_extra for row 1, minus student_discount_pct if student.
book_seat(name, row, seat, is_student=False) — validates input, calculates price, marks seat "X", appends booking to CSV, prints ticket, and returns booking dict or None on failure.
print_ticket(booking) — prints a small ticket to console.

demo()
Creates a Theater object, shows seats, books example seats, attempts a duplicate booking, and prints the final seat map.

# ATM_simulator
A simple and beginner-friendly ATM Simulator built using Python OOP concepts.
This project implements:
Encapsulation (private balance)
Error Handling
Custom messages for invalid withdrawals
Mini-statement tracking
Deposit / Withdraw / Balance check features

📌 Features
✔ Deposit Money
User can add money to the account.
Transaction is recorded in mini-statement.

✔ Withdraw Money
If withdrawal amount > balance → custom error message
Otherwise deduct money and record the transaction.

✔ Check Balance
Shows current account balance (balance stays private).

✔ Mini-Statement
Displays list of last transactions (Deposit/Withdraw + amount).

✔ Encapsulation
Balance is stored in a private variable __balance to prevent direct modification.

🧠 Concepts Used:-
🟦 OOP (Object-Oriented Programming)
Class: ATM
Encapsulation using private variable __balance
Methods for deposit, withdraw, balance check

🟧 Error Handling
Prevents withdrawing more money than available
Shows clear error messages

🟩 Data Structures
List used for mini-statement

📌 Example Output scrrenshot:-
![alt text](image-5.png)
![alt text](image-6.png)

 # 🎵 Music Player App (Python OOP Project)

A simple Music Player Application built using Python and Object-Oriented Programming (OOP).

This project includes:
Song management
Playlist handling
Recently played tracking
Clear playlist feature
Class-based OOP structure

📌 Features
✔ Add Songs
Users can add songs with:
Song name
Artist name

✔ Play Songs
Songs can be selected and played from the playlist.

✔ Recently Played List
Whenever a song is played, it is added to the "recently played" list.

✔ View Playlist
Displays all songs added to the playlist.

✔ Clear Playlist
Allows the user to:
Clear all songs
Clear recently played list

✔ OOP Concepts Used
Classes and objects
Encapsulation (attributes inside classes)
Methods for operations
Clean separation between Song and Playlist classes

🧠 Concepts Used
🔹 Classes
    Song — represents a single song
    Playlist — manages list of songs + recent songs

🔹 Lists
    Used to store playlist and recently played songs.

🔹 Encapsulation
    Song attributes stored and accessed safely.

🔹 Error Handling
    Handles invalid song selection.

Example Output screenshot:-
![alt text](image-5.png)
![alt text](image-6.png)


# Grading System
🏫 School Grading System (Python Project)
A simple School Grading System built using Python that calculates:

Total Marks
Percentage
Grade (A, B, C, D, F)
Distinction (if all subjects > 75)
Saves report to a .txt file
Uses functions + nested conditions + file handling
This project is perfect for beginners learning Python basics.

📌 Features
✔ Input marks for 5 subjects
User enters marks for:
five subects.

✔ Calculates
Total Marks
Percentage

✔ Grade Evaluation
Based on percentage:
| Percentage | Grade |
| ---------- | ----- |
| ≥ 80       | A     |
| 60–79      | B     |
| 45–59      | C     |
| 35–44      | D     |
| < 35       | F     |

🧠 Concepts Used
🔹 Functions
Used for:
Calculating grade
Checking distinction
Saving file

🔹 Nested Conditions
To evaluate grade rules.

🔹 File Handling
Stores student report in a .txt file.

🔹 Lists / Loops
Used to store and process marks.

Example Output Screenshots:-
![alt text](image-7.png)

# Hospital System
🏥 Hospital Patient Management System (Python Project)
A simple Hospital Patient Management System built using Python that supports:
Registering new patients
Storing patient data in a file
Doctor updating diagnosis
Billing system with senior-citizen discount (age > 60)
A medical record inside each patient (composition)
Uses: 
OOP, File Handling, Dictionaries, Composition, Nested Conditions

📌 Features
✔ Register New Patients
Each patient has:
Name
Age
Problem
Assigned doctor
Stored inside a file (patients.txt or .csv).
![alt text](image-8.png)

✔ Medical Record (Composition)
Each patient HAS a medical record object.

✔ Doctors Can Update Diagnosis
Doctor can:
Add new diagnosis
Update medicines
Mark follow-up dates

✔ Senior Citizen Discount
If age > 60, bill gets:
20% discount automatically.

🧠 Concepts Used
🔹 Object-Oriented Programming
Class Patient
Class MedicalRecord
Class HospitalSystem

🔹 Composition
Patient contains an object of MedicalRecord.

🔹 Nested Conditions
Used for:
Discounts
Diagnoses
Validations

🔹 File Handling
Used to save patient information in a text file.

🔹 Dictionaries
Used to store patient attributes.

Example Output Screenshot:-
![alt text](image-9.png)






