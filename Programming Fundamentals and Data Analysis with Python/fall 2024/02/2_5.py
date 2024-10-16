def caesar_cipher(text):
    encrypted_text =""
    for char in text:
        if 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            encrypted_text += new_char
        elif 'a' <= char <= 'z':
                new_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text
message = input()
encrypted_message = caesar_cipher(message)
print(encrypted_message)