import tkinter as tk

root = tk.Tk()
root.geometry('400x400+100+100')

l0 = tk.Label(root, text='Label 0', bg='red')
l1 = tk.Label(root, text='Label 1', bg='green')
l2 = tk.Label(root, text='Label 2', bg='blue', height=20, width=20) # tamanho em unidades de texto
l3 = tk.Label(root, text='Label 3', bg='gray', font=("Helvetica", 16))

# método pack: passa a responsabilidade de posicionar widget para o geometry manager

l0.pack(fill=tk.X) # fill: preenche tela com widget na direção informada
l1.pack(fill=tk.X, expand=tk.YES) # expand: caso haja espaço vazio no master, redimensiona widget
l2.pack()
l3.pack(fill=tk.Y, expand=tk.YES)

root.mainloop()
