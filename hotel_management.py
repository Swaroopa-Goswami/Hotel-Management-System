from datetime import datetime
import random


class HotelRoom:

    # ==================================================
    # CONSTRUCTOR
    # ==================================================

    def __init__(self):

        self.customer_id = ""
        self.name = ""
        self.mobile = ""
        self.room_number = 0
        self.booking_time = ""

        self.room_type = ""
        self.bed_type = ""
        self.days = 0

        self.food = ""
        self.wifi = ""
        self.laundry = ""

        self.rent = 0
        self.food_charge = 0
        self.wifi_charge = 0
        self.laundry_charge = 0

        self.total_bill = 0

    # ==================================================
    # BOOK ROOM
    # ==================================================

    def book_room(self):

        print("\n===================================")
        print("          ROOM BOOKING")
        print("===================================")

        # AUTO GENERATED DETAILS

        self.customer_id = "CUST" + str(random.randint(1000, 9999))

        self.room_number = random.randint(101, 500)

        self.booking_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        # CUSTOMER DETAILS

        self.name = input(
            "Enter Customer Name : "
        ).title()

        self.mobile = input(
            "Enter Mobile Number : "
        )

        self.room_type = input(
            "Enter Room Type (AC / Non-AC) : "
        ).strip().title()

        self.bed_type = input(
            "Enter Bed Type (Single / Double) : "
        ).strip().title()

        self.days = int(
            input("Enter Number of Days Stayed : ")
        )

        print("\n----------- EXTRA SERVICES -----------")

        self.food = input(
            "Food Service Required? (yes / no) : "
        ).strip().lower()

        self.wifi = input(
            "WiFi Service Required? (yes / no) : "
        ).strip().lower()

        self.laundry = input(
            "Laundry Service Required? (yes / no) : "
        ).strip().lower()

    # ==================================================
    # CALCULATE RENT
    # ==================================================

    def calculate_rent(self):

        # ROOM RENT

        if self.room_type == "Ac" and self.bed_type == "Single":

            self.rent = self.days * 2000

        elif self.room_type == "Ac" and self.bed_type == "Double":

            self.rent = self.days * 3000

        elif self.room_type == "Non-Ac" and self.bed_type == "Single":

            self.rent = self.days * 1000

        elif self.room_type == "Non-Ac" and self.bed_type == "Double":

            self.rent = self.days * 1500

        else:

            print("\n⚠ Invalid Room Type or Bed Type!")
            self.rent = 0

        # FOOD CHARGE

        if self.food == "yes":

            self.food_charge = self.days * 500

        else:

            self.food_charge = 0

        # WIFI CHARGE

        if self.wifi == "yes":

            self.wifi_charge = self.days * 100

        else:

            self.wifi_charge = 0

        # LAUNDRY CHARGE

        if self.laundry == "yes":

            self.laundry_charge = self.days * 200

        else:

            self.laundry_charge = 0

        # TOTAL BILL

        self.total_bill = (
            self.rent
            + self.food_charge
            + self.wifi_charge
            + self.laundry_charge
        )

    # ==================================================
    # DISPLAY CUSTOMER DETAILS
    # ==================================================

    def display(self):

        print("\n===================================")
        print("         CUSTOMER DETAILS")
        print("===================================")

        print(f"Customer ID   : {self.customer_id}")
        print(f"Customer Name : {self.name}")
        print(f"Mobile Number : {self.mobile}")
        print(f"Room Number   : {self.room_number}")
        print(f"Booking Time  : {self.booking_time}")

        print("-----------------------------------")

        print(f"Room Type     : {self.room_type}")
        print(f"Bed Type      : {self.bed_type}")
        print(f"Days Stayed   : {self.days}")

        print("-----------------------------------")

        print(f"Room Rent     : ₹{self.rent}")
        print(f"Food Charge   : ₹{self.food_charge}")
        print(f"WiFi Charge   : ₹{self.wifi_charge}")
        print(f"Laundry Charge: ₹{self.laundry_charge}")

        print("-----------------------------------")

        print(f"TOTAL BILL    : ₹{self.total_bill}")

        print("===================================")

    # ==================================================
    # SAVE RECORD
    # ==================================================

    def save_record(self):

        with open("hotelrecord.txt", "a") as file:

            file.write(
                f"{self.customer_id},"
                f"{self.name},"
                f"{self.mobile},"
                f"{self.room_number},"
                f"{self.booking_time},"
                f"{self.room_type},"
                f"{self.bed_type},"
                f"{self.days},"
                f"{self.rent},"
                f"{self.food_charge},"
                f"{self.wifi_charge},"
                f"{self.laundry_charge},"
                f"{self.total_bill}\n"
            )

        print("\nRecord Saved Successfully!")

    # ==================================================
    # SHOW RECORDS
    # ==================================================

    def show_records(self):

        try:

            with open("hotelrecord.txt", "r") as file:

                records = file.readlines()

                if len(records) == 0:

                    print("\n⚠ No Records Found!")
                    return

                print("\n==============================================================================================================================================================================")

                print(
                    f"{'ID':<12}"
                    f"{'NAME':<25}"
                    f"{'MOBILE':<15}"
                    f"{'ROOM':<8}"
                    f"{'DATE & TIME':<22}"
                    f"{'TYPE':<10}"
                    f"{'BED':<10}"
                    f"{'DAYS':<8}"
                    f"{'RENT':<10}"
                    f"{'FOOD':<10}"
                    f"{'WIFI':<10}"
                    f"{'LAUNDRY':<12}"
                    f"{'TOTAL':<10}"
                )

                print("==============================================================================================================================================================================")

                for line in records:

                    data = line.strip().split(",")

                    if len(data) >= 13:

                        print(
                            f"{data[0]:<12}"
                            f"{data[1]:<25}"
                            f"{data[2]:<15}"
                            f"{data[3]:<8}"
                            f"{data[4]:<22}"
                            f"{data[5]:<10}"
                            f"{data[6]:<10}"
                            f"{data[7]:<8}"
                            f"{data[8]:<10}"
                            f"{data[9]:<10}"
                            f"{data[10]:<10}"
                            f"{data[11]:<12}"
                            f"{data[12]:<10}"
                        )

                print("==============================================================================================================================================================================")

        except FileNotFoundError:

            print("\n⚠ No Records File Found!")

    # ==================================================
    # SEARCH CUSTOMER
    # ==================================================

    def search_customer(self):

        search_name = input(
            "\nEnter Customer Name to Search : "
        ).title()

        found = False

        try:

            with open("hotelrecord.txt", "r") as file:

                records = file.readlines()

                for line in records:

                    data = line.strip().split(",")

                    if data[1] == search_name:

                        found = True

                        print("\n===================================")
                        print("        CUSTOMER FOUND")
                        print("===================================")

                        print(f"Customer ID   : {data[0]}")
                        print(f"Customer Name : {data[1]}")
                        print(f"Mobile Number : {data[2]}")
                        print(f"Room Number   : {data[3]}")
                        print(f"Booking Time  : {data[4]}")
                        print(f"Room Type     : {data[5]}")
                        print(f"Bed Type      : {data[6]}")
                        print(f"Days Stayed   : {data[7]}")
                        print(f"Room Rent     : ₹{data[8]}")
                        print(f"Food Charge   : ₹{data[9]}")
                        print(f"WiFi Charge   : ₹{data[10]}")
                        print(f"Laundry Charge: ₹{data[11]}")
                        print(f"Total Bill    : ₹{data[12]}")

                        print("===================================")

                if found == False:

                    print("\n❌ Customer Record Not Found!")

        except FileNotFoundError:

            print("\n⚠ No Records File Found!")

    # ==================================================
    # CLEAR ALL RECORDS
    # ==================================================

    def clear_records(self):

        with open("hotelrecord.txt", "w") as file:
            pass

        print("\n🗑 All Records Cleared Successfully!")


