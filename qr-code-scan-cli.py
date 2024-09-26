import sys
import cv2
from pyzbar import pyzbar
import pathlib

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python qr-code-scan-cli.py \"path\"")
            sys.exit(1)

        image_path = sys.argv[1]

        if not pathlib.Path(image_path).is_file():
            raise Exception(f"{image_path} is not a file")

        # Load the image
        image = cv2.imread(image_path)
        
        # Decode the QR code
        decoded_objects = pyzbar.decode(image)
        
        # Extract and print the decoded data
        for obj in decoded_objects:
            print(f"Type: {obj.type}")
            print(f"Data: {obj.data.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")