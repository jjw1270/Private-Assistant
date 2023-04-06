import tkinter as tk
import tkinter.font as tkFont


class TkinterWindow:
    def __init__(self, text):
        # Create a new window
        self.window = tk.Tk()
        self.window.title("더블클릭하면 닫힙니다")
        self.window.geometry("800x600")

        # Create a canvas widget
        self.canvas = tk.Canvas(self.window, bg="white")

        # Pack the canvas widget to fill the window
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas to hold the label widget
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Create a font object with the desired size and weight
        self.font = tkFont.Font(size=16, weight="bold")

        # Create a text widget to display the text with the custom font
        self.text_widget = tk.Text(self.frame, font=self.font, wrap="word")
        self.text_widget.insert("end", text)
        self.text_widget.pack(side="left", fill="both", expand=True)

        # Allow the text widget to be selectable by dragging the mouse
        self.text_widget.bind("<ButtonPress-1>", lambda event: self.text_widget.tag_add("sel", "insert", "end"))
        self.text_widget.bind("<B1-Motion>", lambda event: self.text_widget.tag_add("sel", "insert", "end"))

        # Resize the canvas scrollable region based on the frame size
        self.frame.bind("<Configure>", lambda event, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # Bind the double-click event to the close_window function
        self.text_widget.bind("<Double-Button-1>", self.close_window)

    # Function to close the window
    def close_window(self, event):
        self.window.destroy()

    # Start the main event loop
    def start(self):
        self.window.mainloop()
