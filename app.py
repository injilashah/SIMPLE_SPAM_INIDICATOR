import tkinter as tk
from tkinter import messagebox
from spam_indicator import SI


# Function to check for spam
def check_spam():
    message = entry.get("1.0", tk.END).lower().strip()  # Get the text input from the user
    is_spam = any(spam in message for spam in SI())
    
    if is_spam:
        messagebox.showwarning("Spam Alert", "Warning: The message is spam!")
    else:
        messagebox.showinfo("All Clear", "The message is not spam.")

# Create the main application window
app = tk.Tk()
app.title("Spam Indicator")
app.geometry("400x300")

# Create a text label
label = tk.Label(app, text="Enter your message below:", font=("Arial", 14))
label.pack(pady=10)

# Create a text box for user input
entry = tk.Text(app, height=10, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Create a button to check the message
check_button = tk.Button(app, text="Check Message", command=check_spam, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

# Run the application
app.mainloop()
