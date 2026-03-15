# Secure Password Generator

A **Secure Password Generator** built using **Python and Tkinter** that allows users to generate strong and customizable passwords.  
The application also evaluates password strength and allows users to copy generated passwords directly to the clipboard.

This project demonstrates **GUI development, password security concepts, and modular Python programming**.

---

## Features

- Generate **random secure passwords**
- Customize password length
- Select character types:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special symbols (#, $, %, etc.)
- Automatic **password strength detection**
- **Copy password to clipboard** with one click
- Simple and user-friendly **Tkinter GUI**

---

## Project Structure

```
Password-Generator
│
├── main.py              # Tkinter GUI application
├── generator_logic.py   # Password generation and strength logic
└── README.md            # Project documentation
```

---

## Technologies Used

- **Python**
- **Tkinter** – GUI development
- **Pyperclip** – clipboard access
- **Random / String libraries** – password generation

---

## How the Password Generator Works

1. The user selects:
   - Password length
   - Character types (uppercase, lowercase, digits, symbols)

2. The program randomly generates characters based on selected options.

3. The generated password is displayed in the interface.

4. The password strength is analyzed and classified as:

- **Weak**
- **Medium**
- **Strong**

---

## Installation

### 1. Clone the repository

```
```

### 2. Install required library

```
pip install pyperclip
```

Tkinter usually comes pre-installed with Python.

---

## Running the Application

Run the following command:

```
python main.py
```

The GUI application will open where you can:

1. Choose password length
2. Select character types
3. Generate a secure password
4. View password strength
5. Copy password to clipboard

---

## Example Generated Password

```
G7#kP9@dL2!q
```

Strength: **Strong**

---

## Learning Objectives

This project demonstrates:

- Python **GUI development with Tkinter**
- **Secure password generation techniques**
- **User input validation**
- **Clipboard operations**
- **Modular programming**

---
