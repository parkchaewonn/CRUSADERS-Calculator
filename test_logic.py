from tkinter import *
import math

class Genius_Pad(Frame):
# Main class for the calculator

    def __init__(self, master):
    # Frame of the calculator

        super(Genius_Pad, self).__init__(master)
        self.function = ""
        self.user_input = StringVar()
        self.grid()
        self.calculator_widgets()

    def calculator_widgets(self):
    # Creating the buttons of the calculator and design
    # GUI
    
        self.input = Entry(self, bg = "#068789", bd = 12, insertwidth = 5, width = 26, 
        font = ("Arial", 20, "bold"), fg = "white", textvariable = self.user_input, justify = RIGHT)
        self.input.grid(columnspan = 4)

        self.input.insert(0, "0")
        
        # Button for number 0
        self.image0 = PhotoImage(file = "Buttons/Zero.png")
        self.num0 = Button(self, image = self.image0, highlightthickness = 0, bd = 0,command = lambda : self.click_button(0))
        self.num0.grid(row = 5, column = 1, sticky = W)
        
        # Button for number 1
        self.image1 = PhotoImage(file = "Buttons/One.png")
        self.num1 = Button(self, image = self.image1, highlightthickness = 0, bd = 0, command = lambda : self.click_button(1))
        self.num1.grid(row = 4, column = 0, sticky = W)
    
        # Button for number 2
        self.image2 = PhotoImage(file = "Buttons/Two.png")
        self.num2 = Button(self, image = self.image2, highlightthickness = 0, bd = 0, command = lambda : self.click_button(2))
        self.num2.grid(row = 4, column = 1, sticky = W)
        
        # Button for number 3
        self.image3 = PhotoImage(file = "Buttons/Three.png")
        self.num3 = Button(self, image = self.image3, highlightthickness = 0, bd = 0, command = lambda : self.click_button(3))
        self.num3.grid(row = 4, column = 2, sticky = W)

        # Button for number 4
        self.image4 = PhotoImage(file = "Buttons/Four.png")
        self.num4 = Button(self, image = self.image4, highlightthickness = 0, bd = 0, command = lambda : self.click_button(4))
        self.num4.grid(row = 3, column = 0, sticky = W)

        # Button for number 5
        self.image5 = PhotoImage(file = "Buttons/Five.png")
        self.num5 = Button(self, image = self.image5, highlightthickness = 0, bd = 0, command = lambda : self.click_button(5))
        self.num5.grid(row = 3, column = 1, sticky = W)

        # Button for number 6
        self.image6 = PhotoImage(file = "Buttons/Six.png")
        self.num6 = Button(self, image = self.image6, highlightthickness = 0, bd = 0, command = lambda : self.click_button(6))
        self.num6.grid(row = 3, column = 2, sticky = W)

        # Button for number 7
        self.image7 = PhotoImage(file = "Buttons/Seven.png")
        self.num7 = Button(self, image = self.image7, highlightthickness = 0, bd = 0, command = lambda : self.click_button(7))
        self.num7.grid(row = 2, column = 0, sticky = W)

        # Button for number 8
        self.image8 = PhotoImage(file = "Buttons/Eight.png")
        self.num8 = Button(self, image = self.image8, highlightthickness = 0, bd = 0, command = lambda : self.click_button(8))
        self.num8.grid(row = 2, column = 1, sticky = W)

        # Button for numberd 9
        self.image9 = PhotoImage(file = "Buttons/Nine.png")
        self.num9 = Button(self, image = self.image9, highlightthickness = 0, bd = 0, command = lambda : self.click_button(9))
        self.num9.grid(row = 2, column = 2, sticky = W)

        # Buttons for basic operations
        # Addition Button
        self.image_addition = PhotoImage(file = "Buttons/Addition.png")
        self.num_addition = Button(self, image = self.image_addition, highlightthickness = 0, bd = 0, command = lambda : self.click_button("+"))
        self.num_addition.grid(row = 1, column = 0, sticky = W)

        # Subtraction Button
        self.image_subtraction = PhotoImage(file = "Buttons/Subtraction.png")
        self.num_subtraction = Button(self, image = self.image_subtraction, highlightthickness = 0, bd = 0, command = lambda : self.click_button("-"))
        self.num_subtraction.grid(row = 1, column = 1, sticky = W)

        # Multiplication Button
        self.image_multiplication = PhotoImage(file = "Buttons/Multiplication.png")
        self.num_multiplication = Button(self, image = self.image_multiplication, highlightthickness = 0, bd = 0, command = lambda : self.click_button("*"))
        self.num_multiplication.grid(row = 1, column = 2, sticky = W)
        
        # Division Button
        self.image_division = PhotoImage(file = "Buttons/Division.png")
        self.num_division = Button(self, image = self.image_division, highlightthickness = 0, bd = 0, command = lambda : self.click_button("/"))
        self.num_division.grid(row = 1, column = 3, sticky = W)

        # Decimal Button
        self.image_decimal_point = PhotoImage(file = "Buttons/Decimal Point.png")
        self.num_decimal_point = Button(self, image = self.image_decimal_point, highlightthickness = 0, bd = 0, command = lambda : self.click_button("."))
        self.num_decimal_point.grid(row = 5, column = 0, sticky = W)

        # Equal Button
        self.image_equals = PhotoImage(file = "Buttons/Equals.png")
        self.num_equals = Button(self, image = self.image_equals, highlightthickness = 0, bd = 0)
        self.num_equals.grid(row = 5, column = 2, sticky = W)

        # Exponent Button
        self.image_squared = PhotoImage(file = "Buttons/Squared.png")
        self.num_squared = Button(self, image = self.image_squared, highlightthickness = 0, bd = 0, command = self.ExpNum)
        self.num_squared.grid(row = 2, column = 3, sticky = W)
        
        # Squareroot Button
        self.image_square_root = PhotoImage(file = "Buttons/Square Root.png")
        self.num_square_root = Button(self, image = self.image_square_root, highlightthickness = 0, bd = 0, command = self.SqrtNum)
        self.num_square_root.grid(row = 3, column = 3, sticky = W)
        
        # Delete Button
        self.image_delete= PhotoImage(file = "Buttons/Delete.png")
        self.num_delete = Button(self, image = self.image_delete, highlightthickness = 0, bd = 0, command = self.DeleteNum)
        self.num_delete.grid(row = 4, column = 3, sticky = W)
        
        # Clear Button
        self.image_clear_all = PhotoImage(file = "Buttons/Clear All.png")
        self.num_clear_all = Button(self, image = self.image_clear_all, highlightthickness = 0, bd = 0, command = self.Clear)
        self.num_clear_all.grid(row = 5, column = 3, sticky = W)

    def click_button(self, number):
        self.function = str(self.function) + str(number)
        self.user_input.set(self.function)

    def displayResult(self, value) -> None:
        self.input.delete(0, END)
        self.input.insert(0, value)

    def Clear(self):
        self.function = ""
        self.input.delete(0, END)
        self.input.insert(0, "0")

    def DeleteNum(self):
        self.function = self.input.get()[:-1]
        self.input.delete(0, END)
        self.input.insert(0, self.function)
        
    def ExpNum(self) -> None:
        try:
            self.function = math.pow(float(self.input.get()), 2)
            self.input.delete(0, END)
            self.input.insert(0, self.function)
        except OverflowError:
            self.displayResult("Math Error")
            self.function = ""

    def SqrtNum(self) -> None:
        try:
            self.function = math.sqrt(float(self.input.get()))
            self.input.delete(0, END)
            self.input.insert(0, self.function)
        except ValueError:
            self.displayResult("Math Error")
            self.function = ""

class LogicTest():
    def __init__(self):
    # Frame of the calculator
        self.input = ""

    def Calculate(self):
        
        try:
            self.answer = eval(self.input)
            return self.answer

        except SyntaxError as e:
            
            return "Syntax Error"

        except ZeroDivisionError:
            return "Zero Division Error"
            
        except OverflowError:
            return "Math Error"

calculator = Tk()

calculator.title("The Genius Pad")
app = Genius_Pad(calculator)

# Make window fixed (cannot be resized)
calculator.resizable(width = False, height = False)

#calculator.mainloop()
