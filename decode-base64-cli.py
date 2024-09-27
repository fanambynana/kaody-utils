import sys
import base64

def is_base64_like(string):
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    return all(char in allowed_chars for char in string)

if __name__ == "__main__":   
    try:
        if len(sys.argv) != 2:
            print("Usage: python decode-base64-cli.py \"string\"")
            sys.exit(1)

        input_string = sys.argv[1]

        # Verify encoding
        if is_base64_like(input_string):
            # Base64-encoded string
            encoded_string = input_string
        else:
            raise Exception("String is not Base64 encoded")
        
        # Decode the Base64 string
        decoded_bytes = base64.b64decode(encoded_string)

        # Convert bytes to string (assuming UTF-8 encoding)
        decoded_string = decoded_bytes.decode('utf-8')
        
        print(f"Decoded result: {decoded_string}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")