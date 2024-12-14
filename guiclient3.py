import tkinter as tk
from tkinter import scrolledtext
import paho.mqtt.client as mqtt
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Load RSA keys
with open('client3_private_key.pem', 'rb') as key_file:
    client3_private_key = serialization.load_pem_private_key(key_file.read(), password=None)

with open('client1_public_key.pem', 'rb') as key_file:
    client1_public_key = serialization.load_pem_public_key(key_file.read())

with open('client2_public_key.pem', 'rb') as key_file:
    client2_public_key = serialization.load_pem_public_key(key_file.read())

public_keys = {
    "client1": client1_public_key,
    "client2": client2_public_key,
}

# Flag to track connection status
is_connected = False  

def on_connect(client, userdata, flags, rc):
    global is_connected
    if rc == 0:
        if not is_connected:  # Log message only when connecting for the first time
            log_display.insert(tk.END, "Client 3 connected successfully\n")
            is_connected = True
        client.subscribe("topic/client3")
    else:
        log_display.insert(tk.END, f"Failed to connect with result code {rc}\n")
        is_connected = False  # Reset flag if connection fails

def on_message(client, userdata, msg):
    try:
        # Decrypt the received message using the private key
        decrypted_message = client3_private_key.decrypt(
            msg.payload,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        decoded_message = decrypted_message.decode()

        # Extract sender and message content
        sender, message_content = decoded_message.split(":", 1)
        log_display.insert(tk.END, f"Received message from {sender}: {message_content}\n")
    except Exception as e:
        log_display.insert(tk.END, f"Failed to decrypt message: {e}\n")

def send_message(event=None):
    recipient = recipient_var.get()
    if recipient not in public_keys:
        log_display.insert(tk.END, "Invalid recipient. Try again.\n")
        return

    message = message_entry.get()

    # Create message to be sent (client3: message)
    message_to_send = f"client3:{message}"

    # Encrypt message using recipient's public key
    encrypted_message = public_keys[recipient].encrypt(
        message_to_send.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Publish encrypted message
    client3.publish(f"topic/{recipient}", encrypted_message)
    log_display.insert(tk.END, f"Sent message to {recipient}\n")
    message_entry.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("Client 3")

# Recipient dropdown menu
recipient_label = tk.Label(root, text="Recipient:")
recipient_label.grid(row=0, column=0)

recipient_var = tk.StringVar(root)
recipient_var.set("client1")  # Default value
recipient_menu = tk.OptionMenu(root, recipient_var, "client1", "client2")
recipient_menu.grid(row=0, column=1)

# Message entry
message_label = tk.Label(root, text="Message:")
message_label.grid(row=1, column=0)

message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1)
message_entry.bind("<Return>", send_message)  # Bind Enter key to send message

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=2, column=1)

# Log display
log_display = scrolledtext.ScrolledText(root, width=50, height=10)
log_display.grid(row=3, column=0, columnspan=2)

# MQTT client setup
client3 = mqtt.Client("client3")
client3.on_connect = on_connect
client3.on_message = on_message
client3.connect("test.mosquitto.org", 1883, 60)
client3.loop_start()

# Tkinter main loop
root.mainloop()

# Stop MQTT loop and disconnect when closing
client3.loop_stop()
client3.disconnect()
