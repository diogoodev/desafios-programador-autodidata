# 3. Escreva uma função que receba tres parametros obrigatorios e dois parametros opcionais

def form(nome, idade, hobby, pais='Brasil', ano='2024'):
 """
    :param nome: str.
    :param idade: int.
    :param hobby: str.
    :param pais: str.
    :param ano: int.
    :return: str, int, str, str, int exibe as respostas do formulario.

 """

  print("================================================")
  print("Nome: ", nome)
  print("idade: ", idade)
  print('Hobby: ', hobby)
  print("Pais: ", pais)
  print("Ano: ", ano)
  print("================================================")

def insert_form():
   
   confirma = input("Você deseja prencher todos os campos do formulario? (y/n)") 

   if confirma == 'y' : 
      print("Prenche os dados a seguir: ")
      print("================================================")
      nome = input("Nome: ")
      idade = input('Idade: ')
      hobby = input('Hobby: ')
      pais = input('Pais: ')
      ano = input('Ano: ')
      print("================================================")
      form(nome, idade, hobby, pais, ano)
   else:
      print("================================================")
      print("Prenche os dados a seguir: ")
      nome = input("Nome: ")
      idade = input('Idade: ')
      hobby = input('Hobby: ')
      print("================================================")
      form(nome, idade, hobby)

      

insert_form()