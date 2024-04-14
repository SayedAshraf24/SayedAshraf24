def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift_amount) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - shift_amount) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ")
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (an integer): "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (an integer): "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
