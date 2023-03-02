from opcao1 import *

opcao = int(input(print("(1)Fazer consulta | (2)Sair")))

continuar = 'N'

while continuar.upper() == 'N':
    if opcao == 1:
        num = str(input(print("""
            1- selecionar todos as pessoas que tem mais de 18 anos"
            2- selecionar todas as colunas da cidade
            3- selecionar a uf e quantas cidades tem em cada uf
            4- selecionar a pessoa mais velha
            5- selecionar qual a pessoa mais nova
            6- selecionar o nome, endereco, telefone, celular, nome_cidade, nascimento das pessoas que moram no PR
            7- selecionar as cidades possuem pessoas cadastradas e quantas pessoas em cada cidade.
            8- selecionar todas as pessoas ativas exibindo todas as colunas ordenando pelo telefone.
            9- selecionar todas as cidades que nao possuem pessoas
            10- selecionar quais pessoas tem e-mail do hotmail""")))
            
        if num == 1:
            result = resposta(num)
            print("As pessoas que possuem mais que 18 anos são: " + num)
        
        elif num == 2:
            result = resposta(num)
            
            for linha in num:
                print(str(num[0]), str(num[1]), str(num[2]) )
            
    else:
        continuar = int(input("Deseja sair? (S/N)"))
