# Um test no módulo sigaa

from sigaa.curso import Curso, Semestre
from sigaa.disciplina import Disciplina
from sigaa.aluno import Aluno
from sigaa.professor import Professor

# Para executar: python -m sigaa.test

def main():
    # Criar um curso
    C = Curso("BCT", 5)

    print("="*20)
    print("Professores")
    print("="*20)
    # Criar alguns professores
    P1 = Professor("Maria", 1234,1)
    P2 = Professor("João", 5678,1)
    P3 = Professor("Pedro", 1212,1)
    print(P1)
    P1.ascender()
    print("Depois de ascender")
    print(P1)


    # Esses professores deveriam estar lotados em um departamento da
    # Universidade... mas não estamos modelando isso

    print("="*20)
    print("Disciplinas")
    print("="*20)

    # Criar algumas disciplinas
    # Note que cada disciplina está associada a um professor
    C1 = Disciplina(1,"cálculo I", P1, 60)
    C2 = Disciplina(2,"cálculo II", P1, 60)
    C3 = Disciplina(3,"cálculo III", P2, 60)
    ED = Disciplina(4,"Equações Diferencias", P2, 60)
    F1 = Disciplina(5,"Física I", P2, 60)
    F2 = Disciplina(6,"Física II", P2, 60)

    F1.trocarProfessor(P3) # Trocar um profesor de uma disciplina

    # Adicionar pré-requisitos
    C2.adicionarPreReq(C1)
    C3.adicionarPreReq(C2)
    ED.adicionarPreReq(C3)
    F2.adicionarPreReq(F1)
    F2.adicionarPreReq(ED)

    # Adicionar as disciplinas ao curso 
    C.adicionarDisciplina(C1,0)
    C.adicionarDisciplina(C2,1)
    C.adicionarDisciplina(C3,2)
    C.adicionarDisciplina(ED,3)
    C.adicionarDisciplina(F1,3)
    C.adicionarDisciplina(F2,4)

    print(F2)
    print(F2.listarPrereq())

    print("Imprimir a grade e a carga horária do curso")

    C.imprimirGrade()
    print(f'Carga Horária: {C.cargaHoraria()}')

    print("="*20)
    print("Alunos")
    print("="*20)

    #Criar alguns alunos
    A1 = Aluno("Aluno 1", 1)
    A2 = Aluno("Aluno 2", 2)
    A3 = Aluno("Aluno 3", 3)
    A4 = Aluno("Aluno 4", 4)

    # Cadastrar os alunos no curso
    C.cadastrarAluno(A1)
    C.cadastrarAluno(A2)
    C.cadastrarAluno(A3)
    C.cadastrarAluno(A4)

    # Os semestres
    S1 = Semestre(2019,1)
    S2 = Semestre(2019,2)
    S3 = Semestre(2020,1)
    S4 = Semestre(2020,2)

    # O aluno 1 pagou os 3 cálculos
    C.matricularAluno(A1, C1, S1)
    C.trocarNota(A1.matricula, C1.cod, S1, 9.5)
    C.matricularAluno(A1, C2, S2)
    C.trocarNota(A1.matricula, C2.cod, S2, 10.0)
    C.matricularAluno(A1, C3, S3)
    C.trocarNota(A1.matricula, C3.cod, S3, 4.2)
    C.matricularAluno(A1, C3, S4)
    C.trocarNota(A1.matricula, C3.cod, S4, 9.0)

    # Agora podemos imprimir o histórico do aluno
    print("Histórico acadêmico do aluno")
    C.imprimirHistorico(A1.matricula)



main()
