import csv

def main():
    # Open grades.csv file for reading
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        # Loop through each row in the CSV file
        for row in reader:
            # Print each row in a formatted manner
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))

if __name__ == "__main__":
    main()