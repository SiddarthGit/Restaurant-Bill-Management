# Restaurant-Bill-Management
Restaurant Bill Management System
![image](https://github.com/user-attachments/assets/3e59dfdf-763b-44ed-bbd7-0b1e2174e3a8)
Restaurant Management System

Overview

This is a graphical user interface (GUI) application developed using Python's Tkinter library. The application provides a login system, a billing section, and a built-in calculator. It is designed to help manage restaurant operations efficiently.

Features

Login System: Users must enter a username and password to access the billing section.

Billing Section: Users can enter customer details, purchase information, and generate bills.

Calculator: A basic calculator for performing quick arithmetic calculations.

Bill Generation: Automatically generates a bill number and allows adding items.

Total Calculation: Computes the total cost of all purchased items.

Reset & Clear Functionality: Users can reset or clear entries as needed.

Installation

Prerequisites

Ensure you have Python installed (3.x recommended). You can download it from python.org.

Required Libraries

The required libraries (Tkinter, datetime, random) are included with Python by default.

Running the Application

Save the script as restaurant_management.py and run it using:

python restaurant_management.py

File Structure

restaurant_management.py  # Main script containing the GUI application

Code Explanation

1. Main Function

Initializes the Tkinter window and calls the LoginPage class.

2. LoginPage Class

Displays the login screen.

Has fields for username and password.

Only allows access to billing upon successful login.

3. Window2 Class (Billing Section)

Manages the billing system.

Allows users to input customer details and item purchases.

Calculates total cost.

Displays a formatted bill.

Provides options to reset, clear, and save bills.

4. Calculator

Built-in calculator for quick calculations.

Uses Tkinter buttons and an event-driven approach.

5. Functions

check_login(): Enables billing section after login.

reset(): Clears login fields.

genbill(): Generates and formats the bill.

add_func(): Adds an item to the bill.

total_func(): Computes and displays the total amount.

press_btn(event): Handles calculator button presses.

References

Tkinter Documentation

Tkinter Relief Styles

Future Enhancements

Implement a database for storing customer details.

Add authentication with hashed passwords.

Export bills as PDF.

Implement discount and tax calculation.
