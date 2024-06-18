import re

#Formats the list of tokens into a string with new lines and '&' at the end of each line
def format_output(tokens, max_elements_per_line=50):
    lines = []
    i = 0
    
    while i < len(tokens):
        # Determine the end index of the current line
        end_index = min(i + max_elements_per_line, len(tokens))
        
        # Check if the last token in the line chunk is '*' or '**'
        if tokens[end_index - 1] == '*' or tokens[end_index - 1] == '**':
            end_index += 1
        
        # Create the current line by joining tokens
        line = ''.join(tokens[i:end_index])
        
        # Check if we need to add '&' at the end of the current line
        if end_index < len(tokens):
            # Check the first token of the next line
            next_line_start_token = tokens[end_index]
            
            # Avoid breaking lines just before or after '* ' or '**'
            if next_line_start_token == '*' or next_line_start_token == '**':
                # Move the end_index to the beginning of the next token
                end_index += 1
                line = ''.join(tokens[i:end_index])
        
        # Add '&' at the end of the current line, unless it's the last line
        if end_index < len(tokens):
            line += ' &'
        
        # Append the formatted line to the lines list
        lines.append(line)
        
        # Move to the next chunk of tokens
        i = end_index
    
    # Join lines with newline character
    result_string = '\n'.join(lines)
    
    return result_string

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
    patternlist = [['SMP', 'm', 'e',], ['SMP', 'm', 'tau'], ['^'], ['Momentum'], ['Alpha'], ['Re', 'X', 'ScalarC0IR6', 's', 'me', 'me'], ['Im', 'X', 'DiscB', 's', 'me', 'me'], ['Eps', 'p2', 'q1', 'q2', 'sp1'], ['Eps', 'p2', 'q1', 'q2', 'sp2'], ['Eps', 'p2', 'q1', 'q2', 'sq1'], ['Eps', 'p2', 'q1', 'q2', 'sq2'],
                  ['Eps', 'p2', 'q1', 'sp1', 'sp2'], ['Eps', 'p2', 'q1', 'sp1', 'sq1'], ['Eps', 'p2', 'q1', 'sp1', 'sq2'], ['Eps', 'p2', 'q1', 'sp2', 'sq1'], ['Eps', 'p2', 'q1', 'sp2', 'sq2'], ['Eps', 'p2', 'q1', 'sq1', 'sq2'], ['Eps', 'p2', 'q2', 'sp1', 'sp2'], ['Eps', 'p2', 'q2', 'sp1', 'sq1'], 
                  ['Eps', 'p2', 'q2', 'sp1', 'sq2'], ['Eps', 'p2', 'q2', 'sp2', 'sq1'], ['Eps', 'p2', 'q2', 'sp2', 'sq2'], ['Eps', 'p2', 'q2', 'sq1', 'sq2'], ['Eps', 'q1', 'q2', 'sp1', 'sp2'], ['Eps', 'q1', 'q2', 'sp1', 'sq1'], 
                  ['Eps', 'q1', 'q2', 'sp1', 'sq2'], ['Eps', 'q1', 'q2', 'sp2', 'sq1'], ['Eps', 'q1', 'q2', 'sp2', 'sq2'], ['Eps', 'q1', 'q2', 'sq1', 'sq2'], ['Eps', 'p2', 'sp1', 'sp2', 'sq1'], ['Eps', 'p2', 'sp1', 'sp2', 'sq2'], ['Eps', 'p2', 'sp1', 'sq1', 'sq2'], ['Eps', 'p2', 'sp2', 'sq1', 'sq2'], 
                  ['Eps', 'q1', 'sp1', 'sp2', 'sq1'], ['Eps', 'q1', 'sp1', 'sp2', 'sq2'], ['Eps', 'q1', 'sp1', 'sq1', 'sq2'], ['Eps', 'q1', 'sp2', 'sq1', 'sq2'], ['Eps', 'q2', 'sp1', 'sp2', 'sq1'], ['Eps', 'q2', 'sp1', 'sp2', 'sq2'], ['Eps', 'q2', 'sp1', 'sq1', 'sq2'], ['Eps', 'q2', 'sp2', 'sq1', 'sq2'], 
                  ['Eps', 'sp1', 'sp2', 'sq1', 'sq2'], ['Re', 'X', 'DiscB', 's', 'me', 'me'], ['Pi'], ['Epsilon'], ['PaXKallenLambda', 't', 'me', '**', '2', 'mt', '**', '2'], ['Log', 'mt', '**', '2', '/', 's'], ['Log', 'me', '**', '2', '/', 's'], ['Log', 'me', '**', '2', '/', 'mt', '**', '2'],
                  ['Log', 'ScaleMu', '**', '2', '/', 'mt', '**', '2'], ['Log', 'ScaleMu', '**', '2', '/', 'me', '**', '2'], ['Re', 'X', 'ScalarC0IR6', 't', 'me', 'mt'], ['Re', 'X', 'ScalarC0', 's', 'me', '**', '2', 'me', '**', '2', '0', '0', 'me'], 
                  ['Im', 'X', 'ScalarC0', 's', 'me', '**', '2', 'me', '**', '2', '0', '0', 'me'], ['Re', 'X', 'ScalarC0', 's', 'mt', '**', '2', 'mt', '**', '2', '0', '0', 'mt'], ['Im', 'X', 'ScalarC0', 's', 'mt', '**', '2', 'mt', '**', '2', '0', '0', 'mt'], ['PaXKallenLambda', '-', 's', '-', 't', '+', '2', '*', 'me', '**', '2', '+', '2', '*', 'mt', '**', '2', 'me', '**', '2', 'mt', '**', '2'], ['PaXKallenLambda', 'me', '**', '2', 'mt', '**', '2', '-', 's', '-', 't', '+', '2', '*', 'me', '**', '2', '+', '2', '*', 'mt', '**', '2'], ['s'], ['t']]
    replacementlist = [['me'], ['mt'], ['**'], [], ['alpha'], ['scalarc0ir6se'], ['discbseIm'], ['asym234n1'], ['asym234n2'], ['asym234n3'], ['asym234n4'], ['asym23n1n2'], ['asym23n1n3'], ['asym23n1n4'], ['asym23n2n3'], ['asym23n2n4'], ['asym23n3n4'], ['asym24n1n2'], ['asym24n1n3'], ['asym24n1n4'], ['asym24n2n3'],
                      ['asym24n2n4'], ['asym24n3n4'], ['asym34n1n2'], ['asym34n1n3'], ['asym34n1n4'], ['asym34n2n3'],
                      ['asym34n2n4'], ['asym34n3n4'],['asym2n1n2n3'], ['asym2n1n2n4'], ['asym2n1n3n4'], ['asym2n2n3n4'], ['asym3n1n2n3'], ['asym3n1n2n4'], ['asym3n1n3n4'], ['asym3n2n3n4'], ['asym4n1n2n3'], ['asym4n1n2n4'], ['asym4n1n3n4'], ['asym4n2n3n4'], ['asymn1n2n3n4'], ['discbse'],
                      ['pi'], ['sing'], ['me**4 - 2*me**2*(mt**2+t) + (mt**2 - t)**2'], ['logst'], ['logse'], ['logte'], ['logtm'], ['logem'], ['scalarc0ir6tte'], ['scalarc0se'], ['scalarc0seIm'], ['scalarc0st'], ['scalarc0stIm'], ['me**4 - 2*me**2(mt**2+s+t) + (s+t-mt**2)**2'], ['me**4 - 2*me**2(mt**2+s+t) + (s+t-mt**2)**2'], ['ss'], ['tt']]

    for i in range(len(patternlist)):
        lst = replace_pattern(lst, patternlist[i], replacementlist[i])

def tokenize_expression(expression):
    # Regular expression to match alphanumeric sequences or specific characters
    token_pattern = r'[a-zA-Z0-9]+|[+\-*\/()^]'
    tokens = re.findall(token_pattern, expression)
    replace_all_patterns(tokens)
    # List to store tokens with necessary '*' insertions
    #corrected_tokens = []

    #Old code which inserted '*' manually
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
    print("Please specify input file name:")
    textfile = input()
    filename = './Virtual/' + textfile + '.txt'
    word_array = read_file_and_store_words(filename)
    tokens = tokenize_expression(word_array)

    # Print the array of words
    print("Fortran Code:", format_output(tokens))
