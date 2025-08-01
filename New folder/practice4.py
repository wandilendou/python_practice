def main():
    print("Enter integers for Set 1 (separated by spaces):")
    set1_input = input(">> ")
    set1 = set(map(int, set1_input.split()))

    print("\nEnter integers for Set 2 (separated by spaces):")
    set2_input = input(">> ")
    set2 = set(map(int, set2_input.split()))

    # Find the intersection of the two sets
    common_elements = set1 & set2

    print("\nSet 1:", set1)
    print("Set 2:", set2)
    print("Common elements:", common_elements)

# Run the program
if __name__ == "__main__":
    main()
