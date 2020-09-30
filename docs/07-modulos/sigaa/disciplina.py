from .professor import Professor
class Disciplina:
    '''
    Representação de uma disciplina com carga horária e pré-requisitos. 
    Cada disciplina está a cargo de um professor
    '''

    def __init__(self, cod, nome, prof, CH):
        self.__cod = cod
        self.__nome = nome
        self.__prof = prof # Relação com a classe Professor 
        self.__CH = CH
        # Lista (poderia ser um conjunto) de pré-requisitos
        self.__prereq = []
        

    @property
    def cod(self):
        return self.__cod

    @property
    def CH(self):
        return self.__CH

    @property
    def nome(self):
        return self.__nome

    @property
    def professor(self):
        return self.__prof

    @property
    def prereq(self):
        '''Lista de pré-requisitos'''
        return self.__prereq

    # Este método poderia ser um setter
    def trocarProfessor(self, novoP):
        self.__prof = novoP

    def adicionarPreReq(self, D):
        '''
        Adicionar um pré-requisito
        D : Disciplina, disciplina que será pré-requisito
        '''
        self.__prereq.append(D)

    def __repr__(self):
        return f'Disciplina({self.cod}, {self.nome}, {self.professor}, {self.CH})'

    def listarPrereq(self):
        '''Retorna uma lista com os nomes dos pre-requisitos'''
        # Aqui temos um exemplo de Compreensão de lista em Python
        # [ d.nome for d in self._prereq] significa:
        # para cada d (do tipo disciplina) em self.__prereq, adicione 
        # a string d.nome à lista. O resultado: uma lista com os nomes dos 
        # pré-requisitos. 
        return f'Pré-requisitos de {self.nome}:  {[d.nome for d in self.__prereq]}'
