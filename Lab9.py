# Juan Sanchez
# Encoder function
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shift each digit up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password

# Decoder function
# Christian Villa
def decode(s):
    # Takes string s
    t = ""
    for i in range(0, len(s)):
        x = int(s[i])
        #using -3 = 7 mod 10
        x = (x + 7) % 10
        t += str(x)
    return t
# Main function
def main():
    encoded_password = ""
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
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
