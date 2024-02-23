import re

def CutOneLineTokens(line):
    output = []
    line = line.strip()  # Remove leading and trailing whitespace
    
    # Regular expressions for tokens
    keyword_pattern = r'(?P<keyword>if|else|int|float)\b'
    operator_pattern = r'(?P<operator>=|\+|>|\*)'
    separator_pattern = r'(?P<separator>\(|\)|:|;)'
    identifier_pattern = r'(?P<identifier>[a-zA-Z]+[0-9]*)|\b(?P<single_char>[a-zA-Z])\b'
    float_literal_pattern = r'(?P<float_literal>\d+\.\d+)'
    int_literal_pattern = r'(?P<int_literal>\d+)'
    string_literal_pattern = r'(?P<string_literal>"([^"]*)")'
    
    # Combine all patterns
    combined_pattern = '|'.join([keyword_pattern, operator_pattern, separator_pattern,
                                 identifier_pattern, float_literal_pattern,
                                 int_literal_pattern, string_literal_pattern])
    
    # Tokenize the line
    for match in re.finditer(combined_pattern, line):
        for name, value in match.groupdict().items():
            if value is not None:
                output.append("<{}, {}>".format(name, value))
                break  # Break loop after appending the matched token
    
    return output

# Test cases
test_cases = [
    "int A1=5",
    "float BBB2 =1034.2",
    "float cresult = A1 +BBB2 * BBB2",
    'if (cresult >10):',
    'print("TinyPie ")'
]

# Iterate through test cases
for i, test_case in enumerate(test_cases, start=1):
    print("Test Case", i)
    print("Test input string:", test_case)
    try:
        tokens = CutOneLineTokens(test_case)
        print("Output <type, token> list:\n\n", tokens)
    except ValueError as e:
        print("Error:", e)
    print()




