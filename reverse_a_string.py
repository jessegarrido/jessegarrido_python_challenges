import string
def reverse_string(s:str):
    """Return the reverse of the input string s."""
    # return s[::-1]
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
cleaned_reversed_string = reversed_string.strip().translate(str.maketrans('','',string.punctuation))  
print("Cleaned and Reversed string:", cleaned_reversed_string)