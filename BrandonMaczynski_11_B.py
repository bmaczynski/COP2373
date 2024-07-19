import math

# Create method to calculate the hypotenuse
def calculate_hypotenuse(angle, adjacent_length):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle)
    # Calculate the hypotenuse using the cosine function
    hypotenuse_length = adjacent_length / math.cos(angle_radians)
    return hypotenuse_length

def main():
    # Prompt user to enter nearest angle in degrees
    angle = float(input("Enter the nearest angle in degrees: "))
    # Prompt user to enter the length of adjacent side
    adjacent_length = float(input("Enter the length of the adjacent side: "))
    # Calculate hypotenuse using method calculate_hypotenuse
    hypotenuse_length = calculate_hypotenuse(angle, adjacent_length)
    # Display result
    print(f"The length of the hypotenuse is: {hypotenuse_length:.2f}")

if __name__ == "__main__":
    main()