def caesar_cipher(text:str, shift:int) -> str:
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
decrypted_text = caesar_cipher(encrypted_text, -shift_value)
print("Decrypted text:", decrypted_text)