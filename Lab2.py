import re
strings = ["22.11", "23", "66.7f", "123abcde", "Case44", "Happy", "78", "66.7", "yes123", "Book111"]
patterns = [
    r'^\d+\.\d+$',# Float with decimal point
    r'^\d+$',# Integer
    r'^\d+\.\d+[a-f]$',# Float with decimal point and 'f' at the end
    r'^\d+[a-z]+$',# Alphanumeric
    r'^[A-Z][a-z]+\d+$' # CamelCase
]
def test_patterns(string):
    for i, pattern in enumerate(patterns):
        if re.match(pattern, string):
            return f"{string} matches the pattern {i+1}: {pattern}"
    return f"No pattern found for {string}"
for string in strings:
    print(test_patterns(string))
def remove_integer(string):
    match = re.match(r'^(\d+)\s*(.*)', string)
    if match:
        integer = match.group(1)
        rest_of_string = match.group(2)
        return f"Found integer {integer} at the beginning of this string. The rest of the string is: {rest_of_string}"
    else:
        return "No integer found at the beginning of the string"
print(remove_integer("22 street"))
print(remove_integer("90years"))
