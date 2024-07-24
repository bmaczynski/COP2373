import numpy as np
import csv

# Function to load data from the CSV file into a numpy array
def load_data(filename):
    # Initialize an empty list to store data
    data = []
    # Open the CSV file for reading
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        # Read each row in the CSV file
        for row in reader:
            # Append exam scores to the data list
            data.append([int(row[2]), int(row[3]), int(row[4])])
    # Convert the data list to a numpy array
    return np.array(data)

# Function to print the first few rows of the dataset
def print_first_rows(data, num_rows=12):
    print("Test Scores:")
    # Print the specified number of rows
    print(data[:num_rows])

# Function to calculate and print statistics for each exam
def calculate_statistics(data):
    print("\nStatistics for each exam:")
    # Loop through each exam (column)
    for i in range(data.shape[1]):
        # Get scores for the current exam
        exam_scores = data[:, i]
        print(f"Exam {i+1}:")
        # Calculate and print the mean
        print(f"  Mean: {np.mean(exam_scores):.2f}")
        # Calculate and print the median
        print(f"  Median: {np.median(exam_scores):.2f}")
        # Calculate and print the standard deviation
        print(f"  Standard Deviation: {np.std(exam_scores):.2f}")
        # Print the minimum score
        print(f"  Minimum: {np.min(exam_scores)}")
        # Print the maximum score
        print(f"  Maximum: {np.max(exam_scores)}")

# Function to calculate and print overall statistics for the entire dataset
def calculate_overall_statistics(data):
    # Flatten the data to get all scores combined
    all_scores = data.flatten()
    print("\nOverall statistics for all exams combined:")
    # Calculate and print the mean for all scores
    print(f"  Mean: {np.mean(all_scores):.2f}")
    # Calculate and print the median for all scores
    print(f"  Median: {np.median(all_scores):.2f}")
    # Calculate and print the standard deviation for all scores
    print(f"  Standard Deviation: {np.std(all_scores):.2f}")
    # Print the minimum score for all exams
    print(f"  Minimum: {np.min(all_scores)}")
    # Print the maximum score for all exams
    print(f"  Maximum: {np.max(all_scores)}")

# Function to determine and print the number of students who passed and failed each exam
def calculate_pass_fail(data, passing_grade=60):
    print("\nNumber of students who passed and failed each exam:")
    # Loop through each exam (column)
    for i in range(data.shape[1]):
        # Get scores for the current exam
        exam_scores = data[:, i]
        # Count the number of students who passed
        num_passed = np.sum(exam_scores >= passing_grade)
        # Count the number of students who failed
        num_failed = np.sum(exam_scores < passing_grade)
        print(f"Exam {i+1}: Passed: {num_passed}, Failed: {num_failed}")

# Function to calculate and print the overall pass percentage across all exams
def calculate_overall_pass_percentage(data, passing_grade=60):
    # Flatten the data to get all scores combined
    all_scores = data.flatten()
    # Calculate the number of passing scores
    num_passed = np.sum(all_scores >= passing_grade)
    # Calculate the total number of scores
    total_scores = all_scores.size
    # Calculate the pass percentage
    pass_percentage = (num_passed / total_scores) * 100
    print(f"\nOverall pass percentage across all exams: {pass_percentage:.2f}%")

def main():
    # Load data from the CSV file
    filename = 'grades.csv'
    data = load_data(filename)
    
    # Print the first few rows of the dataset
    print_first_rows(data)
    # Calculate and print statistics for each exam
    calculate_statistics(data)
    # Calculate and print overall statistics
    calculate_overall_statistics(data)
    # Calculate and print the number of students who passed and failed each exam
    calculate_pass_fail(data)
    # Calculate and print the overall pass percentage across all exams
    calculate_overall_pass_percentage(data)

if __name__ == "__main__":
    main()