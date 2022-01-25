#Verificar.py

#Algoritmo
#1. cria uma lista de cores
#2. pergunta ao usuário o nome de uma cor
#3. diz para o usuário se a cor existe na lista
#4. se não está na lista, adiciona(anexa=append) na lista

cores=["verde","branco","preto","vermelho","branco","preto","amarelo","laranja","roxo","azul"]
cor=input("Digite uma cor: ")
if cor in cores:
    print("A cor digitada está na lista.")
else:
        print("A cor digitada não está na lista.")
        cores.append(cor)
        print("Você adicionou uma cor nova.")
        


