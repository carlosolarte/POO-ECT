
# Contantes para os cargos (depois utilizaremos atributos de classe para
# representar a mesma situação)

CARGO = {0:"Adjunto", 1:"Associado", 2:"Titular"}


# As classes Professor e Aluno compartilham alguns atributos e comportamentos.
# Depois, utilizaremos o conceito de Herança para evitar duplicar esse
# comportamento

class Professor:
    '''Representação de um professor'''

    def __init__(self, nome, matricula, cargo):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargo = cargo


    @property
    def nome(self):
        '''get para self.__nome'''
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def cargo(self):
        return self.__cargo

    def ascender(self):
        '''Ascender na carreira docente'''
        if self.cargo < 2: #Note que self.cargo chama ao método definido no @property
            self.__cargo += 1

    def __repr__(self):
        return f'Professor({self.nome}, {self.matricula}, {CARGO[self.cargo]})'

