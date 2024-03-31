import tkinter as tk

class Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("250x500")
        self.window.resizable(0,0)
        # Create a button
        self.button1 = tk.Button(self.window, width = 5, height = 3,fg="white",bg="grey",text="1")
        self.button1.bind("<Button-1>", lambda event: self.on_click(event, "1"))
        self.button2 = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="2")
        self.button2.bind("<Button-1>", lambda event: self.on_click(event, "2"))
        self.button3 = tk.Button(self.window, width = 5, height = 3,fg="white",bg="grey",text="3")
        self.button3.bind("<Button-1>", lambda event: self.on_click(event, "3"))
        self.buttonplus = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="+")
        self.buttonplus.bind("<Button-1>", lambda event: self.on_click(event, "+"))
        self.button4 = tk.Button(self.window, width = 5, height = 3,fg="white",bg="grey",text="4")
        self.button4.bind("<Button-1>", lambda event: self.on_click(event, "4"))
        self.button5 = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="5")
        self.button5.bind("<Button-1>", lambda event: self.on_click(event, "5"))
        self.button6 = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="6")
        self.button6.bind("<Button-1>",lambda event: self.on_click(event, "6"))
        self.buttonminus = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="-")
        self.buttonminus.bind("<Button-1>",lambda event: self.on_click(event, "-"))
        self.button7 = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="7")
        self.button7.bind("<Button-1>", lambda event: self.on_click(event, "7"))
        self.button8 = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="8")
        self.button8.bind("<Button-1>", lambda event: self.on_click(event, "8"))
        self.button9 = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="9")
        self.button9.bind("<Button-1>", lambda event: self.on_click(event, "9"))
        self.buttond = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="/")
        self.buttond.bind("<Button-1>", lambda event: self.on_click(event, "/"))
        self.buttonp = tk.Button(self.window, width = 5, height = 3,fg="white",bg="grey",text=".")
        self.buttonp.bind("<Button-1>", lambda event: self.on_click(event, "."))
        self.button0 = tk.Button(self.window, width = 5, height = 3,fg="white",bg="grey",text="0")
        self.button0.bind("<Button-1>", lambda event: self.on_click(event, "0"))
        self.buttonm = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="*")
        self.buttonm.bind("<Button-1>", lambda event: self.on_click(event, "*"))
        self.buttone = tk.Button(self.window,width = 5, height = 3,fg="white",bg="grey", text="=")
        self.buttone.bind("<Button-1>", lambda event: self.on_click(event, "="))
        
        
        self.buttonclr = tk.Button(self.window,width = 2, height = 2,fg="red",text="Clear")
        self.buttonclr.bind("<Button-1>",lambda event: self.on_click(event,"Clear"))
        # Create a text box
        
        self.text_box = tk.Entry(self.window,font = ('Arial',20,'bold'),width=10)

        # Pack the button and text box
        #self.button1.grid(row=1,column=1)
        self.text_box.grid(row=0,column=0,columnspan=4,sticky="ew")
        self.buttonclr.grid(row=1,column=0,columnspan=4,sticky="ew")
        self.button1.grid(row=2,column=0,sticky="ew")
        self.button2.grid(row=2,column=1,sticky="ew")
        self.button3.grid(row=2,column=2,sticky="ew")
        self.buttonplus.grid(row=2,column=3,sticky="ew")
        self.button4.grid(row=3,column=0,sticky="ew")
        self.button5.grid(row=3,column=1,sticky="ew")
        self.button6.grid(row=3,column=2,sticky="ew")
        self.buttonminus.grid(row=3,column=3,sticky="ew")
        self.button7.grid(row=4,column=0,sticky="ew")
        self.button8.grid(row=4,column=1,sticky="ew")
        self.button9.grid(row=4,column=2,sticky="ew")
        self.buttond.grid(row=4,column=3,sticky="ew")
        self.buttonp.grid(row=5,column=0,sticky="ew")
        self.button0.grid(row=5,column=1,sticky="ew")
        self.buttonm.grid(row=5,column=2,sticky="ew")
        self.buttone.grid(row=5,column=3,sticky="ew")
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_columnconfigure(0, weight=0)
    def on_click(self, event,text):
        button_value = text
        # Get the current value of the text box
        current_value = self.text_box.get()
        if button_value=="=":
            try:
                current_value = eval(current_value)
                self.text_box.delete(0, tk.END)
                self.text_box.insert(0, current_value)

            except:
                self.text_box.delete(0, tk.END)
                self.text_box.insert(0, "Error")
        elif button_value=="Clear":
            self.text_box.delete(0, tk.END)
        else:
        # Set the value of the text box
            self.text_box.delete(0, tk.END)
            self.text_box.insert(0, current_value + button_value)

if __name__ == "__main__":
    example = Example()
    example.window.mainloop()