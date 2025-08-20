'''
Topics to Cover:
- Typing Test GUI Application
'''

import tkinter as tk
import time
import random

# Sample texts for typing test
TEXTS = [
    "Python is a powerful programming language for data science.",
    "Artificial intelligence is transforming the world rapidly.",
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help you improve accuracy and speed.",
    "Tkinter makes it easy to create desktop applications in Python."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.text_to_type = random.choice(TEXTS)
        self.start_time = None
        self.end_time = None

        # Title
        self.label_title = tk.Label(root, text="Typing Speed Test", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=10)

        # Text to type
        self.label_text = tk.Label(root, text=self.text_to_type, wraplength=600, 
                                   font=("Arial", 14), justify="center", fg="blue")
        self.label_text.pack(pady=20)

        # Input box
        self.text_entry = tk.Text(root, height=5, width=60, font=("Arial", 14))
        self.text_entry.pack()
        self.text_entry.bind("<KeyPress>", self.start_typing)

        # Button
        self.submit_button = tk.Button(root, text="Check Speed", command=self.check_speed, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        # Results
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset Test", command=self.reset_test, font=("Arial", 12))
        self.reset_button.pack(pady=5)

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_speed(self):
        if self.start_time is None:
            self.result_label.config(text="Start typing first!", fg="red")
            return

        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        typed_text = self.text_entry.get("1.0", tk.END).strip()

        # Words per minute calculation
        word_count = len(typed_text.split())
        wpm = round((word_count / total_time) * 60, 2)

        # Accuracy calculation
        correct_chars = 0
        for i, c in enumerate(typed_text):
            if i < len(self.text_to_type) and c == self.text_to_type[i]:
                correct_chars += 1
        accuracy = round((correct_chars / len(self.text_to_type)) * 100, 2)

        result_text = f"Time: {round(total_time, 2)} sec\nWPM: {wpm}\nAccuracy: {accuracy}%"
        self.result_label.config(text=result_text, fg="green")

    def reset_test(self):
        self.text_to_type = random.choice(TEXTS)
        self.label_text.config(text=self.text_to_type)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
