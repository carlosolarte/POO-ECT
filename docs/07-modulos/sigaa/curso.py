from .disciplina import Disciplina
from .professor import Professor
from .aluno import Aluno

class Semestre:
    '''Representação de um semestre como 2020.1'''

    def __init__(self, ano, semestre):
        # Atributos públicos! 
        self.ano = ano
        self.semestre=semestre

    def __repr__(self):
        return f'{self.ano}.{self.semestre}'

    def __eq__(self, outro):
        '''retorna True se o ano e semestre forem iguais'''
        return type(outro) == Semestre and outro.ano == self.ano and outro.semestre == self.semestre


class Nota:
    '''
    Notas dos alunos
    '''

    def __init__(self, aluno, disciplina, semestre, nota=0.0):
        self.__aluno = aluno
        self.__disciplina = disciplina
        self.__nota = nota
        self.__semestre = semestre

    @property 
    def aluno(self): return self.__aluno

    @property
    def disciplina(self): return self.__disciplina

    @property 
    def nota(self): return self.__nota

    @nota.setter
    def nota(self, N): self.__nota = N

    @property
    def semestre(self): return self.__semestre

    def __repr__(self):
        return f'{self.aluno.nome, self.disciplina.nome, self.nota, self.semestre}'


class Curso:
    '''Cursos da universidade. 
    Cada curso define a grade curricular
    O curso administra (e armazena)  as matrículas/notas dos alunos
    '''

    def __init__(self, nome, numSemestres):
        self.__nome = nome
        # A grade curricular é uma lista com as disciplinas de cada semestre
        # Aqui mais um exemplo de Compreensão de lista
        self.__grade = [ [] for i in range(numSemestres) ]

        # Alunos cadastrados nesse curso e suas matrículas/Notas
        # Utilizaremos um dicionário: chave: matrícula do aluno
        # valor: uma tupla com, um objeto aluno e uma lista de objetos tipo Nota

        self.__alunos = {}


    def adicionarDisciplina(self, D, S):
        '''
        Adicionar a disciplina D no semestre S
        S:int O número de semestre 0..len(self.__grade)-1
        '''
        self.__grade[S].append(D)

    @property
    def nome(self):
        return self.__nome

    def __repr__(self):
        s = f'Curso: {self.nome}. Número de semestres: {len(self.__grade)}'

    def cargaHoraria(self):
        '''Retorna o somatório das cargas horárias de todas as disciplinas da
        grade curricular'''
        s = 0
        for L in self.__grade:
            # Exemplo de compreesão de listas
            s += sum([ d.CH for d in L])

        return s

    def imprimirGrade(self):
        '''Imprime a grade curricular'''

        for (i, L) in enumerate(self.__grade):
            # O método join da classe string retorna a lista separada por ","
            print(f'Semestre {i+1}: ' + ','.join([d.nome for d in L]))

    def cadastrarAluno(self, A):
        '''
        Cadastrar o aluno A no curso.
        A: Aluno o aluno a ser cadastrado
        '''
        if A.matricula in self.__alunos:
            print(f'O aluno {A} já estava cadastrado')
        else:
            # Inicializar a tupla com A e a lista vazia de notas/matrículas
            self.__alunos[A.matricula] = (A, [])

    def matricularAluno(self, A, D, S):
        '''
        Matricular o Aluno A na disciplina D para o semestre S
        A:Aluno o Aluno a ser matriculado
        D:Disciplina A disciplina a cursar
        S:Semestre O semestre atual 
        '''
        if A.matricula not in self.__alunos:
            print('O aluno não pertence ao curso')
        else:
            N = Nota(A, D, S)
            # Lembre que __alunos[A.matricula] é uma tupla: < aluno, lista de notas>
            self.__alunos[A.matricula][1].append(N)
            

    def obterNota(self, matA, codD, S):
        '''
        Dada a matrícula de um aluno, o código da disciplina e um semestre, retorna
        o objeto Nota desse aluno (None se não existir)
        matA:int Número de matrícula do aluno
        codD:int Código da disciplina
        S:Semestre Objeto tipo semestre
        '''
        if matA not in self.__alunos:
            return None
        # como __alunos[matA] é uma tupla, atribuímos para duas variáveis
        A, LM = self.__alunos[matA]

        #Procurar a nota do aluno
        for N in LM:
            if N.disciplina.cod == codD and N.semestre == S:
                return N
        return None

    def trocarNota(self, matA, codD,S, novaNota):
        '''Trocar a nota do aluno'''
        N = self.obterNota(matA, codD, S)
        if N is None:
            print('Matrícula não encontrada')

        # Aqui estamos utilizando o setter da classe Nota
        N.nota = novaNota

    def imprimirHistorico(self, matA):
        '''Dado o número de matrícula, imprime o histórico  do aluno'''

        if matA not in self.__alunos:
            print('Aluno não cadastrado')
            return

        LM = self.__alunos[matA][1]
        for N in LM:
            print(N)

