import os
import subprocess
import time

def limpatela(): # limpar terminal para deixar mais bonito
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

# para limpar descrição do local do arquivo
limpatela() 

sair=False
while not sair:
    
    print("=" * 10, "JOGO DA FORCA", "=" * 10, "\n")
    print("| Dica: não utilize nada além de letras.\n")
    palavra = (input(">>> Escreva a palavra para adivinharem: ").lower().strip())  # palavra chave
    limpatela()

    # OBS.: Shift + Alt + F || Formata corretamente o script.

    palavra_oculta = [" " if letra == " " else "_" for letra in palavra]  #[expressão for variável in sequência]
    n_tentativas = 6  # numero de tentativas
    letras_tentadas = []
    caracteres = list(palavra)  # separar a palavra em letras

    while n_tentativas > 0:

        limpatela()

        print("=" * 10, "JOGO DA FORCA", "=" * 10)
        print(f"\n| Palavra: {" ".join(palavra_oculta)}  ({len(palavra)})")
        print(f"| Tentativas restantes: {n_tentativas}\n")

        erro = True
        chute = input(">>> Tente uma letra: ").lower().strip()
        print()

        if chute in letras_tentadas:
            print("| Essa letra já foi escolhida.\n")
            time.sleep(1)
            continue
            
        letras_tentadas.append(chute)

        for i, letra in enumerate(caracteres): # utiliza o indice (i) para cada item (letra) em caracteres -> letra[i] 
            if chute == letra:
                palavra_oculta[i] = chute
                erro = False

        if erro:
            n_tentativas -= 1
            print("| Essa letra não está na palavra.\n")
            time.sleep(1)
    
        if "_" not in palavra_oculta:
            break

    limpatela()

    print("=" * 10, "MORTE SUBITA", "=" * 10)
    print(f"\n| Palavra: {" ".join(palavra_oculta)}")
    chute_palavra = input(">>> A palavra é: ")
    print()

    if chute_palavra == palavra:
        print("="*10,"RESULTADO",10*"=")
        print(f"\n| Você acertou! A palavra é '{palavra}'\n")

    else:
        print("="*10,"RESULTADO",10*"=")
        print(f"\n| Você errou! A palavra é '{palavra}'\n")

    while True:
            
            print("="*10,"JOGA NOVAMENTE",10*"=","\n")
            print("| Deseja jogar novamente? [y/n]")
            opcao=input(">>> Sua escolha: ")

            if opcao=="y":
                print("\n| Você escolheu jogar novamente.")
                time.sleep(1)
                limpatela()
                time.sleep(1)
                break
                
            elif opcao=="n":
                print("\n| Você escolheu sair.")
                sair=True # permite sair do While pai (while not sair)
                time.sleep(1)
                limpatela()
                time.sleep(1)
                break

            else:
                print("\n| Opção inválida.\n")
                time.sleep(1)
                limpatela()