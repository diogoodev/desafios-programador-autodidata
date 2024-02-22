#Escreva  um programa que permita que o usuario pergunte sua altura, cor favorita ou autor favorito e retorne o resultado a partir do dicioraio criado no desafio anterior


sobre_mim = {"altura": "1.78","cor_favorita": "azul", "autor_favorito": "frank heirberlt", "livro_favorito":"duna"}

info = input("Para saber informações sobre mim digite: altura, cor_favorita, autor_favorito ou livro_favorito: ")

if info in sobre_mim:
    print(sobre_mim[info])
else:
    print("Não existe preferencia")