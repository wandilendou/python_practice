# Program to store personal information in a dictionary

def main():
    # Create an empty dictionary
    person_info = {}

    # Get user input
    person_info['name'] = input("Enter your name: ")
    person_info['age'] = input("Enter your age: ")
    person_info['favorite_color'] = input("Enter your favorite color: ")

    # Display the dictionary
    print("\nStored information:")
    print(person_info)

# Run the program
if __name__ == "__main__":
    main()
