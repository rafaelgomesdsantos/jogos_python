# codigo 8 rafgds jogo adivinhação de números com o botlomeu

print("--------------Jogo do Número Secreto---------\n")
from random import *
rdn = randint(0,20)
tent = 5
print("Olá jogador, duvido você acertar o número que estou pensando\n")
print("Você tem apenas 5 vidas, Boa Sorte! >:D \n")
print("Para começar gostaria de saber o seu nome \n")
nome = input ("Digite o seu nome: ")
print("\n Olá", nome,", você pode me chamar de Botlomeu, vamos começar?")
while tent > 0:
    tent = tent - 1
    ch = int(input("Tente a sorte, digite um número: "))
    print()
    if ch > rdn:
        print("O número que estou pensando é menor")
        print("Você tem %d vidas" % tent,"," ,nome)
        print()
    elif ch < rdn:
        print("O número que estou pensando é maior")
        print("Você tem %d vidas" % tent, "," ,nome)
        print()
    else:
        print("Você ganhou! O número que eu estava pensando era %d !" % rdn, " Parabéns", nome, ":D")
        tent = -1
if tent == 0:
    print()
    print("Você perdeu! Mais sorte da próxima vez", nome, ":(")
    print("o número que eu estava pensando era %d !" % rdn)
    input()
elif tent == -1:
    input()
