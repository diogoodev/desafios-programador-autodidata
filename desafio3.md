 1. Exiba três strings diferentes:
   print('Um')
   print('Dois')
   print('Tres')

2. Escreva um programa que exiba uma mensagem se uma variavel for menor que 10 e outra mensagem se uma variavel for maior ou igual a 10
     a = 10
     if a > 10:
       print("É maior a 10")
     else:
       print("É igual ou menor a 10")
3. Escreva um programa que exiba uma mensagem se uma variavel for menor ou igual a 10 e outra mensagem se uma variavel for maior que 10, mas menor que 25 e ainda outra mensagem se a variavel for maior do que 25.
     a = 10
     if a <= 10:
       print("É menor ou igual  a 10")
     elif a > 10 and a <= 25:
       print("É maior 10 e menor ou igual a 25")
     else:
       print("É maior que 25")
4. Crie um programa que divida duas variaveis e exiba o resto.
   a = 10
   b = 2
   result = a % b
   print('O resto da divisão é', result)
5. Crie um programa que receba duas variaveis, as divida, e exiba o quociente.
   a = 25
   b = 5
   result = a // b
   print('O quaociente da divisão é', result)
6.  Escreva um programa com uma variavel **age** que receba um inteiro e exiba strings diferentes dependendo de que o inteiro **age** receber.
   age = 10
   if age >= 18:
      print('Você é um adulto')
   elif age >=12 and age < 18:
      print('Você é um adolescente')
   else:
      print('Você é uma criança')  
