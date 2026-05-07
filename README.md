# 🏨 HOTEL MANAGEMENT SYSTEM

A simple yet professional **Hotel Management System** built using **Python** and **Object-Oriented Programming (OOP)** concepts.
This project allows hotel staff to manage room bookings, calculate bills, save customer records, search records, and manage hotel services efficiently.

---

# ✨ Features

* ✅ Room Booking System
* ✅ Auto Generated Customer ID
* ✅ Auto Generated Room Number
* ✅ Booking Date & Time
* ✅ AC / Non-AC Room Selection
* ✅ Single / Double Bed Selection
* ✅ Food Service
* ✅ WiFi Service
* ✅ Laundry Service
* ✅ Automatic Bill Calculation
* ✅ File Handling using `.txt`
* ✅ Save Customer Records
* ✅ View All Saved Records
* ✅ Search Customer Records
* ✅ Clear All Records
* ✅ Professional Console UI
* ✅ Error Handling

---

# 🛠 Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* File Handling
* Random Module
* Datetime Module

---

# 📂 Project Structure

```bash
Hotel-Management-System/
│
├── hotel_management.py
├── hotelrecord.txt
└── README.md
```

---

# ⚙ How It Works

## 1️⃣ Book Room

The user enters:

* Customer Name
* Mobile Number
* Room Type
* Bed Type
* Number of Days

Additional services:

* Food
* WiFi
* Laundry

The system then:

* Generates Customer ID
* Assigns Room Number
* Stores Booking Time
* Calculates Final Bill

---

## 2️⃣ View Saved Records

Displays all customer records in a clean tabular format including:

* Customer ID
* Name
* Mobile Number
* Room Number
* Booking Time
* Room Details
* Charges
* Total Bill

---

## 3️⃣ Search Customer

Search any customer record using the customer name.

---

## 4️⃣ Clear Records

Deletes all saved records from the file.

---

# 💰 Room Pricing

| Room Type | Bed Type | Price Per Day |
| --------- | -------- | ------------- |
| AC        | Single   | ₹2000         |
| AC        | Double   | ₹3000         |
| Non-AC    | Single   | ₹1000         |
| Non-AC    | Double   | ₹1500         |

---

# 🍽 Additional Service Charges

| Service | Charge Per Day |
| ------- | -------------- |
| Food    | ₹500           |
| WiFi    | ₹100           |
| Laundry | ₹200           |

---

# 📸 Sample Output

```text
===================================
         CUSTOMER DETAILS
===================================

Customer ID   : CUST4821
Customer Name : Swaroopa Goswami
Mobile Number : 9876543210
Room Number   : 204
Booking Time  : 07-05-2026 14:22:10

-----------------------------------

Room Type     : Ac
Bed Type      : Double
Days Stayed   : 3

-----------------------------------

Room Rent     : ₹9000
Food Charge   : ₹1500
WiFi Charge   : ₹300
Laundry Charge: ₹600

-----------------------------------

TOTAL BILL    : ₹11400

===================================
```

---

# 🚀 How To Run

## Clone Repository

```bash
git clone https://github.com/Swaroopa-Goswami/Hotel-Management-System.git
```

---

## Open Project Folder

```bash
cd Hotel-Management-System
```

---

## Run Program

```bash
python hotel_management.py
```

---

# 📚 Concepts Used

This project demonstrates:

* Classes & Objects
* Constructors
* Methods
* Conditional Statements
* Loops
* Exception Handling
* File Handling
* String Formatting
* Random Number Generation
* Date & Time Handling

---

# 🎯 Future Improvements

* 🔹 GUI Version using Tkinter
* 🔹 Database Integration (MySQL)
* 🔹 Admin Login System
* 🔹 Room Availability Tracking
* 🔹 Online Booking
* 🔹 Bill Invoice Generation (PDF)
* 🔹 Customer Check-In / Check-Out
* 🔹 Data Analytics Dashboard
* 🔹 Web Version using Flask/Django

---

# ⭐ Project Status

✅ Completed
📌 Beginner-Friendly Python Project
🎓 Great for Academic Mini Projects & OOP Practice

---

# 📄 License

This project is open-source and free to use for educational purposes.
