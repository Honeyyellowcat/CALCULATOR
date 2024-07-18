import tkinter as tk
import sympy as sp
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pink Calculator")
        self.geometry("400x700")
        self.resizable(False, False)
        
        self.history = []  # List to store calculation history
        self.is_negative = False  # Track whether the current number is negative
        
        # Define colors
        self.bg_color = "#ffecec"  # Light pink
        self.button_color = "#ffbaba"  # Medium pink
        self.text_color = "#663f3f"  
        self.hover_bg_color = "#663f3f"  
        self.hover_text_color = "#ffffff"  # White
        self.current_bottom_box_color = "#ffd8d8"
        
        self.configure(bg=self.bg_color)
        
        # Create history display with transparent border
        self.history_display = tk.Listbox(self, height=5, font=("Arial", 12), borderwidth=0, relief=tk.FLAT, bg=self.current_bottom_box_color, fg=self.text_color, highlightthickness=0, highlightbackground=self.current_bottom_box_color)
        self.history_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Create display with transparent border
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=0, relief=tk.FLAT, justify='right', bg=self.current_bottom_box_color, fg=self.text_color, highlightthickness=0, highlightbackground=self.current_bottom_box_color)
        self.display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Create and place buttons
        buttons = [
            ('C', 2, 0), ('CE', 2, 1), ('e^x', 2, 2), ('π', 2, 3),
            ('sin', 3, 0), ('cos', 3, 1), ('tan', 3, 2), ('d/dx', 3, 3),
            ('sin⁻¹', 4, 0), ('cos⁻¹', 4, 1), ('tan⁻¹', 4, 2), ('∫', 4, 3),
            ('log', 5, 0), ('ln', 5, 1), ('%', 5, 2), ('/', 5, 3),
            ('7', 6, 0), ('8', 6, 1), ('9', 6, 2), ('x', 6, 3),
            ('4', 7, 0), ('5', 7, 1), ('6', 7, 2), ('-', 7, 3),
            ('1', 8, 0), ('2', 8, 1), ('3', 8, 2), ('+', 8, 3),
            ('0', 9, 0), ('.', 9, 1), ('+/-', 9, 2), ('=', 9, 3)
        ]
        
        # Create and place custom buttons with adjusted width and padding
        for (text, row, col) in buttons:
            self.create_button(text, row, col, width=80, height=50)
        
        # Configure grid rows and columns to be responsive
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
        # Adjust column padding
        self.grid_columnconfigure(0, minsize=20)  # Adjust left padding
        self.grid_columnconfigure(3, minsize=20)  # Adjust right padding

    def create_button(self, text, row, col, width=80, height=50, radius=10):
        canvas = tk.Canvas(self, width=width, height=height, bg=self.bg_color, highlightthickness=0)
        canvas.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # Uniform padding between buttons
        
        # Coordinates for the arcs
        x1, y1 = 0, 0
        x2, y2 = width, height
        r = radius
        
        # Draw rounded corners using arcs
        canvas.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, fill=self.button_color, outline="")
        canvas.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, fill=self.button_color, outline="")
        canvas.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, fill=self.button_color, outline="")
        canvas.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, fill=self.button_color, outline="")
        
        # Draw rectangles to fill the gaps and connect the arcs
        canvas.create_rectangle(x1 + r, y1, x2 - r, y1 + 2 * r, fill=self.button_color, outline="")
        canvas.create_rectangle(x1, y1 + r, x2, y2 - r, fill=self.button_color, outline="")
        canvas.create_rectangle(x1 + r, y2 - 2 * r, x2 - r, y2, fill=self.button_color, outline="")
        
        # Draw the button text in the center
        text_id = canvas.create_text(width / 2, height / 2, text=text, fill=self.text_color, font=("Arial", 14))
        
        # Bind events 
        canvas.bind("<Button-1>", lambda e, t=text: self.click_event(t))
        canvas.bind("<Enter>", lambda e: self.on_enter(canvas, text_id))
        canvas.bind("<Leave>", lambda e: self.on_leave(canvas, text_id))

    def on_enter(self, canvas, text_id):
        canvas.itemconfig(text_id, fill=self.hover_text_color)

    def on_leave(self, canvas, text_id):
        canvas.itemconfig(text_id, fill=self.text_color)

    def click_event(self, key):
        print(f"Clicked: {key}")  # Debug: Print clicked button
        if key == '=':
            try:
                expr = self.display.get()
                expr = expr.replace('π', str(sp.pi))
                expr = expr.replace('e', str(math.e))
                result = str(sp.sympify(expr).evalf())
                print(f"Evaluating: {expr} = {result}")  # Debug: Print evaluation
                self.history.append(expr + " = " + result)
                self.update_history()
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.after(2000, self.clear_display)  # Clear the display after 2 seconds
            except Exception as e:
                print(f"Error: {e}")  # Debug: Print error message
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.after(2000, self.clear_display)  # Clear the display after 2 seconds
        elif key == 'C':
            self.display.delete(0, tk.END)
            self.is_negative = False  # Reset sign toggle state
        elif key == 'CE':
            self.history.clear()
            self.update_history()
        elif key == '+/-':
            current_text = self.display.get()
            if current_text:
                if self.is_negative:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, current_text.lstrip('-'))
                    self.is_negative = False
                else:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, '-' + current_text)
                    self.is_negative = True
        elif key in ['√', 'ln', 'e^x', 'π', '∫', 'd/dx', 'sin', 'cos', 'tan', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh', 'cosh', 'tanh']:
            try:
                expr = self.display.get()
                expr = expr.replace('π', str(sp.pi))
                expr = expr.replace('e', str(math.e))
                x = sp.symbols('x')
                sym_expr = sp.sympify(expr)
                
                if key == '√':
                    result = str(sp.sqrt(sym_expr).evalf())
                elif key == 'ln':
                    result = str(sp.ln(sym_expr).evalf())
                elif key == 'e^x':
                    result = str(sp.exp(sym_expr).evalf())
                elif key == 'π':
                    result = str(sp.pi.evalf())
                elif key == '∫':
                    result = str(sp.integrate(sym_expr, x).evalf())
                elif key == 'd/dx':
                    result = str(sp.diff(sym_expr, x).evalf())
                elif key == 'sin':
                    result = str(sp.sin(sym_expr).evalf())
                elif key == 'cos':
                    result = str(sp.cos(sym_expr).evalf())
                elif key == 'tan':
                    result = str(sp.tan(sym_expr).evalf())
                elif key == 'sin⁻¹':
                    result = str(sp.asin(sym_expr).evalf())
                elif key == 'cos⁻¹':
                    result = str(sp.acos(sym_expr).evalf())
                elif key == 'tan⁻¹':
                    result = str(sp.atan(sym_expr).evalf())
                elif key == 'sinh':
                    result = str(sp.sinh(sym_expr).evalf())
                elif key == 'cosh':
                    result = str(sp.cosh(sym_expr).evalf())
                elif key == 'tanh':
                    result = str(sp.tanh(sym_expr).evalf())
                
                print(f"Advanced Calc: {key}({expr}) = {result}")  # Debug: Print result
                self.history.append(key + "(" + expr + ") = " + result)
                self.update_history()
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.after(2000, self.clear_display)  # Clear the display after 2 seconds
            except Exception as e:
                print(f"Error: {e}")  # Debug: Print error message
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.after(2000, self.clear_display)  # Clear the display after 2 seconds
        else:
            self.display.insert(tk.END, key)
    
    def update_history(self):
        self.history_display.delete(0, tk.END)
        for entry in self.history:
            self.history_display.insert(tk.END, entry)
    
    def clear_display(self):
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
 
