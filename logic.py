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
    pass