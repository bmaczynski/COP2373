import csv

def main():
    def input_grades():
        # Input number of students
        num_students = int(input("Enter the number of students: "))
        
        # Open grades.csv file for writing using with
        with open('grades.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
            
            # For loop through the number of students
            for _ in range(num_students):
                # Input student's first name
                first_name = input("Enter student's first name: ")
                # Input student's last name
                last_name = input("Enter student's last name: ")
                # Input student's Exam 1 grade
                exam1 = int(input("Enter Exam 1 grade: "))
                # Input student's Exam 2 grade
                exam2 = int(input("Enter Exam 2 grade: "))
                # Input student's Exam 3 grade
                exam3 = int(input("Enter Exam 3 grade: "))
                # Write the student's data to the CSV file
                writer.writerow([first_name, last_name, exam1, exam2, exam3])

    def display_grades():
        # Open grades.csv file for reading
        with open('grades.csv', mode='r') as file:
            reader = csv.reader(file)
            # Loop through each row in the CSV file
            for row in reader:
                # Print each row in a formatted manner
                print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))

    # Ask user if they want to input or display grades
    choice = input("Do you want to (1) input grades or (2) display grades? Enter 1 or 2: ")
    
    # Conditional for user choice
    if choice == '1':
        input_grades()
    elif choice == '2':
        display_grades()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()