#AC2

#Exercício 1

ganho_hora = float(input("Digite os ganhos por hora:"))
horas_no_mes = float(input("Digite as horas trabalhadas:"))
pagamento = ganho_hora * horas_no_mes

print("O salário é: R$",  pagamento)

#Exercício 2


conjunto = (1, 2, 3)
calculo = (2 * 1 + 3 + 3 + 3**3)
print(calculo)

#Exercício 3

def funcao():
 conjunto = (1, 2, 3)
 calculo = (2 * 1 + 3 + 3 + 3**3)


 return funcao

#Exercício 4 

ano = float(input("Digite um ano:"))

ano = (ano % 4 == 0)
ano = (ano % 100 == 0)
ano = (ano % 400 == 0)

print(ano)

