import tkinter as tk

root = tk.Tk()
root.geometry('400x200+100+100')

l0 = tk.Label(root, text='Nome:')
e0 = tk.Entry(root)
b0 = tk.Button(root, text='OK') # cria widget do tipo botão

l0.grid(row=0, column=0, sticky='NSWE') # sticky: cola a borda do widget na sua célula (quando esta é maior que o widget) 
                                        # (combinações de Norte-N, Sul-S, Leste-E, Oeste-W podem ser usadas)
e0.grid(row=0, column=1, sticky='NSWE')
b0.grid(row=1, columnspan=2, sticky='NSWE')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()