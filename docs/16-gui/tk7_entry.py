import tkinter as tk

root = tk.Tk()
root.geometry('400x200+100+100')

l0 = tk.Label(root, text='Nome:')
e0 = tk.Entry(root) # cria widget para entrada de texto
l1 = tk.Label(root, text='Outro label')

l0.grid(row=0, column=0)
e0.grid(row=0, column=1)
l1.grid(row=1, columnspan=2) # grid permite que um widget ocupe mais de uma linha/coluna

s = 'Texto inicial'
e0.insert(0, s) # valor padrão para o campo de texto

root.mainloop()