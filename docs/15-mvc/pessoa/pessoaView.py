#Imeplementacao do View 

class PessoaView():
    '''Uma view muito simples que imprime na tela as informações'''

    @staticmethod
    def mostrarPessoa(P):
        ''' Mostra as informações de P
        Parâmetros
        ---------
        P : Pessoa
        '''

        print(P)

    @staticmethod
    def mostrarListaPessoas(l):
        ''' Mostra a lista de pessoas

        Parâmetros
        ----------
        l : list Pessoa
        '''

        print('------------------')
        for p in l:
            print(f' - {p}')

        print('------------------')

    @staticmethod
    def mostrarCPFJaExiste(P):
        '''
        Imprime a mensagem de erro relacionada ao erro CPFJaExiste

        Parametro
        ---------
        P : Pessoa
          Pessoa que está sendo cadastrada
        '''
        print(f'[Erro] O CPF {P.cpf} ja esta cadastrado no sistem')

    @staticmethod
    def mostrarCPFNaoExiste(cpf):
        '''
        Imprime a mensagem de erro relacionada ao erro CPFNaoExiste
        '''
        print(f'[Erro] O CPF {cpf} não existe no banco de dados')

    @staticmethod
    def mostrarAdicionar(P):
        ''' Mensagem para adicionar uma pessoa'''
        print(f'A pessoa {P} foi adicionada no sistema')

    @staticmethod
    def mostrarRemover(P):
        ''' Mensagem para adicionar uma pessoa'''
        print(f'A pessoa {P} foi removida do sistema')

    @staticmethod
    def mostrarUpdate(cpf, email):
        ''' Mensagem para update (email)'''
        print(f'O email da  pessoa com CPF {cpf} foi atualizado para {email}. ')

