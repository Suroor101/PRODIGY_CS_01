import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode="encrypt"):
    """Encrypt or decrypt the input text using the Caesar cipher algorithm."""
    result = ""
    # Adjust the shift for decryption
    if mode == "decrypt":
        shift = -shift
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetical characters remain unchanged
    return result

def perform_action():
    """Get user input and perform encryption or decryption."""
    message = entry_message.get()  # Get the input message from the entry box
    try:
        shift = int(entry_shift.get())  # Get the shift value and convert it to an integer
    except ValueError:
        # Show an error message if the shift value is invalid
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    
    mode = mode_var.get()  # Get the selected mode (encrypt/decrypt)
    result = caesar_cipher(message, shift, mode)  # Perform the cipher operation
    result_label.config(text=f"Result: {result}", fg="#333333")  # Display the result
    copy_button.config(state=tk.NORMAL)  # Enable the copy button

def clear_fields():
    """Clear the input fields and reset the result display."""
    entry_message.delete(0, tk.END)  # Clear the message input field
    entry_shift.delete(0, tk.END)  # Clear the shift value input field
    result_label.config(text="Result: ", fg="#666666")  # Reset the result label
    copy_button.config(state=tk.DISABLED)  # Disable the copy button

def copy_to_clipboard():
    """Copy the result text to the clipboard."""
    result_text = result_label.cget("text")[8:]  # Extract text after "Result: "
    window.clipboard_clear()  # Clear the clipboard
    window.clipboard_append(result_text)  # Append the result text to the clipboard
    status_label.config(text="Copied to clipboard!", fg="#4CAF50")  # Update the status label

# Set up the main window
window = tk.Tk()  # Create the main application window
window.title("Enhanced Caesar Cipher")  # Set the window title
window.geometry("450x400")  # Set the window size
window.configure(bg="#f0f0f3")  # Set the background color

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Title Label
title_label = tk.Label(window, text="Caesar Cipher Tool", font=("Helvetica", 18, "bold"), bg="#f0f0f3", fg="#2E86C1")
title_label.grid(row=0, column=0, columnspan=3, pady=(15, 25))  # Position the title label

# Message input
tk.Label(window, text="Enter your message:", bg="#f0f0f3", fg="#333333", font=("Helvetica", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_message = tk.Entry(window, width=35, font=("Helvetica", 10))  # Input field for the message
entry_message.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Shift input
tk.Label(window, text="Enter shift value:", bg="#f0f0f3", fg="#333333", font=("Helvetica", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_shift = tk.Entry(window, width=15, font=("Helvetica", 10))  # Input field for the shift value
entry_shift.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Mode selection (Encrypt/Decrypt)
mode_var = tk.StringVar(value="encrypt")  # Set default mode to encrypt
tk.Radiobutton(window, text="Encrypt", variable=mode_var, value="encrypt", bg="#f0f0f3", fg="#333333", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Decrypt", variable=mode_var, value="decrypt", bg="#f0f0f3", fg="#333333", font=("Helvetica", 10)).grid(row=3, column=1, padx=10, pady=5)

# Action buttons
action_button = tk.Button(window, text="Submit", command=perform_action, bg="#2E86C1", fg="white", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
action_button.grid(row=4, column=0, pady=(15, 20), padx=5)  # Submit button
clear_button = tk.Button(window, text="Clear", command=clear_fields, bg="#E74C3C", fg="white", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
clear_button.grid(row=4, column=1, pady=(15, 20), padx=5)  # Clear button

# Copy button
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard, bg="#1ABC9C", fg="white", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
copy_button.grid(row=4, column=2, pady=(15, 20), padx=5)  # Copy button
copy_button.config(state=tk.DISABLED)  # Initially disable the copy button

# Result display
result_label = tk.Label(window, text="Result: ", font=("Helvetica", 12), bg="#f0f0f3", fg="#666666")  # Label for displaying results
result_label.grid(row=5, column=0, columnspan=3, pady=10)

# Status display
status_label = tk.Label(window, text="", font=("Helvetica", 10, "italic"), bg="#f0f0f3", fg="#666666")  # Label for displaying status messages
status_label.grid(row=6, column=0, columnspan=3, pady=10)

# Start the GUI event loop
window.mainloop()
