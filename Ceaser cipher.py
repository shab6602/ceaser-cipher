# Caesar Cipher
# Encryption
def encryption(dec_data, key):
    result = ""
    for char in dec_data:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char
    return result

# Decryption
def decryption(enc_text, key):
    result = ""
    for char in enc_text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            result += char
    return result

# Main
choice = int(input("Please enter 1 for encryption and 2 for decryption: "))
if choice == 1:
    dec_text = input("Enter the text you want to encrypt: ")
    key = int(input("Enter the number of shifts: "))
    enc_data = encryption(dec_text, key)
    print("The encrypted data is: ", enc_data)
elif choice == 2:
    enc_text = input("Enter the text you want to decipher: ")
    key = int(input("Enter the number of shifts: "))
    dec_data = decryption(enc_text, key)
    print("Your decrypted data is: ", dec_data)