# ==================================================
# MAIN PROGRAM
# ==================================================

print("************************************************")
print("              WELCOME TO TAJ HOTEL")
print("************************************************")
print("           HOTEL MANAGEMENT SYSTEM")
print("************************************************")

h1 = HotelRoom()

while True:

    print("\n=============== MAIN MENU ===============")

    print("1. Book Room")
    print("2. View Saved Records")
    print("3. Search Customer Record")
    print("4. Clear All Records")
    print("5. Exit")

    print("=========================================")

    try:

        ch = int(input("Enter Your Choice : "))

        # BOOK ROOM

        if ch == 1:

            h1.book_room()

            h1.calculate_rent()

            h1.display()

            h1.save_record()

        # VIEW RECORDS

        elif ch == 2:

            h1.show_records()

        # SEARCH CUSTOMER

        elif ch == 3:

            h1.search_customer()

        # CLEAR RECORDS

        elif ch == 4:

            confirm = input(
                "\nAre you sure you want to clear all records? (yes/no): "
            ).lower()

            if confirm == "yes":

                h1.clear_records()

            else:

                print("\nOperation Cancelled!")

        # EXIT

        elif ch == 5:

            print("\n===================================")
            print(" Thank You for Visiting TAJ HOTEL")
            print("        Visit Again")
            print("===================================")

            break

        else:

            print("\nInvalid Choice!")

    except ValueError:

        print("\n⚠ Please Enter Numbers Only!")