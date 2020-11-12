from pessoaCtr import PessoaCtr
from pessoaView import PessoaView

def main():
    V = PessoaView() #View
    Ctr = PessoaCtr(V)
    Ctr.adicionar('cpf1','nome1','email1')
    Ctr.adicionar('cpf2','nome2','email2')
    Ctr.listar()
    Ctr.mostrar('cpf1')
    Ctr.mostrar('cpf3')
    Ctr.remover('cpf1')
    Ctr.remover('cpf1')
    Ctr.atualizar('cpf2','novoemail')
    Ctr.adicionar('cpf3', 'nome3','email3')
    Ctr.listar()


if __name__ == "__main__":
    main()
