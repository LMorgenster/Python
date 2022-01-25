#Login.py

#Algoritmo
#1. criar uma lista com nomes de usuário, contendo vários usuários
#2. perguntar o nome do usuário
#3. verificar se o usuário está na lista
#4. informar se o usuário existe ou não

nomes=["Fernando","Eduarda", "Vitória","Rafaela","Giovana","Lucas","Vinícius", "Pedro"]
nome=input("Qual o nome do usuário? ").capitalize()
if nome in nomes:
    print("Bem-vindo usuário.")
else:
    print("Usuário não existente.")
