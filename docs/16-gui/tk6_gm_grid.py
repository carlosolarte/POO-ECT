import tkinter as tk

root = tk.Tk()
root.geometry('400x200+100+100')

l0 = tk.Label(root, text='Label 0', bg='red')
l1 = tk.Label(root, text='Label 1', bg='green')
l2 = tk.Label(root, text='Label 2', bg='blue')
l3 = tk.Label(root, text='Label 3', bg='gray')
l4 = tk.Label(root, text='Label 4', bg='gray')
l5 = tk.Label(root, text='Label 5', bg='gray')
l6 = tk.Label(root, text='Label 6', bg='gray')
l7 = tk.Label(root, text='Label 7', bg='gray')
l8 = tk.Label(root, text='Label 8', bg='gray')

# método grid: informa o geometry manager em qual linha/coluna do master deseja posicionar widget
# (master é dividido em uma matriz)

l0.grid(row=0, column=0, stick='NE') 
l1.grid(row=0, column=1)
l2.grid(row=0, column=2)
l3.grid(row=1, column=0)
l4.grid(row=1, column=1)
l5.grid(row=1, column=2)
l6.grid(row=2, column=0)
l7.grid(row=2, column=1)
l8.grid(row=2, column=2)


# método rowconfigure: informa em quantos pixels uma linha deve ser redimensionada quando o seu mestre for redimensionado
# método columnconfigure: informa em quantos pixels uma coluna deve ser redimensionada quando o seu mestre for redimensionado

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()
