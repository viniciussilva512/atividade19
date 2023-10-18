# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

def calcular_media_e_status(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media < 5.0:
        return "REPROVADO"
    elif 5.0 <= media < 7.0:
        return "RECUPERAÇÃO"
    else:
        return "APROVADO"
    #Entrada de notas 
nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota "))
 
status = calcular_media_e_status(nota1, nota2)
 
print(f"O aluno está {status} com uma média de {nota1} e {nota2}.")
    