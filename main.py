import re


def cut_tokens(oneline):
    # Output list to store tokens
    tokens = []

    # Regular expressions for each token type
    token_patterns = {

        'Keywords': r'if|else|int|float',
        'Operators': r'[=+>*]',
        'Separators': r'[():;"]',
        'Identifiers': r'^[a-zA-Z]+\d*$',
        'Int_literal': r'^[+-]?\d+$',
        'Float_literal': r'^[+-]?\d*\.\d+$',
        'String_literal': r'[a-zA-Z]+',

    }

    words = oneline.split()
    print(words)
    # Iterate through each pattern
    # for pattern, token_type in token_patterns.items():
    #     # Find all matches in the line
    #     matches = re.findall(pattern, oneline)
    #     # Add matches to the tokens list
    #     for match in matches:
    #         tokens.append((token_type, match))
    #         line = line.replace(match, '', 1)

    return tokens


def main():
    # Test input strings
    inputs = [
        "int    A1=5",
        "float BBB2     =1034.2",
        "float     cresult     =     A1     +BBB2     *      BBB2",
        "if     (cresult     >10):",
        'print("TinyPie    ")'
    ]

    # Test the function with each input
    for input_str in inputs:
        print("Test input string:", input_str)
        print("Output <type, token> list:", cut_tokens(input_str))


if __name__ == '__main__':
    main()
