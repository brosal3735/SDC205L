from datetime import datetime

# Display the application title with student ID
student_id = "Student1234"
print(f"{student_id}'s Excel Spreadsheet Automation Menu")

# Display menu options
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called choice.
choice = input()

# Display the selected option with current date and time
print(f"You selected {choice} at {str(datetime.now())}")


