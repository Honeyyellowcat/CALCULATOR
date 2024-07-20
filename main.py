import tkinter as tk
from dark_mode import get_dark_mode_colors, get_light_mode_colors

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pink Calculator")
        self.geometry("400x700")
        self.resizable(False, False)
        
        self.history = []
        self.is_negative = False
        
        # Initialize theme to light mode
        self.theme = 'light'
        self.colors = get_light_mode_colors()
        
        self.configure(bg=self.colors["bg_color"])
        
        # Create and place the dark mode toggle switch
        self.dark_mode_canvas = tk.Canvas(self, width=120, height=30, bg=self.colors["bg_color"], highlightthickness=0)
        self.dark_mode_canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Draw the rounded border for the toggle box
        self.draw_rounded_border()
        
        # Create the smaller switch
        self.toggle_switch = self.dark_mode_canvas.create_oval(5, 5, 25, 25, fill=self.colors["button_color"], outline="")
        
        # Draw the sun icon
        self.dark_mode_canvas.create_text(20, 15, text="☀️", fill=self.colors["text_color"], font=("Arial", 12))
        
        # Draw the crescent moon icon
        self.dark_mode_canvas.create_text(95, 15, text="🌙", fill=self.colors["text_color"], font=("Arial", 12))
        
        self.dark_mode_canvas.bind("<Button-1>", self.toggle_dark_mode)
        
        # Create history display
        self.history_display = tk.Listbox(self, height=5, font=("Arial", 12), borderwidth=0, relief=tk.FLAT,
                                         bg=self.colors["current_bottom_box_color"], fg=self.colors["text_color"],
                                         highlightthickness=0, highlightbackground=self.colors["current_bottom_box_color"])
        self.history_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Create display
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=0, relief=tk.FLAT, justify='right',
                                bg=self.colors["current_bottom_box_color"], fg=self.colors["text_color"],
                                highlightthickness=0, highlightbackground=self.colors["current_bottom_box_color"])
        self.display.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Create and place buttons
        buttons = [
            ('C', 3, 0), ('CE', 3, 1), ('e^x', 3, 2), ('π', 3, 3),
            ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('log', 4, 3),
            ('sin⁻¹', 5, 0), ('cos⁻¹', 5, 1), ('tan⁻¹', 5, 2), ('ln', 5, 3),
            ('(', 6, 0), (')', 6, 1), ('%', 6, 2), ('/', 6, 3),
            ('7', 7, 0), ('8', 7, 1), ('9', 7, 2), ('x', 7, 3),
            ('4', 8, 0), ('5', 8, 1), ('6', 8, 2), ('-', 8, 3),
            ('1', 9, 0), ('2', 9, 1), ('3', 9, 2), ('+', 9, 3),
            ('0', 10, 0), ('.', 10, 1), ('+/-', 10, 2), ('=', 10, 3)
        ]
        
        # Create and place custom buttons with adjusted width and padding
        for (text, row, col) in buttons:
            self.create_button(text, row, col, width=80, height=50, radius=10)
         
        # Configure grid rows and columns to be responsive
        for i in range(11):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
        # Adjust column padding
        self.grid_columnconfigure(0, minsize=20)  # Adjust left padding
        self.grid_columnconfigure(3, minsize=20)  # Adjust right padding

    def draw_rounded_border(self):
        # Draw the rounded border
        box_width = 120
        box_height = 30
        radius = 15
        
        # Draw arcs for the corners
        self.dark_mode_canvas.create_arc(0, 0, 2*radius, 2*radius, start=90, extent=90, outline=self.colors["button_color"], width=2, style='arc')
        self.dark_mode_canvas.create_arc(box_width-2*radius, 0, box_width, 2*radius, start=0, extent=90, outline=self.colors["button_color"], width=2, style='arc')
        self.dark_mode_canvas.create_arc(0, box_height-2*radius, 2*radius, box_height, start=180, extent=90, outline=self.colors["button_color"], width=2, style='arc')
        self.dark_mode_canvas.create_arc(box_width-2*radius, box_height-2*radius, box_width, box_height, start=270, extent=90, outline=self.colors["button_color"], width=2, style='arc')

        # Draw lines to connect the arcs (the rectangles are replaced with lines)
        self.dark_mode_canvas.create_line(radius, 0, box_width-radius, 0, fill=self.colors["button_color"], width=2)
        self.dark_mode_canvas.create_line(0, radius, 0, box_height-radius, fill=self.colors["button_color"], width=2)
        self.dark_mode_canvas.create_line(box_width, radius, box_width, box_height-radius, fill=self.colors["button_color"], width=2)
        self.dark_mode_canvas.create_line(radius, box_height, box_width-radius, box_height, fill=self.colors["button_color"], width=2)

    def create_button(self, text, row, col, width=80, height=50, radius=10):
        canvas = tk.Canvas(self, width=width, height=height, bg=self.colors["bg_color"], highlightthickness=0)
        canvas.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # Uniform padding between buttons
        
        # Coordinates for the arcs
        x1, y1 = 0, 0
        x2, y2 = width, height
        r = radius
        
        # Draw rounded corners using arcs
        canvas.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, fill=self.colors["button_color"], outline="")
        canvas.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, fill=self.colors["button_color"], outline="")
        canvas.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, fill=self.colors["button_color"], outline="")
        canvas.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, fill=self.colors["button_color"], outline="")
        
        # Draw rectangles to fill the gaps and connect the arcs
        canvas.create_rectangle(x1 + r, y1, x2 - r, y1 + 2 * r, fill=self.colors["button_color"], outline="")
        canvas.create_rectangle(x1, y1 + r, x2, y2 - r, fill=self.colors["button_color"], outline="")
        canvas.create_rectangle(x1 + r, y2 - 2 * r, x2 - r, y2, fill=self.colors["button_color"], outline="")
        
        # Draw the button text in the center
        text_id = canvas.create_text(width / 2, height / 2, text=text, fill=self.colors["text_color"], font=("Arial", 14))
        
        # Bind events 
        canvas.bind("<Button-1>", lambda e, t=text: self.click_event(t))
        canvas.bind("<Enter>", lambda e: self.on_enter(canvas, text_id))
        canvas.bind("<Leave>", lambda e: self.on_leave(canvas, text_id))

    def on_enter(self, canvas, text_id):
        canvas.itemconfig(text_id, fill=self.colors["hover_text_color"])

    def on_leave(self, canvas, text_id):
        canvas.itemconfig(text_id, fill=self.colors["text_color"])

    def click_event(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.history.append(self.display.get() + ' = ' + str(result))
                self.history_display.insert(tk.END, self.display.get() + ' = ' + str(result))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        elif text == "CE":
            current_text = self.display.get()
            self.display.delete(len(current_text)-1, tk.END)
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + text)

    def toggle_dark_mode(self, event):
        if self.theme == 'light':
            self.theme = 'dark'
            self.colors = get_dark_mode_colors()
            self.dark_mode_canvas.config(bg=self.colors["bg_color"])
            self.configure(bg=self.colors["bg_color"])
            self.move_circle_to_right()
        else:
            self.theme = 'light'
            self.colors = get_light_mode_colors()
            self.dark_mode_canvas.config(bg=self.colors["bg_color"])
            self.configure(bg=self.colors["bg_color"])
            self.move_circle_to_left()
        
        self.update_colors()

    def move_circle_to_right(self):
        # Calculate the right edge coordinates of the toggle box
        right_edge = 120 - 25  # 120 (box width) - 25 (circle diameter)
        self.dark_mode_canvas.coords(self.toggle_switch, right_edge, 5, right_edge + 20, 25)
        self.dark_mode_canvas.itemconfig(self.dark_mode_canvas.find_withtag("current"), fill=self.colors["button_color"])


    def move_circle_to_left(self):
        # Set coordinates for the circle to move to the left edge
        self.dark_mode_canvas.coords(self.toggle_switch, 5, 5, 25, 25)
        self.dark_mode_canvas.itemconfig(self.dark_mode_canvas.find_withtag("current"), fill=self.colors["button_color"])


    def update_colors(self):
        # Update colors for buttons and display
        for widget in self.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.config(bg=self.colors["bg_color"])
                widget.itemconfig("text", fill=self.colors["text_color"])
            elif isinstance(widget, tk.Entry):
                widget.config(bg=self.colors["current_bottom_box_color"], fg=self.colors["text_color"])
            elif isinstance(widget, tk.Listbox):
                widget.config(bg=self.colors["current_bottom_box_color"], fg=self.colors["text_color"])

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
