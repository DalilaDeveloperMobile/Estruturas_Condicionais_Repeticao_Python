![Captura de tela 2024-04-17 123206](https://github.com/DalilaDeveloperMobile/Conhecendo-Linguagem-Python/assets/29806802/83eba503-c094-4431-b85f-e7b4cc9d92de)
### Passos Iniciais Realizados Nesse Bootcamp Python AI Backend Developer. [dio_me](https://www.dio.me/)
### ✅Estruturas Condicionais e de Repetição em Python.

### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> Indentação e Blocos:

```
# Python só deixa exercultar um código se tiver Indentação.

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(10000)

# Result: Obrigado por ser nosso cliente, tenha um bom dia!
```
### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> Estruturas Condicionais:

### Estruturas Condicionais if/elif/else:
```
# Estruturas Condicionais if/elif/else

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar a CNH")    


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")     
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")

# Informe sua idade: 17
# Ainda não pode tirar a CNH
# Ainda não pode tirar a CNH
# Pode fazer aulas teóricas, mas não pode fazer aulas práticas.
```
### Estrutura Condicional Aninhada:
```
# Estrutura Condicional Aninhada.

conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do chaque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente.")            
```
### Estrutura Condicional Ternária:
``` 
# Estrutura Condicional Ternária.

saldo = 500
saque = 200

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
# Result: Sucesso ao realizar o saque!.
```
### <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> Estruturas de Repetição:

### Estruturas de Repetição for iterável e função built-in range:
```
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
```
### Estruturas de Repetição While:    
```
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
```
### Estruturas de Repetição While com break e continue:  
```
#  continue pula o número.
#  break para a execulção apartir do número.

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#    if numero % 2 == 0:
#        continue

#    print(numero, end=" ")
```
<h3 align="center"> Made with <img src="https://gifs.eco.br/wp-content/uploads/2021/06/gifs-de-coracao-7.gif" width="30px"> by Dalila...</h3>
<div align="center"  style="display: inline-block">
  <a href="https://www.linkedin.com/in/dalila-cust%C3%B3dio-046076181/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
  <a href = "mailto:dalila.dalila70@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://instagram.com/dalila.dalila70" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
  <a target="_blank" href="https://api.whatsapp.com/send?phone=5588997138541"><img  alt="Whatsapp" width="117px" src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a> 
</div>
