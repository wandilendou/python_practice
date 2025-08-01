# Python program to create a list of integers from user input and compute the sum

def main():
    print("Enter integers separated by spaces:")
    
    try:
        # Get input from user
        user_input = input(">> ")
        
        # Split the input string into list elements and convert to integers
        int_list = list(map(int, user_input.split()))
        
        # Calculate the sum
        total = sum(int_list)
        
        print(f"The list you entered is: {int_list}")
        print(f"The sum of the integers is: {total}")
    
    except ValueError:
        print("Please make sure to enter only integers separated by spaces.")

# Run the program
if __name__ == "__main__":
    main()
