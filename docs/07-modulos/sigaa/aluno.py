class Aluno:
    '''Representação de um aluno'''

    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula


    @property
    def nome(self):
        '''get para self.__nome'''
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    def __repr__(self):
        return f'Aluno({self.nome}, {self.matricula})'
