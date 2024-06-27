import csv

def main():
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

if __name__ == "__main__":
    main()