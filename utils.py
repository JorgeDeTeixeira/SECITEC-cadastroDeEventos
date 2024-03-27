# Importa o módulo os para executar comandos no sistema operacional
import os

# Importa o módulo keyboard para detectar o pressionamento de teclas no teclado
import keyboard

# Importa o módulo datetime para trabalhar com datas e horas
import datetime

# Importa o módulo sys para interagir com o interpretador Python
import sys

# Importa o módulo dados como dd para carregar dados dos administradores
import dados as dd


def line():
    """
    Imprime uma linha horizontal de 40 caracteres "=".
    """
    # Imprime uma linha de 40 "="
    print("=" * 40)


def simpleLine():
    """
    Imprime uma linha horizontal de 60 caracteres "-".
    """
    # Imprime uma linha de 60 "-"
    print("-" * 60)


def titleCentered(title):
    """
    Imprime o "titulo" centralizado em uma linha de 40 caracteres.

    Args:
        title: O título a ser centralizado.
    """
    # Imprime o título centralizado em 40 caracteres
    print(f"{title:^40}")


def clearTerminal():
    """
    Limpa a tela do terminal.
    """
    # Limpa a tela do terminal de acordo com o sistema operacional
    os.system("cls" if os.name == "nt" else "clear")


def back():
    """
    Exibe uma mensagem para o usuário pressionar "Q" para sair.
    """
    # Exibe mensagem e espera 'Q' para sair
    print("Pressione 'Q' para sair")
    simpleLine()
    while True:
        if keyboard.is_pressed("q"):
            print("Saindo...")
            break


def validatePassword(password):
    """
    Valida a senha do usuário.

    Args:
        password: A senha a ser validada.

    Raises:
        ValueError: Se a senha for inválida.
    """
    # Inicializa o contador de tentativas
    cont = 0

    # Valida a senha contra a lista de senhas dos administradores
    while password not in [admin["password"] for admin in dd.users["administrators"]]:
        simpleLine()
        print("ERRO! Senha incorreta!")
        cont += 1
        print(f"Mais {3 - cont} tentativas.")
        simpleLine()

        # Solicita a senha novamente
        password = str(input("Informe a senha:")).strip()

        # Encerra o programa após 3 tentativas
        if cont == 2:
            print("Tentativas esgotadas! Programa encerrado!")
            sys.exit()  # Encerra o programa


def validateDate(date):
    """
    Valida a data informada pelo usuário.

    Args:
        date: A data a ser validada.

    Returns:
        True se a data for válida, False caso contrário.
    """
    # Tenta converter a data para o formato datetime
    try:
        datetime.datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        # Se a conversão falhar, a data é inválida
        return False


def validateHours(hours):
    """
    Valida o horário informado pelo usuário.

    Args:
        hours: O horário a ser validado.

    Returns:
        True se o horário for válido, False caso contrário.
    """
    # Tenta converter o horário para o formato datetime
    try:
        datetime.datetime.strptime(hours, "%H:%M")
        return True
    except ValueError:
        # Se a conversão falhar, o horário é inválido
        return False

# No arquivo utils.py

def get_valid_input(prompt, validation_func):
    """
    Solicita entrada ao usuário e valida-a usando a função de validação fornecida.
    
    Args:
        prompt (str): A mensagem a ser exibida para solicitar entrada ao usuário.
        validation_func (function): Uma função que valida a entrada do usuário. Deve retornar True ou False.
    
    Returns:
        str: A entrada válida fornecida pelo usuário.
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Entrada inválida. Por favor, tente novamente.")
