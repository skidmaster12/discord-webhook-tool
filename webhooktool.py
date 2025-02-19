import tkinter as tk
import requests
import threading
import time

# Define the Webhook URL
WEBHOOK_URL = 'your webhook here'

spamming = False  # Control variable for spam feature

# Function to send a message to the webhook
def send_message():
    message = message_entry.get()
    if message:
        data = {"content": message}
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            status_label.config(text="Message sent successfully!", fg="green")
        else:
            status_label.config(text=f"Failed to send message: {response.status_code}", fg="red")
    else:
        status_label.config(text="Please enter a message.", fg="red")

# Function to update webhook profile picture
def change_pfp():
    avatar_url = avatar_entry.get()
    if avatar_url:
        data = {"avatar": avatar_url}
        response = requests.patch(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            status_label.config(text="Webhook avatar updated!", fg="green")
        else:
            status_label.config(text=f"Failed to update avatar: {response.status_code}", fg="red")
    else:
        status_label.config(text="Please enter an avatar URL.", fg="red")

# Function to start spamming messages
def start_spam():
    global spamming
    spamming = True
    def spam():
        while spamming:
            send_message()
            time.sleep(0.1)  # 0.1 second interval
    threading.Thread(target=spam, daemon=True).start()

# Function to stop spamming messages
def stop_spam():
    global spamming
    spamming = False
    status_label.config(text="Spamming stopped.", fg="blue")

# Create the main window
root = tk.Tk()
root.title("Webhook Messenger")

# Message input field
message_label = tk.Label(root, text="Enter message:")
message_label.pack(padx=10, pady=5)

message_entry = tk.Entry(root, width=50)
message_entry.pack(padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack(padx=10, pady=5)

# Spam button
spam_button = tk.Button(root, text="Start Spamming", command=start_spam, fg="white", bg="red")
spam_button.pack(padx=10, pady=5)

# Stop spam button
stop_button = tk.Button(root, text="Stop Spamming", command=stop_spam, fg="white", bg="blue")
stop_button.pack(padx=10, pady=5)

# Avatar URL input
avatar_label = tk.Label(root, text="Enter new avatar URL:")
avatar_label.pack(padx=10, pady=5)

avatar_entry = tk.Entry(root, width=50)
avatar_entry.pack(padx=10, pady=5)

# Change PFP button
pfp_button = tk.Button(root, text="Change Avatar", command=change_pfp)
pfp_button.pack(padx=10, pady=5)

# Status label
status_label = tk.Label(root, text="", fg="black")
status_label.pack(padx=10, pady=10)


# Run the main loop
root.mainloop()

