import re

#Replaces all occurrences of the pattern given by sublist with the desired replacement
def replace_pattern(lst, sublist, replacement):
    n, m = len(lst), len(sublist)
    
    i = 0
    while i <= n - m:
        # Check if the sublist pattern matches the slice of lst
        if lst[i:i + m] == sublist:
            # Replace the sublist with the replacement
            lst[i:i + m] = replacement
            # Adjust the length of the list
            n = len(lst)
            # Move the index forward by the length of the replacement
            i += len(replacement)
        else:
            i += 1
    return lst

#Replaces all patterns defined by patternlist with replacementlist
def replace_all_patterns(lst):
    patternlist = [['SMP', 'm', 'e',], ['SMP', 'm', 'tau'], ['^'], ['Momentum']]
    replacementlist = [['me'],['mt'], ['**'], []]

    for i in range(len(patternlist)):
        lst = replace_pattern(lst, patternlist[i], replacementlist[i])

def tokenize_expression(expression):
    # Regular expression to match alphanumeric sequences or specific characters
    token_pattern = r'[a-zA-Z0-9]+|[+\-*\/()^]'
    tokens = re.findall(token_pattern, expression)
    replace_all_patterns(tokens)
    # List to store tokens with necessary '*' insertions
    #corrected_tokens = []

    # Iterate through tokens to insert '*' where necessary
    #for i in range(len(tokens)):
        # Add current token to corrected_tokens
        #corrected_tokens.append(tokens[i])
        
        # Check if there's a need to insert '*'
        #if i < len(tokens) - 1:  # Check next token
            #if tokens[i] not in '+-()**' and tokens[i+1] not in '+-()**' and tokens[i] not in '*/' and tokens[i+1] not in '*/':
                #corrected_tokens.append('*')
    
    return tokens

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
    filename = 'sample2.txt'
    word_array = read_file_and_store_words(filename)
    tokens = tokenize_expression(word_array)

    # Print the array of words
    print("Array of words:", tokens)
