import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x400")
        self.master.config(bg="black")  # Set background color to black

        self.title_label = tk.Label(master, text="Need a Unique, Secure Password?", font=("Helvetica", 16), bg="black", fg="white")
        self.title_label.pack(pady=20)

        self.generate_button = tk.Button(master, text="Use Password Generator", command=self.show_options, bg="red", fg="white", font=("Helvetica", 14))
        self.generate_button.pack()

        self.last_selected_button = None  # To keep track of the last selected radio button

    def show_options(self):
        self.generate_button.pack_forget()
        self.title_label.pack_forget()

        self.length_label = tk.Label(self.master, text="Choose password length", font=("Helvetica", 12),bg="black",fg="white")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.length_entry.pack()

        self.strength_label = tk.Label(self.master, text="Choose password strength", font=("Helvetica", 12),bg="black",fg="white")
        self.strength_label.pack(pady=10)

        self.strength_var = tk.StringVar()
        self.strength_var.set("Weak")

        self.weak_radio = tk.Radiobutton(self.master, text="Weak", variable=self.strength_var, value="Weak", font=("Helvetica", 12),bg="black",fg="white", command=self.change_color)
        self.weak_radio.pack(pady=5)

        self.medium_radio = tk.Radiobutton(self.master, text="Medium", variable=self.strength_var, value="Medium", font=("Helvetica", 12),bg="black",fg="white", command=self.change_color)
        self.medium_radio.pack(pady=5)

        self.strong_radio = tk.Radiobutton(self.master, text="Strong", variable=self.strength_var, value="Strong", font=("Helvetica", 12),bg="black",fg="white", command=self.change_color)
        self.strong_radio.pack(pady=5)

        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password, bg="red", fg="white", font=("Helvetica", 14))
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg="black", fg="white")
        self.password_label.pack()

    def change_color(self):
        if self.last_selected_button:
            self.last_selected_button.config(bg="black", fg="white") 
        if self.strength_var.get() == "Weak":
            self.weak_radio.config(bg="blue", fg="white")  
            self.last_selected_button = self.weak_radio
        elif self.strength_var.get() == "Medium":
            self.medium_radio.config(bg="blue", fg="white")  
            self.last_selected_button = self.medium_radio
        else:
            self.strong_radio.config(bg="blue", fg="white")  
            self.last_selected_button = self.strong_radio

    def generate_password(self):
        length = self.length_entry.get()
        try:
            length = int(length)
            if length <= 0:
                messagebox.showerror("Error", "Password length should be a positive integer.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
            return

        if self.strength_var.get() == "Weak":
            characters = string.ascii_letters
        elif self.strength_var.get() == "Medium":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))
        self.password_label.config(text=f"Generated Password: {password}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
