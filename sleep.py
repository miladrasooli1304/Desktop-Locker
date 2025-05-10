import tkinter as tk
from tkinter import messagebox
import win32gui
import win32con
import threading
import time
import sys

# Initial settings
PASSWORD = "123"  # Password (you can change it)
TIMEOUT_SECONDS = 2000  # Timer duration in seconds (e.g., 30 seconds)
OPACITY_LEVEL = 0.1  # Opacity level (0.0 to 1.0, where 1.0 is fully black)

class DesktopLocker:
    def __init__(self, root, password, timeout, opacity):
        self.root = root
        self.password = password
        self.timeout = timeout
        self.opacity = opacity
        self.unlocked = False

        # Set window to fullscreen
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)  # Window always on top
        self.root.configure(bg="black")
        self.root.attributes("-alpha", self.opacity)  # Set transparency level (blackness)

        # Disable specific keys (as much as possible)
        self.root.bind("<Alt-Tab>", lambda e: "break")
        self.root.bind("<Control-Escape>", lambda e: "break")
        self.root.bind("<Control-Alt-Delete>", lambda e: "break")

        # Create user interface
        self.label = tk.Label(root, text="Desktop is locked. Enter the password:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack(pady=20)

        self.password_entry = tk.Entry(root, show="*", font=("Arial", 16), width=20)
        self.password_entry.pack(pady=10)
        self.password_entry.focus()

        self.submit_button = tk.Button(root, text="Unlock", command=self.check_password, font=("Arial", 14))
        self.submit_button.pack(pady=10)

        # Display remaining time
        self.timer_label = tk.Label(root, text=f"Unlocks after {self.timeout} seconds", fg="white", bg="black", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        # Start timer
        self.start_timer()

        # Close program with correct password or timer
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)

    def check_password(self):
        """Check the entered password"""
        entered_password = self.password_entry.get()
        if entered_password == self.password:
            self.unlocked = True
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect password!")
            self.password_entry.delete(0, tk.END)

    def start_timer(self):
        """Start timer for automatic unlocking"""
        def countdown():
            remaining = self.timeout
            while remaining > 0 and not self.unlocked:
                self.timer_label.config(text=f"Unlocks after {remaining} seconds")
                time.sleep(1)
                remaining -= 1
            if not self.unlocked:
                self.unlocked = True
                self.root.destroy()

        timer_thread = threading.Thread(target=countdown)
        timer_thread.daemon = True
        timer_thread.start()

    def prevent_close(self):
        """Prevent manual closing of the window"""
        if not self.unlocked:
            pass  # Window won't close unless unlocked by password or timer

def lock_desktop(password, timeout, opacity=0.9):
    """Main function to lock the desktop"""
    root = tk.Tk()
    app = DesktopLocker(root, password, timeout, opacity)
    root.mainloop()

if __name__ == "__main__":
    # Lock the desktop with specified password, timer, and opacity level
    lock_desktop(PASSWORD, TIMEOUT_SECONDS, OPACITY_LEVEL)