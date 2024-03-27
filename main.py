import datetime
from time import sleep
from participant import Participant
from event import Event
from certificate import Certificate

import utils as u
import dados as dd


def mainMenu():
    while True:
        u.line()
        u.titleCentered("MENU DE OPÇÕES")
        u.line()

        # Exibe as opções do menu numeradas
        print("1 - Cadastro de participantes.")
        print("2 - Cadastro de eventos.")
        print("3 - Listar eventos do sistema.")
        print("4 - Escolher evento.")
        print("5 - Gerar certificado.")
        print("6 - Sair.")

        # Solicita a escolha do usuário
        choice = str(input("Informe sua opção: "))
        u.clearTerminal()

        if choice == "1":
            Participant.registerParticipant()
        elif choice == "2":
            Event.registerEvent()
        elif choice == "3":
            Event.listEvents()
        elif choice == "4":
            Event.chooseEvent()
        elif choice == "5":
            Certificate.generateCertificate()
        elif choice == "6":
            # Imprime uma mensagem de saída e sai do loop infinito, encerrando o programa
            print("OBRIGADO POR USAR NOSSO SISTEMA! FIM DO PROGRAMA!")
            break
        else:
            # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro
            print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
        # Limpa o terminal depois de sair do menu
        sleep(2)
        u.clearTerminal()


mainMenu()
