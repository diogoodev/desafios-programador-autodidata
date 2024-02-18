# Escreva uma função que converta uma string em um float e retorne o resultado. Use a manipulação de exceções para capturar a exceção que pode ocorrer.



def converte(valor):
    """
    :param valor: str.
    :return: float convertido
    """

    return float(valor)

peso = input('Digite o seu peso: ')

print(f'O seu peso convertido de string para float é: {converte(peso)}')
