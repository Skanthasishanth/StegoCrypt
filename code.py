from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from PIL import Image
import base64

# AES Encryption
def encrypt_message(message, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    iv = cipher.iv
    encrypted_message = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    encrypted_data = iv + encrypted_message
    # Encode to base64 for safe storage and transmission
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_message(encrypted_message, key):
    try:
        # Decode the base64 encoded message
        data = base64.b64decode(encrypted_message)
        iv = data[:16]  # First 16 bytes are the IV
        encrypted_message = data[16:]  # Remaining part is the encrypted message

        # Debugging: print the extracted encrypted message and IV
        print(f"IV (hex): {iv.hex()}")
        print(f"Encrypted Message (hex): {encrypted_message.hex()}")

        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)
        return decrypted_message.decode('utf-8')
    except Exception as e:
        print("Error during decryption:", e)
        return None

# LSB Steganography
def encode_image(image_path, data, output_path):
    image = Image.open(image_path)
    binary_data = ''.join(format(ord(i), '08b') for i in data) + '1111111111111110'  # End delimiter
    data_len = len(binary_data)
    pixels = image.load()

    idx = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = list(pixels[i, j])
            for k in range(3):  # RGB channels
                if idx < data_len:
                    pixel[k] = pixel[k] & ~1 | int(binary_data[idx])
                    idx += 1
            pixels[i, j] = tuple(pixel)
            if idx >= data_len:
                break

    image.save(output_path)
    print(f"Data encoded into {output_path}")

def decode_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    binary_data = ""

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            for k in range(3):  # RGB channels
                binary_data += str(pixel[k] & 1)

    # Split into bytes and clean up the binary data based on the delimiter
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        if byte == "11111110":  # End delimiter (this marks the end of embedded data)
            break
        decoded_data += chr(int(byte, 2))

    # Clean up the decoded string and remove non-ASCII characters (e.g., `ÿ`)
    decoded_data = decoded_data.strip()
    # Remove any invalid characters from the base64 string
    decoded_data = decoded_data.split('ÿ')[0]

    return decoded_data

# Main Program
if __name__ == "__main__":
    print("1. Encrypt and Encode\n2. Decode and Decrypt")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Encrypt and Encode
        message = input("Enter the message to encrypt: ")
        key = input("Enter a 16-byte key: ")
        if len(key) != 16:
            print("Key must be exactly 16 bytes!")
            exit()
        encrypted_message = encrypt_message(message, key)
        print(f"Encrypted Message (base64): {encrypted_message}")

        image_path = input("Enter the path of the image (e.g., input.png): ")
        output_path = "encoded_image.png"
        encode_image(image_path, encrypted_message, output_path)

    elif choice == "2":
        # Decode and Decrypt
        image_path = input("Enter the path of the encoded image (e.g., encoded_image.png): ")
        key = input("Enter the 16-byte key: ")
        if len(key) != 16:
            print("Key must be exactly 16 bytes!")
            exit()
        encrypted_message = decode_image(image_path)
        print(f"Encoded Encrypted Message (extracted): {encrypted_message}")

        try:
            decrypted_message = decrypt_message(encrypted_message, key)
            if decrypted_message:
                print(f"Decrypted Message: {decrypted_message}")
            else:
                print("Decryption failed.")
        except Exception as e:
            print("Failed to decrypt message. Check the key or image.")
            print("Error:", e)

    else:
        print("Invalid choice!")
