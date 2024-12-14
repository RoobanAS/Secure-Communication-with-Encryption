import paho.mqtt.client as mqtt
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Display Client connected successfully")
      
        client.subscribe("topic/client1")
        client.subscribe("topic/client2")
        client.subscribe("topic/client3")
    else:
        print(f"Failed to connect with result code {rc}")

def on_message(client, userdata, msg):
    
    display_box.insert(tk.END, f"Encrypted message received on {msg.topic}:\n{msg.payload.hex()}\n\n")

display_client = mqtt.Client("display_client")
display_client.on_connect = on_connect
display_client.on_message = on_message


window = tk.Tk()
window.title("Display Client")


display_box = ScrolledText(window, width=80, height=20)
display_box.pack(pady=10)


display_client.connect("test.mosquitto.org", 1883, 60)
display_client.loop_start()

window.mainloop()

display_client.loop_stop()
display_client.disconnect()
