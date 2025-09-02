import random
import string

#Função para gerar senha segura

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Você precisa escolher pelo meno sum tipo de caractere."

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

#Função para gerar multiplas senhas

def gerar_multiplas_senhas(quantidade, tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    senhas = []
    for _ in range(quantidade):
        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
        senhas.append(senha)
    return senhas

#Entrada interativa de usuario

try:
    quantidade = int(input("Quantas senhas você deseja gerar? "))
    tamanho = int(input("Qual o tamanho de cada senha? "))

    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n) ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    senhas_geradas = gerar_multiplas_senhas(
        quantidade=quantidade,
        tamanho=tamanho,
        usar_maiusculas=usar_maiusculas,
        usar_minusculas=usar_minusculas,
        usar_numeros=usar_numeros,
        usar_simbolos=usar_simbolos,
    
    )

    for i, senha in enumerate(senhas_geradas,start=1):
        print(f"Senha {i}: {senha}")

except ValueError:
    print("Por favor, insira valores numéricos válidos para quantidade e tamanho.")