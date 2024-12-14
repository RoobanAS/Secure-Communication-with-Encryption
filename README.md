# Secure Communication with MQTT and RSA Encryption

This project implements a secure messaging application that integrates **MQTT** for real-time communication and **RSA encryption** to ensure the privacy and security of messages. The application includes a user-friendly graphical interface (GUI) to facilitate secure communication between multiple clients.

## Features
- **End-to-End Encryption**: Ensures secure message delivery using RSA encryption.
- **Real-Time Communication**: Utilizes the MQTT protocol for fast and efficient message delivery.
- **RSA Key Management**:
  - Each client generates its own RSA key pair.
  - Private keys are stored locally for enhanced security.
  - Public keys are shared with other clients for encrypted communication.
- **Graphical User Interface (GUI)**:
  - Allows users to generate RSA keys, send encrypted messages, and receive/decrypt incoming messages.
  - Displays chat history for each client.
- **Error Handling**: Includes validation for message delivery and recipient errors.

## Technologies Used
- **Programming Language**: Python
- **Messaging Protocol**: MQTT (with `paho-mqtt` library)
- **Encryption**: RSA (with the `cryptography` package)
- **GUI Framework**: Tkinter for cross-platform graphical user interfaces.

## How It Works
1. **Key Generation**:
   - Each client generates its own RSA key pair.
   - Public keys are exchanged among clients.
2. **Message Encryption**:
   - Messages are encrypted using the recipient's public key.
   - Only the recipient can decrypt the message with their private key.
3. **Message Transmission**:
   - Messages are sent over MQTT topics.
   - Each client subscribes to its designated topic to receive messages.
4. **Message Decryption**:
   - Received messages are decrypted using the recipient's private key.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/username/secure-mqtt-rsa
   cd secure-mqtt-rsa
Install required dependencies:
**pip install paho-mqtt cryptography

Run the application:

python client1.py
python client2.py
python client3.py
python rsakey.py
python display.py


Future Enhancements
Add support for secure file sharing between clients.
Introduce multi-factor authentication (MFA) for additional security.
Expand the project to include voice and video communication.

Screenshots
(Include relevant screenshots of the GUI and message flow here)
![Screenshot 2024-10-03 222502](https://github.com/user-attachments/assets/d080a52b-594d-4468-adf0-4d78d3c57996)
