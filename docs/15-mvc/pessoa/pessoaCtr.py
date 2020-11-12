
from pessoa import *
class PessoaCtr:
    '''Controlador'''

    def __init__(self, view):
        # Note que podemos instanciar o controlador com diferentes views 
        self._view = view

    def adicionar(self, cpf, nome, email):
        ''' adicionar a pessoa'''
        P = Pessoa(cpf, nome, email)
        try:
            Pessoa.adicionar(P)
            self._view.mostrarAdicionar(P)
        except CPFJaExiste:
            self._view.mostrarCPFJaExiste()

    def atualizar(self, cpf, email):
        '''Atualizar o email da pessoa'''
        try:
            Pessoa.updateEmail(cpf, email)
            self._view.mostrarUpdate(cpf, email)
        except CPFNaoExiste: 
            self._view.mostrarCPFNaoExiste(cpf)

    def remover(self, cpf):
        ''' remover uma pessoa '''
        try:
            P = Pessoa.dadosPessoa(cpf)
            Pessoa.removerPessoa(cpf)
            self._view.mostrarRemover(P)
        except CPFNaoExiste: 
            self._view.mostrarCPFNaoExiste(cpf)

    def listar(self):
        '''Listar as pessoas'''
        l = Pessoa.listaPessoas()
        self._view.mostrarListaPessoas(l)

    def mostrar(self, cpf):
        '''Mostrar as informacoes da pessoa'''
        try:
            P = Pessoa.dadosPessoa(cpf)
            self._view.mostrarPessoa(P)
        except CPFNaoExiste: 
            self._view.mostrarCPFNaoExiste(cpf)


