import random
import string

print('-' * 40)
print("\n -> GERADOR DE SENHA ALEATÓRIO <-\n")
print('-' * 40)

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = "!@#$%&*"

while True:
    try:
        senha = int(input("Quantos caracteres você quer na sua senha? "))
        if senha < 8:
            print("Número inválido! A quantidade não pode ser menor que 8.")
            continue
        break
    except ValueError:
        print("Entrada Inválida: Digite apenas número.")
        continue

todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

senha_gerada = "".join(random.choices(todos_caracteres, k=senha))

print(f"Sua senha gerada: {senha_gerada}")

