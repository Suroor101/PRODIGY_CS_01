import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def perform_action():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    
    mode = mode_var.get()
    result = caesar_cipher(message, shift, mode)
    result_label.config(text=f"Result: {result}", fg="#333333")
    copy_button.config(state=tk.NORMAL)

def clear_fields():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    result_label.config(text="Result: ", fg="#666666")
    copy_button.config(state=tk.DISABLED)

def copy_to_clipboard():
    result_text = result_label.cget("text")[8:]  # Extract text after "Result: "
    window.clipboard_clear()
    window.clipboard_append(result_text)
    status_label.config(text="Copied to clipboard!", fg="#4CAF50")

# Set up the main window
window = tk.Tk()
window.title("Enhanced Caesar Cipher")
window.geometry("450x400")
window.configure(bg="#f0f0f3")

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Title Label
title_label = tk.Label(window, text="Caesar Cipher Tool", font=("Helvetica", 18, "bold"), bg="#f0f0f3", fg="#2E86C1")
title_label.grid(row=0, column=0, columnspan=3, pady=(15, 25))

# Message input
tk.Label(window, text="Enter your message:", bg="#f0f0f3", fg="#333333", font=("Helvetica", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_message = tk.Entry(window, width=35, font=("Helvetica", 10))
entry_message.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Shift input
tk.Label(window, text="Enter shift value:", bg="#f0f0f3", fg="#333333", font=("Helvetica", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_shift = tk.Entry(window, width=15, font=("Helvetica", 10))
entry_shift.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Mode selection
mode_var = tk.StringVar(value="encrypt")
tk.Radiobutton(window, text="Encrypt", variable=mode_var, value="encrypt", bg="#f0f0f3", fg="#333333", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Decrypt", variable=mode_var, value="decrypt", bg="#f0f0f3", fg="#333333", font=("Helvetica", 10)).grid(row=3, column=1, padx=10, pady=5)

# Action buttons
action_button = tk.Button(window, text="Submit", command=perform_action, bg="#2E86C1", fg="white", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
action_button.grid(row=4, column=0, pady=(15, 20), padx=5)
clear_button = tk.Button(window, text="Clear", command=clear_fields, bg="#E74C3C", fg="white", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
clear_button.grid(row=4, column=1, pady=(15, 20), padx=5)

# Copy button
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard, bg="#1ABC9C", fg="white", font=("Helvetica", 10, "bold"), relief="flat", padx=10, pady=5)
copy_button.grid(row=4, column=2, pady=(15, 20), padx=5)
copy_button.config(state=tk.DISABLED)

# Result display
result_label = tk.Label(window, text="Result: ", font=("Helvetica", 12), bg="#f0f0f3", fg="#666666")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

# Status display
status_label = tk.Label(window, text="", font=("Helvetica", 10, "italic"), bg="#f0f0f3", fg="#666666")
status_label.grid(row=6, column=0, columnspan=3, pady=10)

window.mainloop()
