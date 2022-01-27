#Estoque.py

#cria lista vazia para controle de estoques
produtos=[]
quantidades=[]

def menu():
    option=-1
    while option!=0:
        print("-----   FEIRÃO  DO  LUCÃO   -----")
        print("-- Sistema de Controle de Estoques --")
        print("Desenvolvido por: Lucas Morgenster.")
        print("#1 = Cadastrar.")
        print("#2 = Listar.")
        print("#3 = Remover.")
        print("#4 = Sair.")
        option=int(input("Qual opção? "))
        if option==1:
            cadastrar()
        elif option==2:
            listar()
        elif option==3:
            remover()
        elif option==0:
            print("Saindo...")
        else:
            print("Opção inválida.")
            
def cadastrar():
    resposta=("S")
    while resposta=="S":
        nome=input("Digite o nome do produto: ")
        if nome in produtos:
            print("Produto já cadastrado.")
            continue
        quant=int(input("Digite a quantidade do produto: "))
        produtos.append(nome)
        quantidades.append(quant)
        resposta=input("Necessita de mais itens? (S)im // (N)ão:").upper()
        if resposta == "N":
            print("Parando de adicionar itens...")

def listar():
    print("Produtos:", produtos)
    print("Quantidades:", quantidades)

#   CONTINUA NA PRÓXIMA AULA
def remover():
    nome=input("Digite o nome do produto para ser removido: ")
    quant=int(input("Digite a quantidade do produto para ser removido: "))
    produtos.remove(nome)
    quantidades.remove(quant)

menu()
