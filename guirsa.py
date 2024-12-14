from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import tkinter as tk
from tkinter import messagebox

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def save_key_to_file(key_data, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key_data)

def generate_keys():
    private_key_client1, public_key_client1 = generate_rsa_key_pair()
    private_key_client2, public_key_client2 = generate_rsa_key_pair()
    private_key_client3, public_key_client3 = generate_rsa_key_pair()

    save_key_to_file(private_key_client1, 'client1_private_key.pem')
    save_key_to_file(public_key_client1, 'client1_public_key.pem')

    save_key_to_file(private_key_client2, 'client2_private_key.pem')
    save_key_to_file(public_key_client2, 'client2_public_key.pem')

    save_key_to_file(private_key_client3, 'client3_private_key.pem')
    save_key_to_file(public_key_client3, 'client3_public_key.pem')

    messagebox.showinfo("Success", "Keys generated and saved!")


window = tk.Tk()
window.title("RSA Key Generation")

tk.Button(window, text="Generate Keys", command=generate_keys).pack(pady=20)

window.mainloop()
