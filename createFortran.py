import re

def tokenize_expression(expression):
    # Regular expression to match alphanumeric sequences or specific characters
    token_pattern = r'[a-zA-Z0-9]+|[+\-*\/()]'
    tokens = re.findall(token_pattern, expression)
    # List to store tokens with necessary '*' insertions
    corrected_tokens = []
    
    # Iterate through tokens to insert '*' where necessary
    for i in range(len(tokens)):
        # Add current token to corrected_tokens
        corrected_tokens.append(tokens[i])
        
        # Check if there's a need to insert '*'
        if i < len(tokens) - 1:  # Check next token
            if tokens[i] not in '+-()' and tokens[i+1] not in '+-()' and tokens[i] not in '*/' and tokens[i+1] not in '*/':
                corrected_tokens.append('*')
    
    return corrected_tokens

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

    return content

if __name__ == "__main__":
    print("Start")
    filename = 'sample.txt'  # Replace with your file name
    word_array = read_file_and_store_words(filename)
    tokens = tokenize_expression(word_array)

    

    # Print the array of words
    print("Array of words:", tokens)
