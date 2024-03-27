import os
import keyboard
import datetime
import sys
import dados as dd


def line():
    # Imprime uma linha horizontal formada por 30 caracteres "="
    print("=" * 40)


def simpleLine():
    # Imprime uma linha horizontal formada por 30 caracteres "-"
    print("-" * 60)


def titleCentered(title):
    # Imprime o "titulo" centralizado em uma linha de 30 caracteres
    print(f"{title:^40}")


def clearTerminal():
    # A função os.system() permite executar comandos no sistema operacional.
    # Dependendo do sistema operacional, ele executará 'cls' (Windows) ou 'clear' (Linux/Unix) para limpar a tela do terminal.
    os.system("cls" if os.name == "nt" else "clear")


def back():
    print("Pressione 'Q' para sair")
    simpleLine()
    while True:
        if keyboard.is_pressed("q"):
            print("Saindo...")
            break


def validatePassword(password):
    cont = 0  # Inicializa um contador de tentativas com valor 0

    # Enquanto a senha não estiver na lista de senhas dos administradores
    while password not in [admin["password"] for admin in dd.users["administrators"]]:
        simpleLine()
        print("ERRO! Senha incorreta!")
        cont += 1  # Incrementa o contador de tentativas

        # Exibe o número de tentativas restantes (até 3)
        print(f"Mais {3 - cont} tentativas.")
        simpleLine()

        # Solicita novamente a senha ao usuário
        password = str(input("Informe a senha:")).strip()

        # Se o número de tentativas chegar a 3, encerra o programa
        if cont == 2:
            print("Tentativas esgotadas! Programa encerrado!")
            sys.exit()  # Encerra o programa


def validateDate(date):
    try:
        # Tenta criar um objeto datetime a partir da string de data usando i formato "%d/%m%Y"
        datetime.datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        # Se ocorrer uma exceção ValueErro, a data é inválida, retorna False
        return False


def validateHours(hours):
    try:
        # Tenta criar um objeto datetime a partir da string de horário usando o formato "%H:%M"
        datetime.datetime.strptime(hours, "%H:%M")
        # Se a conversão for bem-sucedida, o horário é válido, retorna True
        return True
    except ValueError:
        # Se ocorrer uma exceção ValueError, o horário é inválido, retorna False
        return False
