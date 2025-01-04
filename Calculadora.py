import tkinter as tk
from tkinter import messagebox

def suma(a, b):
    return a+b

def resta(a, b):
    return 0

def multiplicacion(a, b):
    return 0

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def calcular(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operacion == 'suma':
            resultado = suma(num1, num2)
        elif operacion == 'resta':
            resultado = resta(num1, num2)
        elif operacion == 'multiplicacion':
            resultado = multiplicacion(num1, num2)
        elif operacion == 'division':
            resultado = division(num1, num2)
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo números válidos.")

root = tk.Tk()
root.title("Calculadora Básica")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_num1 = tk.Label(frame, text="Número 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(frame, text="Número 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

button_suma = tk.Button(frame, text="Suma", command=lambda: calcular('suma'))
button_suma.grid(row=2, column=0, padx=5, pady=5)

button_resta = tk.Button(frame, text="Resta", command=lambda: calcular('resta'))
button_resta.grid(row=2, column=1, padx=5, pady=5)

button_multiplicacion = tk.Button(frame, text="Multiplicación", command=lambda: calcular('multiplicacion'))
button_multiplicacion.grid(row=3, column=0, padx=5, pady=5)

button_division = tk.Button(frame, text="División", command=lambda: calcular('division'))
button_division.grid(row=3, column=1, padx=5, pady=5)

label_resultado = tk.Label(frame, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
