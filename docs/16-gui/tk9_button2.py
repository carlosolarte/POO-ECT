import tkinter as tk

def imprime_texto(texto):
    print(f'Texto= {texto}')

root = tk.Tk()
root.geometry('400x200+100+100')

l0 = tk.Label(root, text='Nome:')
e0 = tk.Entry(root)
b0 = tk.Button(root, text='OK', command= lambda: imprime_texto(5)) # adiciona callback: função/método a ser chamado quando evento ocorre

# lambda: imprime_texto(5) é uma função anónima (sem nome) que sempre faz a mesma coisa: executar imprime_texto(5)

# Sem utilizar lambda
def f():
    imprime_texto(5)

b1 = tk.Button(root, text='CANCEL', command= f) 

l0.grid(row=0, column=0)
e0.grid(row=0, column=1)
b0.grid(row=1, column=0)
b1.grid(row=1, column=1)

root.mainloop()
