texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")            

# Informe um texto: lila
# Result: ia
# Result: 0 5 10 15 20 25 30 35 40 45 50     