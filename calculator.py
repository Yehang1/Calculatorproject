from tkinter import *


root=Tk()
root.title("Calculator")
root.iconbitmap(r"C:\Users\lenovo\Downloads\favicon.ico")

#expression to access from all functions
expression=""
def input_number(number,equation):
    global expression
    expression=expression+str(number)
    equation.set(expression)

def clear_input_field(equation):
    global expression
    expression=""
    #empty string on input field
    equation.set("")


def evaluate(equation):
    global expression
    #trial to evaluate expression
    try:
        result=str(eval(expression))
        equation.set(result)

        expression=""
    except:
        expression=""










#Creating GUI
def main():
    root.title("yehangss calculator")
    equation=StringVar()
    input_field=Entry(root,textvariable=equation,font="roman")
    input_field.place(height=80)
    input_field.grid(columnspan=8,ipadx=100,ipady=40)
    equation.set("")

    button0 = Button(root, text="0", padx=40, pady=40, command=lambda: input_number(0, equation),bg="grey")
    button1 = Button(root, text="1", padx=40, pady=40, command=lambda: input_number(1, equation),bg="grey")

    button2 = Button(root, text="2", padx=40, pady=40, command=lambda: input_number(2, equation),bg="grey")
    button3 = Button(root, text="3", padx=40, pady=40, command=lambda: input_number(3, equation),bg="grey")
    button4 = Button(root, text="4", padx=40, pady=40, command=lambda: input_number(4, equation),bg="grey")
    button5 = Button(root, text="5", padx=40, pady=40, command=lambda: input_number(5, equation),bg="grey")
    button6 = Button(root, text="6", padx=40, pady=40, command=lambda: input_number(6, equation),bg="grey")
    button7 = Button(root, text="7", padx=40, pady=40, command=lambda: input_number(7, equation),bg="grey")
    button8 = Button(root, text="8", padx=40, pady=40, command=lambda: input_number(8, equation),bg="grey")
    button9 = Button(root, text="9", padx=40, pady=40, command=lambda: input_number(9, equation),bg="grey")
    button_plus = Button(root, text="+", padx=40, pady=40, command=lambda: input_number("+", equation),bg="pink")
    button_minus = Button(root, text="-", padx=40, pady=40, command=lambda: input_number("-", equation),bg="pink")
    button_divide = Button(root, text="/", padx=40, pady=40, command=lambda: input_number("/", equation),bg="pink")
    button_cross = Button(root, text="*", padx=40, pady=40, command=lambda: input_number("*", equation),bg="pink")
    button_equals = Button(root, text="=", padx=40, pady=40,command=lambda: evaluate(equation),bg="pink")
    button_clear = Button(root, text="AC", padx=40, pady=40, command=lambda: clear_input_field(equation),bg="pink")

    button0.grid(row=5, column=2)
    button1.grid(row=4, column=1)
    button2.grid(row=4, column=2)
    button3.grid(row=4, column=3)
    button4.grid(row=3, column=1)
    button5.grid(row=3, column=2)
    button6.grid(row=3, column=3)
    button7.grid(row=2, column=1)
    button8.grid(row=2, column=2)
    button9.grid(row=2, column=3)
    button_clear.grid(row=5, column=1)
    button_plus.grid(row=5, column=3)
    button_minus.grid(row=2, column=4)
    button_cross.grid(row=3, column=4)
    button_divide.grid(row=4, column=4)
    button_equals.grid(row=5, column=4)

    root.mainloop()
if __name__ == '__main__':
      main()