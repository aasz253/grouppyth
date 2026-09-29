import tkinter as tk
from tkinter import font
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display
        display_frame = tk.Frame(root, bg="#1e1e1e")
        display_frame.pack(padx=10, pady=10, fill="x")

        self.display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Consolas", 24),
            bg="#2d2d2d",
            fg="#ffffff",
            bd=0,
            justify="right",
            insertbackground="white"
        )
        self.display.pack(fill="x", ipady=15)

        # Button layout
        buttons = [
            ["C", "⌫", "(", ")", "π"],
            ["sin", "cos", "tan", "√", "x²"],
            ["7", "8", "9", "/", "log"],
            ["4", "5", "6", "*", "ln"],
            ["1", "2", "3", "-", "eˣ"],
            ["0", ".", "=", "+", "1/x"],
        ]

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(padx=10, pady=5)

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = tk.Button(
                    btn_frame,
                    text=text,
                    font=("Segoe UI", 14, "bold"),
                    width=5,
                    height=2,
                    bd=0,
                    command=lambda t=text: self.on_button_click(t)
                )
                # Color scheme
                if text in ["C", "⌫"]:
                    btn.configure(bg="#ff6b6b", fg="white", activebackground="#ff5252")
                elif text == "=":
                    btn.configure(bg="#4caf50", fg="white", activebackground="#43a047")
                elif text in ["+", "-", "*", "/", "(", ")", "π", "sin", "cos", "tan",
                              "√", "x²", "log", "ln", "eˣ", "1/x"]:
                    btn.configure(bg="#3d3d3d", fg="#64b5f6", activebackground="#555555")
                else:
                    btn.configure(bg="#2d2d2d", fg="white", activebackground="#404040")

                btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

        # Make grid expand evenly
        for i in range(6):
            btn_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            btn_frame.grid_columnconfigure(i, weight=1)

        # Keyboard support
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Return>", lambda e: self.on_button_click("="))
        self.root.bind("<BackSpace>", lambda e: self.on_button_click("⌫"))

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == "=":
            self.calculate()
        elif char == "π":
            self.expression += str(math.pi)
            self.input_text.set(self.expression)
        elif char == "sin":
            self.expression += "math.sin("
            self.input_text.set(self.expression)
        elif char == "cos":
            self.expression += "math.cos("
            self.input_text.set(self.expression)
        elif char == "tan":
            self.expression += "math.tan("
            self.input_text.set(self.expression)
        elif char == "√":
            self.expression += "math.sqrt("
            self.input_text.set(self.expression)
        elif char == "x²":
            self.expression += "**2"
            self.input_text.set(self.expression)
        elif char == "log":
            self.expression += "math.log10("
            self.input_text.set(self.expression)
        elif char == "ln":
            self.expression += "math.log("
            self.input_text.set(self.expression)
        elif char == "eˣ":
            self.expression += "math.exp("
            self.input_text.set(self.expression)
        elif char == "1/x":
            self.expression += "1/"
            self.input_text.set(self.expression)
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            # Safe evaluation with math module available
            result = eval(self.expression, {"__builtins__": None}, {"math": math})
            # Format result nicely
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)  # avoid floating point noise
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def on_key_press(self, event):
        key = event.char
        if key in "0123456789.+-*/()":
            self.on_button_click(key)
        elif key.lower() == "c":
            self.on_button_click("C")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()