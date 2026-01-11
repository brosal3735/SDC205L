"""
Spreadsheet Automation Project (File Handling / CSV)
Student ID: Brosal3735

This program prints a menu and supports:
1) Input Data -> collect date + value, convert it, and append to ZooData.csv
2) View Current Data -> print the file path and contents of ZooData.csv
3) Generate Report -> not implemented (prints error)
"""

from datetime import datetime

# Choose ONE spreadsheet type for your project:
# "Temperature", "Weight", or "Rain Amount"
SPREADSHEET_TYPE = "Temperature"

# Update this path if your instructor requires a different location.
# The sample output shows a path similar to: C:\Users\student\ZooData.csv
ZOO_CSV_PATH = r"C:\Users\student\ZooData.csv"


def convertData(data):
    """Converts the numeric input to the appropriate value for the selected spreadsheet."""
    if SPREADSHEET_TYPE == "Temperature":
        # F to C: (F - 32) * 5/9
        return (data - 32) * 5 / 9
    if SPREADSHEET_TYPE == "Weight":
        # lbs to Kg: lbs / 2.205
        return data / 2.205
    if SPREADSHEET_TYPE == "Rain Amount":
        # in to cm: in * 2.54
        return data * 2.54

    raise ValueError("Invalid SPREADSHEET_TYPE. Use Temperature, Weight, or Rain Amount.")


def insertData(path, csv_line):
    """
    Appends a comma-separated string to a CSV file (or creates it if it does not exist).
    Uses try-except to catch errors while writing.
    """
    try:
        with open(path, "a", encoding="utf-8") as f:
            # Ensure each record is on its own line
            f.write(csv_line + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        raise


def viewData(path):
    """
    Displays the path of the file being read and prints the contents of the CSV file.
    Uses minimal permissions ('r') and includes try-except for reading errors.
    """
    try:
        print(f"The file {path}")
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {path}")
        print("Error: File not found. Add data first using option 1.")
    except Exception as e:
        print(f"Error reading file: {e}")


def getInput():
    """Collects user entries, converts values, and saves each entry to ZooData.csv."""
    while True:
        try:
            entries = int(input("How many entries are you inputting?\n"))
            if entries <= 0:
                print("Please enter a whole number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (example: 3).")

    for _ in range(entries):
        date_str = input("\nEnter a date:\n")

        if SPREADSHEET_TYPE == "Temperature":
            prompt = "Enter the highest temp for the inputted date:\n"
        elif SPREADSHEET_TYPE == "Weight":
            prompt = "Enter the weight in pounds for the inputted date:\n"
        else:
            prompt = "Enter the rain amount in inches for the inputted date:\n"

        while True:
            try:
                raw_value = float(input(prompt))
                break
            except ValueError:
                print("Please enter a valid number (example: 70, 80, 2.5).")

        # convertData(data): data is the numeric input; return is the converted numeric value
        converted_value = convertData(raw_value)

        # Build the CSV line exactly as shown in the sample: date,raw,converted
        csv_line = f"{date_str},{raw_value:g},{converted_value}"

        # Store the line in ZooData.csv with try-except around the write
        try:
            insertData(ZOO_CSV_PATH, csv_line)
            print(f"The following was saved at {datetime.now()} :")
            print(csv_line)
        except Exception:
            print("Error: Could not save the data.")


def print_menu():
    print("\n==============================")
    print("Brosal3735's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report")


def main():
    print_menu()
    choice = input("").strip()

    if choice == "1":
        print(f"You selected 1 at {datetime.now()}")
        getInput()
    elif choice == "2":
        print(f"You selected 2 at {datetime.now()}")
        viewData(ZOO_CSV_PATH)
    else:
        print("Error: The chosen functionality is not implemented yet")


if __name__ == "__main__":
    main()



