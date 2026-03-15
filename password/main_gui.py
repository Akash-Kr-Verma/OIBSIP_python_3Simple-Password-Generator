import tkinter as tk
from tkinter import messagebox
import pyperclip  # Library for clipboard access
import generator_logic  # Import our logic file

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("400x450")

        # --- Title ---
        tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=15)

        # --- Settings Frame ---
        settings_frame = tk.Frame(root)
        settings_frame.pack(pady=10)

        # Length Input
        tk.Label(settings_frame, text="Length:").grid(row=0, column=0, padx=5)
        self.length_var = tk.StringVar(value="12")
        self.length_entry = tk.Entry(settings_frame, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, padx=5)

        # Checkboxes for complexity
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(settings_frame, text="A-Z (Uppercase)", variable=self.use_upper).grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(settings_frame, text="a-z (Lowercase)", variable=self.use_lower).grid(row=2, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(settings_frame, text="0-9 (Digits)", variable=self.use_digits).grid(row=3, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(settings_frame, text="#$% (Symbols)", variable=self.use_symbols).grid(row=4, column=0, columnspan=2, sticky="w")

        # --- Generate Button ---
        self.btn_generate = tk.Button(root, text="Generate Password", command=self.generate_action, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.btn_generate.pack(pady=15)

        # --- Result Display ---
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=("Courier", 14), justify="center", width=24, state="readonly")
        self.result_entry.pack(pady=5)

        # Strength Label
        self.strength_label = tk.Label(root, text="Strength: -", font=("Arial", 10))
        self.strength_label.pack(pady=5)

        # --- Action Buttons (Copy) ---
        self.btn_copy = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#4CAF50", fg="white")
        self.btn_copy.pack(pady=10)

    def generate_action(self):
        try:
            length = int(self.length_var.get())
            
            # Generate using logic file
            pwd = generator_logic.generate_password(
                length,
                self.use_upper.get(),
                self.use_lower.get(),
                self.use_digits.get(),
                self.use_symbols.get()
            )

            # Check for errors returned by logic
            if pwd.startswith("Error"):
                messagebox.showerror("Input Error", pwd)
                return

            # Update UI
            self.result_var.set(pwd)
            
            # Check strength
            strength = generator_logic.check_strength(pwd)
            color = "red" if strength == "Weak" else "orange" if strength == "Medium" else "green"
            self.strength_label.config(text=f"Strength: {strength}", fg=color)

        except ValueError:
            messagebox.showerror("Error", "Length must be a valid number")

    def copy_to_clipboard(self):
        pwd = self.result_var.get()
        if pwd:
            pyperclip.copy(pwd)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "Generate a password first.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()