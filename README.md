# Banking System using Python, Tkinter & MySQL

## Description

This project is a GUI-based Banking Management System developed using Python Tkinter and MySQL database. It allows users to create accounts, deposit and withdraw money, and store account details securely in a database.

## Features

* Create new bank account
* Deposit amount
* Withdraw amount
* Check balance
* Data stored in MySQL database
* User-friendly GUI interface

## Technologies Used

* Python
* Tkinter
* MySQL
* mysql-connector-python

## Project Structure

Bank_Project/

* main.py
* gui.py
* operations.py
* db_config.py
* README.md

## Database Setup

```sql
CREATE DATABASE bank_db;

USE bank_db;

CREATE TABLE accounts(
    account_no INT PRIMARY KEY,
    name VARCHAR(50),
    balance INT
);
```

## How to Run

1. Install dependency:
   pip install mysql-connector-python

2. Configure database in db_config.py

3. Run the project:
   python main.py

## Author

Dhanushree Arangaswamy
