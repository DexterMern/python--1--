import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_integral():
    expression = entry.get()
    try:
        result = eval(expression)
        integral_result = math.integral(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, integral_result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_derivative():
    expression = entry.get()
    try:
        result = eval(expression)
        derivative_result = math.derivative(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, derivative_result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_sqrt():
    expression = entry.get()
    try:
        result = eval(expression)
        sqrt_result = math.sqrt(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, sqrt_result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
button_1 = tk.Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=10, command=lambda: button_click("/"))
button_equal = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
button_clear = tk.Button(root, text="C", padx=20, pady=10, command=button_clear)
button_integral = tk.Button(root, text="∫", padx=20, pady=10, command=button_integral)
button_derivative = tk.Button(root, text="d/dx", padx=20, pady=10, command=button_derivative)
button_sqrt = tk.Button(root, text="√", padx=20, pady=10, command=button_sqrt)

# Grid layout
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)
button_integral.grid(row=5, column=0)
button_derivative.grid(row=5, column=1)
button_sqrt.grid(row=5, column=2)

root.mainloop()
