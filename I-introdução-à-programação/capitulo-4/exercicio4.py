# Escreva um programa com duas funções. A primeira deve receber um inteiro como paramentro e retornar o resultado do inteiro dividido por 2. A segunda função deve  receber um inteiro como paramentro e retornar o resultado multiplicado por 4. Chame a primeira função, salve o resultado como um variavel e passe como paramentro para a segunda função

def dividir(num):
  return num / 2;

def multiplicar(num):
  return num * 4;

result_dividir = dividir(int(input("Insira um numero: ")));
result_multiplicar = multiplicar(result_dividir)

print('O numero inserido dividio por 2 e multiplicado por 4 tem o seguinte resultado: ', result_multiplicar)