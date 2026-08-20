from datetime import datetime
import uuid
import math
import random

from utilities.datetime_utils import (
    current_datetime,
    date_difference,
    custom_date_format,
    stopwatch,
    countdown
)

from utilities.math_utils import (
    factorial,
    compound_interest,
    circle_area,
    rectangle_area,
    square_area,
    logarithm,
    trigonometry
)

from utilities.random_utils import (
    random_number,
    random_list,
    generate_password,
    generate_otp,
    random_sample
)

from utilities.file_utils import (
    write_file,
    append_file,
    read_file,
    update_file
)


def time_operations():

    while True:

        print("\n========== DATE & TIME MODULE ==========")
        print("1. Current Date and Time")
        print("2. Date Difference")
        print("3. Custom Date Format")
        print("4. Stopwatch")
        print("5. Countdown")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\nCurrent Date and Time:")
            print(current_datetime())

        elif choice == "2":

            date1 = input("Enter first date (DD-MM-YYYY): ")
            date2 = input("Enter second date (DD-MM-YYYY): ")

            try:

                date1 = datetime.strptime(
                    date1,
                    "%d-%m-%Y"
                )

                date2 = datetime.strptime(
                    date2,
                    "%d-%m-%Y"
                )

                result = date_difference(
                    date1,
                    date2
                )

                print("Difference:", result, "days")

            except ValueError:

                print("Invalid date format!")

        elif choice == "3":

            print("\nCustom Date Format:")
            print(custom_date_format())

        elif choice == "4":

            seconds = int(
                input("Enter stopwatch seconds: ")
            )

            stopwatch(seconds)

        elif choice == "5":

            seconds = int(
                input("Enter countdown seconds: ")
            )

            countdown(seconds)

        elif choice == "6":

            break

        else:

            print("Invalid choice!")


def math_operations():

    while True:

        print("\n========== MATH MODULE ==========")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Circle Area")
        print("4. Rectangle Area")
        print("5. Square Area")
        print("6. Logarithm")
        print("7. Trigonometry")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            number = int(
                input("Enter number: ")
            )

            print(
                "Factorial:",
                factorial(number)
            )

        elif choice == "2":

            principal = float(
                input("Enter principal amount: ")
            )

            rate = float(
                input("Enter rate: ")
            )

            time = float(
                input("Enter time in years: ")
            )

            n = int(
                input("Enter compounding frequency: ")
            )

            amount, interest = compound_interest(
                principal,
                rate,
                time,
                n
            )

            print("Final Amount:", amount)
            print("Compound Interest:", interest)

        elif choice == "3":

            radius = float(
                input("Enter radius: ")
            )

            print(
                "Circle Area:",
                circle_area(radius)
            )

        elif choice == "4":

            length = float(
                input("Enter length: ")
            )

            width = float(
                input("Enter width: ")
            )

            print(
                "Rectangle Area:",
                rectangle_area(
                    length,
                    width
                )
            )

        elif choice == "5":

            side = float(
                input("Enter side: ")
            )

            print(
                "Square Area:",
                square_area(side)
            )

        elif choice == "6":

            number = float(
                input("Enter number: ")
            )

            base = float(
                input("Enter base: ")
            )

            print(
                "Logarithm:",
                logarithm(
                    number,
                    base
                )
            )

        elif choice == "7":

            angle = float(
                input("Enter angle: ")
            )

            result = trigonometry(angle)

            print("Sin:", result["sin"])
            print("Cos:", result["cos"])
            print("Tan:", result["tan"])

        elif choice == "8":

            break

        else:

            print("Invalid choice!")


def random_operations():

    while True:

        print("\n========== RANDOM MODULE ==========")
        print("1. Random Number")
        print("2. Random List")
        print("3. Generate Password")
        print("4. Generate OTP")
        print("5. Random Sampling")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            start = int(
                input("Enter starting number: ")
            )

            end = int(
                input("Enter ending number: ")
            )

            print(
                "Random Number:",
                random_number(
                    start,
                    end
                )
            )

        elif choice == "2":

            size = int(
                input("Enter list size: ")
            )

            start = int(
                input("Enter starting number: ")
            )

            end = int(
                input("Enter ending number: ")
            )

            print(
                "Random List:",
                random_list(
                    size,
                    start,
                    end
                )
            )

        elif choice == "3":

            length = int(
                input("Enter password length: ")
            )

            print(
                "Generated Password:",
                generate_password(length)
            )

        elif choice == "4":

            print(
                "Generated OTP:",
                generate_otp()
            )

        elif choice == "5":

            data = input(
                "Enter values separated by space: "
            ).split()

            count = int(
                input("How many values to select? ")
            )

            if count <= len(data):

                print(
                    "Random Sample:",
                    random_sample(
                        data,
                        count
                    )
                )

            else:

                print(
                    "Count cannot be greater than data size."
                )

        elif choice == "6":

            break

        else:

            print("Invalid choice!")


def uuid_operation():

    print("\n========== UUID MODULE ==========")

    unique_id = uuid.uuid4()

    print("Generated UUID:")
    print(unique_id)


def file_operations():

    print("\n========== FILE OPERATIONS ==========")

    filename = input(
        "Enter file name: "
    )

    print("1. Write")
    print("2. Append")
    print("3. Read")
    print("4. Update")

    choice = input(
        "Enter choice: "
    )

    if choice == "1":

        data = input(
            "Enter data: "
        )

        print(
            write_file(
                filename,
                data
            )
        )

    elif choice == "2":

        data = input(
            "Enter data: "
        )

        print(
            append_file(
                filename,
                data
            )
        )

    elif choice == "3":

        print("\nFile Content:")

        print(
            read_file(filename)
        )

    elif choice == "4":

        old_text = input(
            "Enter old text: "
        )

        new_text = input(
            "Enter new text: "
        )

        print(
            update_file(
                filename,
                old_text,
                new_text
            )
        )

    else:

        print("Invalid choice!")


def explore_module():

    print(
        "\n========== DYNAMIC MODULE EXPLORATION =========="
    )

    print("1. Explore Math Module")
    print("2. Explore Random Module")
    print("3. Explore DateTime Module")

    choice = input(
        "Enter choice: "
    )

    if choice == "1":

        print("\nMath Module Attributes:")

        print(
            dir(math)
        )

    elif choice == "2":

        print("\nRandom Module Attributes:")

        print(
            dir(random)
        )

    elif choice == "3":

        print("\nDateTime Module Attributes:")

        print(
            dir(datetime)
        )

    else:

        print("Invalid choice!")


def main():

    while True:

        print("\n==========================================")
        print("       WELCOME TO MULTI-UTILITY TOOLKIT")
        print("==========================================")

        print("1. Date & Time Module")
        print("2. Math Module")
        print("3. Random Module")
        print("4. UUID Module")
        print("5. File Operations")
        print("6. Dynamic Module Exploration")
        print("7. Exit")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            time_operations()

        elif choice == "2":

            math_operations()

        elif choice == "3":

            random_operations()

        elif choice == "4":

            uuid_operation()

        elif choice == "5":

            file_operations()

        elif choice == "6":

            explore_module()

        elif choice == "7":

            print(
                "\nThank you for using Multi-Utility Toolkit!"
            )

            break

        else:

            print(
                "Invalid choice! Please try again."
            )


if __name__ == "__main__":
  
   main()