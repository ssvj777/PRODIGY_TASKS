def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - vijaord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
   while True:
       message = input("Enter the Message: ")
       shift = int(input("Enter the Shift Value: "))
       choice = input("Enter 'e' for Encryption or 'd' for Decryption: ")
       if choice.lower() == 'e':
          encrypt_message = encrypt(message, shift)
          print(f"Encrypted Message for {message} is {encrypt_message}")
       elif choice.lower() == 'd':
          decrypt_message = decrypt(message, shift)
          print(f"Decrypted Message for {message} is {decrypt_message}")
       else:
          print("Invalid choice!")

       exit_choice = input("Do you want to exit? (y/n): ")
       if exit_choice == 'y':
          break
main()
        

       
