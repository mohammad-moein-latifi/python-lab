def encode(text, k):
    encoded_text = ""

    for char in text:
        if char.isupper():
            start = ord("A")
            new_char = chr((ord(char) - start + k) % 26 + start)

        elif char.islower():
            start = ord("a")
            new_char = chr((ord(char) - start + k) % 26 + start)

        else:
            new_char = char

        encoded_text += new_char

    return encoded_text


def decode(text, k):
    decoded_text = ""

    for char in text:
        if char.isupper():
            start = ord("A")
            new_char = chr((ord(char) - start - k) % 26 + start)

        elif char.islower():
            start = ord("a")
            new_char = chr((ord(char) - start - k) % 26 + start)

        else:
            new_char = char

        decoded_text += new_char

    return decoded_text


def main():
    print("Welcome to Caesar Cipher!")
    print("What would you like to do today?")
    print("1. Encode a message")
    print("2. Decode a message")

    choice = input("\nChoose an option (1 or 2): ").strip()

    if choice not in ("1", "2"):
        print("Invalid option! Please choose 1 or 2.")
        return

    text = input("\nEnter your message: ")

    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return

    if choice == "1":
        result = encode(text, shift)
        print("\nYour message has been encoded successfully!")
        print("Encoded message:", result)

    else:
        result = decode(text, shift)
        print("\nYour message has been decoded successfully!")
        print("Decoded message:", result)


if __name__ == "__main__":
    main()
