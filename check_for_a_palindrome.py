import string
def reverse_string(s:str):
    """Return the reverse of the input string s."""
    return s[::-1]
def check_for_palindrome(s:str) -> bool:
    """Check if the input string s is a palindrome."""
    cleaned_s = s.strip().translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    reversed_s = reverse_string(cleaned_s)
    return cleaned_s == reversed_s
input_string = input("Enter a string to check for palindrome: ")
is_palindrome = check_for_palindrome(input_string) 
if is_palindrome:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.') 