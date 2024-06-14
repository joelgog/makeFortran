def read_file_and_store_words(filename):
    words = []  # Initialize an empty list to store words

    try:
        with open(filename, 'r') as file:
            # Read the entire content of the file
            content = file.read()

            # Split the content into words based on whitespace (space, tab, newline)
            words = content.split()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return words

# Example usage:
if __name__ == "__main__":
    print("Start")
    filename = 'sample.txt'  # Replace with your file name
    word_array = read_file_and_store_words(filename)

    # Print the array of words
    print("Array of words:", word_array)
