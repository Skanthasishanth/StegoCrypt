## Title of the Project
StegoCrypt is a dual-layer security tool that combines cryptography and steganography to protect sensitive information during transmission. By encrypting data and hiding it within digital media, such as images or audio files, StegoCrypt ensures both data confidentiality and concealment.

## About
StegoCrypt is a secure communication tool that integrates cryptography and steganography to provide dual-layer protection for sensitive data during transmission. This system ensures that data is both encrypted (using cryptographic techniques) and concealed (using steganographic methods) within digital media files such as images or audio. The goal of StegoCrypt is to prevent unauthorized access and minimize the risk of data detection and interception by attackers. This project uses MATLAB for implementing and simulating encryption algorithms, embedding methods, and performance testing.

## Features
- Dual-Layer Security: Combines cryptography (for encryption) and steganography (for data concealment) to enhance security.
- Symmetric and Asymmetric Encryption Options: Users can choose between symmetric encryption (AES) or asymmetric encryption (RSA) for encrypting data before embedding.
- Least Significant Bit (LSB) Steganography: Implements LSB-based embedding, which modifies the least significant bits of pixels or audio samples, making data insertion nearly imperceptible.
- Performance Optimization: MATLAB-based optimization of cryptographic and steganographic algorithms to balance security with speed and efficiency.
- User-Friendly Interface: Provides a MATLAB GUI that simplifies the encryption, embedding, extraction, and decryption processes for users.
- Robustness Against Detection: Resistant to steganalysis and cryptanalysis, making it suitable for high-risk data environments.

## Requirements
- MATLAB (latest version): For algorithm implementation, testing, and GUI development.
- Image Processing Toolbox: Essential for performing operations on images, particularly for LSB embedding and extraction.
- Signal Processing Toolbox: Useful for audio steganography, where data can be embedded within audio signals.
- Cryptography Package: For implementing AES and RSA encryption algorithms within MATLAB.
- Computer Requirements: Minimum 4GB RAM, 2 GHz processor, and 10GB disk space for smooth MATLAB operation.
- Compatible File Formats: Supports PNG, JPEG (for image steganography), and WAV, MP3 (for audio steganography).

## System Architecture
![SystemArc](https://github.com/user-attachments/assets/9147f35e-f440-42ef-8d1c-67d46f88a228)

## Output

#### Output 1 
![op1](https://github.com/user-attachments/assets/3eb214d5-6d85-4b57-acbe-cfe64aeecea8)

#### Output 2
![op2](https://github.com/user-attachments/assets/6445b733-b844-4e15-9de5-c5c19b20b233)

Detection Accuracy:
- Steganography Accuracy: The system is optimized to minimize detectable alterations, ensuring the embedded data remains invisible to human eyes and detection tools. MATLAB simulations test against common steganalysis techniques.
- Cryptography Accuracy: Encryption algorithms are tested to maintain integrity and consistency in data encryption and decryption. MATLAB helps verify that encrypted data accurately matches the decrypted output, ensuring robustness against decryption errors.


## Results and Impact
- Enhanced Security: Dual-layer security significantly reduces risks associated with data transmission, making StegoCrypt suitable for high-stakes environments like military, finance, and corporate data security.
- MATLAB-Driven Efficiency: Using MATLAB for optimization results in efficient processing times and minimal computational load, even with large data sets.
- User Adoption: The MATLAB GUI makes StegoCrypt accessible, encouraging adoption in non-technical environments.
- Real-World Applications: Suitable for secure data sharing in industries where information security is critical. This includes secure communication of financial records, healthcare data, and sensitive corporate information.

## Articles published / References
1. Gupta, S. S., & Gupta, P. K. (2018). "An Overview of Cryptography and Steganography Techniques." International Journal of Computer Science and Engineering.

2. Mallik, R., Krishna, P., & Rao, P. S. (2016). "An Efficient and Secure Data Transmission Based on Cryptography and Steganography." ResearchGate.

3. Pawar, B., & Shinde, G. (2019). "A Review on Combined Approach of Steganography and Cryptography." ResearchGate.

4. Sahu, S. K., & Sahu, A. K. (2015). "A Survey of Image Steganography Techniques." International Journal of Computer Applications.

5. Kaur, A. B., & Kaur, H. (2016). "Digital Image Steganography: A Review." International Journal of Computer Applications.

6. Sharma, A., & Kumari, P. (2019). "Steganography: A Review of the Techniques and Applications." ResearchGate.

7. Acharya, M. V., Kittur, H. M., & Mehtre, S. M. (2020). "Enhanced Security Using Cryptography and Steganography Techniques: A Review." International Journal of Engineering Research and Technology.

8. Shaikh, A., Patil, M., & Shah, A. (2019). "Hybrid Cryptography and Steganography Approach for Secure Data Communication." International Journal of Recent Technology and Engineering.
