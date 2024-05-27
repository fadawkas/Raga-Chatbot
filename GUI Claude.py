import tkinter as tk
from tkinter import scrolledtext

class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Raga Chatbot")
        self.geometry("500x600")

        # Center the window
        window_width = 500
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create chat transcript area
        self.transcript_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=20)
        self.transcript_area.grid(row=0, column=0, padx=10, pady=10)

        # Create input area
        self.input_area = tk.Text(self, wrap=tk.WORD, width=50, height=5)
        self.input_area.grid(row=1, column=0, padx=50, pady=10)

        # Create send button
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=0, padx=10, pady=10)

    def send_message(self):
        message = self.input_area.get("1.0", tk.END).strip()
        if message:
            self.transcript_area.configure(state="normal")
            self.transcript_area.insert(tk.END, "You: " + message + "\n")
            self.transcript_area.configure(state="disabled")
            self.input_area.delete("1.0", tk.END)

            # Add your AI logic here to generate a response
            response = "Waalaikumsalam"
            self.transcript_area.configure(state="normal")
            self.transcript_area.insert(tk.END, "Raga: " + response + "\n")
            self.transcript_area.configure(state="disabled")

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()