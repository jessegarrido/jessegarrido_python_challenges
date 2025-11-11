def caesar_cipher(text:str, shift:int) -> str:
    """Encrypt the input text using a Caesar cipher with the given shift."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result
input_text = input("Enter text to encrypt: ")
shift_value = int(input("Enter shift value: ")) 
encrypted_text = caesar_cipher(input_text, shift_value)
print("Encrypted text:", encrypted_text) 