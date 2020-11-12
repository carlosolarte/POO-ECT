import tkinter as tk

root = tk.Tk()
root.geometry('400x200+100+100')

l0 = tk.Label(root, text='Label 0', bg='red')
l1 = tk.Label(root, text='Label 1', bg='green')
l2 = tk.Label(root, text='Label 2', bg='blue')
l3 = tk.Label(root, text='Label 3', bg='gray')

l0.pack(side=tk.LEFT, fill=tk.Y)
l1.pack(side=tk.LEFT, fill=tk.X)
l2.pack(side=tk.RIGHT, fill=tk.Y)
l3.pack(side=tk.RIGHT, fill=tk.X)

root.mainloop()