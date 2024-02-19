# Crie um função que receba uma string como paramentro e a exiba.

user_name = input("Insira seu nome: ")
print("Olá ",user_name)

# Ou

def name(user_name):
  """
  :param user_name: str
  :return: str exibir o nome do usuario
  """
  return print("", user_name)

name(user_name)

# Ou 

def hi(user):
  """
  :param user: str
  :return: str exibir o nome do usuario
  """
  return print("", user)

hi('Olá')