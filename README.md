## StegoCrypt: Integrated Cryptography and Steganography

StegoCrypt is a dual-layer security tool that combines cryptography and steganography to protect sensitive information during transmission. By encrypting data and hiding it within digital media, such as images or audio files, StegoCrypt ensures both data confidentiality and concealment.

## About

This project combines cryptography and steganography to ensure secure and hidden data transmission. Cryptography encrypts the message to protect it from unauthorized access, while steganography embeds the encrypted data within an image, concealing the very existence of the message. The dual-layered approach ensures confidentiality, integrity, and stealth in communication.

Objective: To provide a robust solution for secure data communication in environments where privacy and discretion are critical.

## Features

- AES Encryption: Implements Advanced Encryption Standard (AES) with CBC mode for secure encryption of messages.
- Image-Based Steganography: Uses the least significant bit (LSB) technique to hide encrypted messages in images without altering their appearance.
- End-to-End Security: Ensures both encryption and concealment of data, protecting against interception and suspicion.
- User-Friendly Integration: Provides easy-to-use methods for encrypting, hiding, extracting, and decrypting messages.
- Stealth Transmission: Messages are embedded in regular image files, making them indistinguishable from normal images.

## Requirements

### Software
- Python 3.8 or later
### Required libraries:
- pycryptodome for cryptographic functions
- Pillow for image processing
### Hardware
- Standard system configuration with sufficient RAM (4 GB or higher) to handle image processing tasks.
- Image files in PNG format to preserve data integrity during the embedding process.
### Key Requirements
- The encryption key must be a secure string of 16, 24, or 32 bytes.
- High-resolution images are recommended for embedding large encrypted messages.


## System Architecture

![SystemArc](https://github.com/user-attachments/assets/9147f35e-f440-42ef-8d1c-67d46f88a228)

## Output

#### Output 1 

![op1](https://github.com/user-attachments/assets/0a61f96d-d37a-4f2b-8078-3955e9f547f3)

#### Output 2

![op2](https://github.com/user-attachments/assets/342836ba-08a9-4383-8333-bb59373a53ea)

#### Output 3

![op3](https://github.com/user-attachments/assets/4d5e9a68-f24c-4bf8-80de-969b5b6c2a4d)

#### Output 4

![op4](https://github.com/user-attachments/assets/bf52e791-db3c-46a7-873e-245607109756)

#### Output 5

![op5](https://github.com/user-attachments/assets/a5455b0f-3591-4811-bb3d-c4823a79f92a)

Detection Accuracy:
- Encryption: AES encryption is mathematically secure and ensures a high level of data confidentiality.
- Steganography: The LSB technique provides a high level of imperceptibility, with no visible changes to the image.
Accuracy:
- Message extraction and decryption accuracy: 100% under ideal conditions (when the key and original image format are preserved).
- Resistance to detection: LSB embedding avoids visual artifacts, making detection by casual observers unlikely.
Limitations:
- Susceptible to advanced statistical steganalysis tools if the attacker has access to multiple altered images.


## Results and Impact

- Successful Secure Transmission: Encrypted messages were securely transmitted within image files and accurately decrypted on the receiving end.
- Minimal Image Distortion: The embedded data caused no perceptible changes to the visual quality of the images.
- Enhanced Security: The combination of encryption and steganography provided a dual layer of protection, ensuring both confidentiality and secrecy.
- Increased Data Security: Valuable for organizations and individuals requiring secure communication channels.
- Broad Applicability: Can be used in various fields such as defense, healthcare, and corporate communications.
- Awareness: Highlights the importance of combining cryptography and steganography for modern cybersecurity challenges.

## Articles published / References
1. Gupta, S. S., & Gupta, P. K. (2018). "An Overview of Cryptography and Steganography Techniques." International Journal of Computer Science and Engineering.

2. Mallik, R., Krishna, P., & Rao, P. S. (2016). "An Efficient and Secure Data Transmission Based on Cryptography and Steganography." ResearchGate.

3. Pawar, B., & Shinde, G. (2019). "A Review on Combined Approach of Steganography and Cryptography." ResearchGate.

4. Sahu, S. K., & Sahu, A. K. (2015). "A Survey of Image Steganography Techniques." International Journal of Computer Applications.

5. Kaur, A. B., & Kaur, H. (2016). "Digital Image Steganography: A Review." International Journal of Computer Applications.

6. Sharma, A., & Kumari, P. (2019). "Steganography: A Review of the Techniques and Applications." ResearchGate.

7. Acharya, M. V., Kittur, H. M., & Mehtre, S. M. (2020). "Enhanced Security Using Cryptography and Steganography Techniques: A Review." International Journal of Engineering Research and Technology.

8. Shaikh, A., Patil, M., & Shah, A. (2019). "Hybrid Cryptography and Steganography Approach for Secure Data Communication." International Journal of Recent Technology and Engineering.
