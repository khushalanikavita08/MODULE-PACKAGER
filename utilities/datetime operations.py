from datetime import datetime
import time


def current_datetime():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def date_difference(date1, date2):
    difference = abs(date2 - date1)
    return difference.days


def custom_date_format():
    now = datetime.now()
    return now.strftime("%A, %d %B %Y - %I:%M:%S %p")


def stopwatch(seconds):
    print("\nStopwatch started...")

    for i in range(seconds, 0, -1):
        print("Time remaining:", i)
        time.sleep(1)

    print("Stopwatch finished!")


def countdown(seconds):
    print("\nCountdown started...")

    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

    print("Time's up!")
