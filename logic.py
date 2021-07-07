import math

# Calculator Logic
def Calculate(self):
    self.data = self.input.get()
    try:
        self.answer = eval(self.data)
        self.displayResult(self.answer)
        self.function = self.answer

    except SyntaxError as e:
        self.displayResult("Syntax Error")
        self.function = ""

    except ZeroDivisionError:
        self.displayResult("Zero Division Error")
        self.function = ""

def displayResult(self, value):
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

def ExpNum(self):
    self.function = math.pow(float(self.input.get()), 2)
    self.input.delete(0, END)
    self.input.insert(0, self.function)
        
def SqrtNum(self):
    self.function = math.sqrt(float(self.input.get()))
    self.input.delete(0, END)
    self.input.insert(0, self.function)
