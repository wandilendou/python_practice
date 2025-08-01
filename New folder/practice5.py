def main():
    # Original list of words
    words = ["apple", "banana", "kiwi", "orange", "grape", "mango", "pear"]

    # Use list comprehension to filter words with an odd number of characters
    odd_length_words = [word for word in words if len(word) % 2 != 0]

    # Display the result
    print("Original words:", words)
    print("Words with odd number of characters:", odd_length_words)

# Run the program
if __name__ == "__main__":
    main()
