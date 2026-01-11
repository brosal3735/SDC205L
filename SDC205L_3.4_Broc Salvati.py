"""
Spreadsheet Automation (Week 4 style)
Menu option 1 is implemented: Input Data
Options 2 and 3 print: Error: The chosen functionality is not implemented yet
"""

from datetime import datetime

# Change this to match the spreadsheet you selected in Part 1:
# "Temperature", "Weight", or "Rain Amount"
SPREADSHEET_TYPE = "Rain Amount"


def convertData(data):
    """
    Takes one argument (data) and returns the converted value appropriate
    for the spreadsheet selected.
      - F to C: (F - 32) * 5/9
      - lbs to Kg: lbs / 2.205
      - in to cm: in * 2.54
    """
    if SPREADSHEET_TYPE == "Temperature":
        return (data - 32) * 5 / 9
    if SPREADSHEET_TYPE == "Weight":
        return data / 2.205
    if SPREADSHEET_TYPE == "Rain Amount":
        return data * 2.54

    raise ValueError("Invalid SPREADSHEET_TYPE. Use: Temperature, Weight, or Rain Amount.")


def getInput():
    # Ask how many entries the user is inputting
    while True:
        try:
            entries = int(input("How many entries are you inputting?\n"))
            if entries <= 0:
                print("Please enter a whole number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (example: 3).")

    # Collect entries
    for _ in range(entries):
        date_str = input("\nEnter a date:\n")

        # Prompt for the correct value based on spreadsheet choice
        if SPREADSHEET_TYPE == "Temperature":
            prompt = "Enter the highest temp for the inputted date:\n"
        elif SPREADSHEET_TYPE == "Weight":
            prompt = "Enter the weight in pounds for the inputted date:\n"
        else:
            prompt = "Enter the rain amount in inches for the inputted date:\n"

        # Read numeric input with validation
        while True:
            try:
                raw_value = float(input(prompt))
                break
            except ValueError:
                print("Please enter a valid number (example: 70, 80, 2.5).")

        # convertData(data) where data = raw_value and return is the converted value
        converted_value = convertData(raw_value)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{date_str},{raw_value:g},{converted_value}")


def print_menu():
    print("Brosal3735's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report")


def main():
    print_menu()

    # Basic error-checking for menu selection
    choice = input("").strip()

    if choice == "1":
        print(f"You selected 1 at {datetime.now()}")
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")


if __name__ == "__main__":
    main()


