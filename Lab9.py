# Encoder function
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shift each digit up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password

# Decoder function
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)  # Shift each digit down by 3 numbers
        decoded_password += decoded_digit
    return decoded_password

# Main function
def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            encoded_password = input("Please enter the encoded password: ")
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
