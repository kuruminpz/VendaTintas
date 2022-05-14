# https://wiki.python.org.br/ListaDeExercicios

# Exercício 01
'''
print("Olá Mundo")
'''

# Exercicio 2
'''
num = input("Digite um Numero: ")
print(f"O numero informado foi: {num}")
'''

# Exercicio 3
'''
num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite um numero: "))

print(f"O resultado é: {num_1 + num_2}")
'''

# Exercicio 17

from math import ceil

print("\n\tLoja de tinta de um FDP")

preco_lata: int = 80
preco_galao = 25

base_lata = 6*18 # retorna os metros quadrados minimos pra gastar 1 lata = 108 m2
base_galao = (3.6)*6 # retorna os metros quadrados minimos pra gastar 1 galao = 21,6 m2


pedido = float(input("Digite o tamanho, em metros quadrados, do local: "))
pedido = pedido * 1.1


def pedido_lata(metros):
    if pedido < base_lata:
        print(f"O senhor gastará R$ {preco_lata}.")
    else:
        aux1 = ceil(pedido/base_lata)
        print(f"O senhor gastará R$ {preco_lata * aux1} usando {aux1} latas.")
        # ceil() arredonda sempre pra cima o valor


def pedido_galao(metros):
    if pedido < base_galao:
        print(f"O senhor gastará R$ {preco_galao}.")
    else:
        aux2 = ceil(pedido/base_galao)
        print(f"O senhor gastará R$ {preco_galao * aux2} usando {aux2} galões.")


def pedido_ambos(metros):
    latas = int(metros/base_lata)
    resto = metros%base_lata
    galoes = ceil(resto/base_galao)

    valor2 = (preco_lata*latas + preco_galao * galoes)

    print(f"O senhor gastará R$ {valor2} em {latas} latas e em {galoes} galões.")

print(f"Com o acréscimo de 10%, consideramos a área em {'%.2f' % pedido} metros quadrados!")

print('\nOrçamento em Latas de 18 litros: ')
pedido_lata(pedido)

print('\nOrçamento em galão de 3,6 litros: ')
pedido_galao(pedido)

print('\nOrçamento em Ambos de 18 e  3,6 litros: ')
pedido_ambos(pedido)
