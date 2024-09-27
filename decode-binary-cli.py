import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python decode-binary-cli.py \"string\"")
            sys.exit(1)

        input_string = sys.argv[1]

        # Remove any spaces from the binary string
        binary_string = input_string.replace(" ", "")
        
        # Check if the length of the binary string is a multiple of 8
        if len(binary_string) % 8 != 0:
            raise ValueError("Invalid binary string. Length must be a multiple of 8.")
        
        # Split the binary string into groups of 8 bits
        byte_groups = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        
        # Convert each byte group to ASCII character and join them together
        decoded_string = ''.join(chr(int(byte_group, 2)) for byte_group in byte_groups)

        print(f"Decoded result: {decoded_string}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
