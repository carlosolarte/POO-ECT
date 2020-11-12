# -*- coding: utf-8 -*-

import tkinter as tk

class Calculadora:
    def __init__(self):
        self.res = None
        self.num1 = None
        self.num2 = None

    def soma(self):
        self.res = self.num1 + self.num2
        return self.res

    def subtrai(self):
        self.res = self.num1 - self.num2
        return self.res

    def multiplica(self):
        self.res = self.num1 * self.num2
        return self.res

    def divide(self):
        self.res = self.num1 / self.num2
        return self.res

class CalculadoraGUI:
    def __init__(self):
        self.calculadora = Calculadora() #objeto que realiza operacoes aritmeticas
        self.estado = 'num1'

        # janela principal
        self.root = tk.Tk()
        self.root.title('Calculadora TK')
        self.root.geometry("300x300")

        self._inicializa_variaveis()
        self._inicializa_gui()
        #self._configura_eventos()
        tk.mainloop()

    def _inicializa_variaveis(self):
        self.var_texto = tk.StringVar() #texto com expressao a ser calculada

    def _inicializa_gui(self):
        # frame interno
        self.frame1 = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.frame1.pack(expand=True, fill=tk.BOTH)

        # entrada de texto
        self.ent_texto = tk.Entry(self.frame1, textvariable=self.var_texto)
        self.ent_texto.pack(side=tk.TOP, fill=tk.X)

        # frame com grupo de botões
        self.frame2 = tk.Frame(self.frame1, bd=5, relief=tk.SUNKEN, bg='yellow')
        self.frame2.pack(expand=True, fill=tk.BOTH)

        # 7 8 9 +
        self.b7 = tk.Button(self.frame2, text="7", command=lambda: self._processa_entrada(7))
        self.b7.grid(row=0, column=0, sticky="NSWE")

        self.b8 = tk.Button(self.frame2, text="8", command=lambda: self._processa_entrada(8))
        self.b8.grid(row=0, column=1, sticky="NSWE")

        self.b9 = tk.Button(self.frame2, text="9", command=lambda: self._processa_entrada(9))
        self.b9.grid(row=0, column=2, sticky="NSWE")

        self.bsom = tk.Button(self.frame2, text="+", command=lambda: self._processa_entrada('+'))
        self.bsom.grid(row=0, column=3, sticky="NSWE")

        # 4 5 6 -
        self.b4 = tk.Button(self.frame2, text="4", command=lambda: self._processa_entrada(4))
        self.b4.grid(row=1, column=0, sticky="NSWE")

        self.b5 = tk.Button(self.frame2, text="5", command=lambda: self._processa_entrada(5))
        self.b5.grid(row=1, column=1, sticky="NSWE")

        self.b6 = tk.Button(self.frame2, text="6", command=lambda: self._processa_entrada(6))
        self.b6.grid(row=1, column=2, sticky="NSWE")

        self.bsub = tk.Button(self.frame2, text="-", command=lambda: self._processa_entrada('-'))
        self.bsub.grid(row=1, column=3, sticky="NSWE")

        # 1 2 3 *
        self.b1 = tk.Button(self.frame2, text="1", command=lambda: self._processa_entrada(1))
        self.b1.grid(row=2, column=0, sticky="NSWE")

        self.b2 = tk.Button(self.frame2, text="2", command=lambda: self._processa_entrada(2))
        self.b2.grid(row=2, column=1, sticky="NSWE")

        self.b3 = tk.Button(self.frame2, text="3", command=lambda: self._processa_entrada(3))
        self.b3.grid(row=2, column=2, sticky="NSWE")

        self.bmul = tk.Button(self.frame2, text="*", command=lambda: self._processa_entrada('*'))
        self.bmul.grid(row=2, column=3, sticky="NSWE")

        # 0   = /
        self.b0 = tk.Button(self.frame2, text="0", command=lambda: self._processa_entrada(0))
        self.b0.grid(row=3, column=0, columnspan=2, sticky="NSWE")

        self.bigual = tk.Button(self.frame2, text="=", command=lambda: self._processa_entrada('='))
        self.bigual.grid(row=3, column=2, columnspan=2, sticky="NSWE")

        # configura linhas e colunas quanto ao redimensionamento
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.frame2.rowconfigure(3, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.columnconfigure(2, weight=1)
        self.frame2.columnconfigure(3, weight=1)

    #def _configura_eventos(self):
    #    self.bsom.bind(tk., self.calculadora.soma)

    def _processa_entrada(self, par):

        # aguardando num. 1
        if self.estado == 'num1':
            # botao com digito pressionado
            if type(par) == int:
                self.var_texto.set(self.var_texto.get() + str(par))
            # botao com operador pressionado
            else:
                conteudo = self.var_texto.get()
                if conteudo.isdigit():
                    self.calculadora.num1 = int(conteudo)
                    self.estado = 'num2'
                    self.var_texto.set('')
                    if par == '+':
                        self.bsom['relief'] = tk.SUNKEN

        # aguardando num. 2
        elif self.estado == 'num2':
            # botao com digito pressionado
            if type(par) == int:
                self.var_texto.set(self.var_texto.get() + str(par))
            # botao com operador pressionado
            else:
                conteudo = self.var_texto.get()
                if conteudo.isdigit():
                    self.calculadora.num2 = int(conteudo)
                    self.estado = 'res_ok'
                    self.calculadora.soma()
                    self.var_texto.set(str(self.calculadora.res))
                    self.bsom['relief'] = tk.RAISED

        # resultado foi calculado anteriormente
        elif self.estado == 'res_ok':
            # botao com digito pressionado
            if type(par) == int:
                self.var_texto.set(str(par))
                self.estado = 'num1'

if __name__ == "__main__":
    c = CalculadoraGUI()

