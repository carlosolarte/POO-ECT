import tkinter as tk

root = tk.Tk()
root.geometry('400x200+100+100')

f1 = tk.Frame(root, bd=10, bg='yellow', relief=tk.SUNKEN)
f1.pack(fill=tk.BOTH, expand=1)

l0 = tk.Label(f1, text='Label 0', bg='red')
l1 = tk.Label(f1, text='Label 1', bg='green')

l0.pack(expand=True)
l1.pack()

f2 = tk.Frame(root, bd=10, bg='cyan', relief=tk.RAISED)
f2.pack(fill=tk.BOTH, expand=1)

l2 = tk.Label(f2, text='Label 2', bg='blue')
l3 = tk.Label(f2, text='Label 3', bg='gray')

l2.pack()
l3.pack()

root.mainloop()
