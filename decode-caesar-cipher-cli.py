import sys

def decode_string(encoded_string, shift):
    decoded_string = ""

    for char in encoded_string:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_string += decoded_char
        else:
            decoded_string += char

    return decoded_string

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python decode-caesar-cipher-cli.py \"string\"")
            sys.exit(1)

        encoded_string = sys.argv[1]
        print("Possibilities are:")
        for i in range(1, 26, 1):
            print(f"Decoded result for shift {i}: {decode_string(encoded_string, i)}")      
    except Exception as e:
        print(f"An error occurred: {str(e)}")