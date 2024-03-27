import utils as u
import dados as dd
from time import sleep
import datetime


from participant import Participant


class Certificate:
    def generateCertificate():
        """
        Gera um certificado para o participante selecionado.
        """

        u.line()
        u.titleCentered("GERAR CERTIFICADO")
        u.line()

        Participant.listParticipants()

        # Loop para selecionar um participante com tratamento de exceções
        while True:
            try:
                choice = int(input("Selecione o número do participante: "))
                if 1 <= choice <= len(dd.users["participants"]):
                    participant = dd.users["participants"][choice - 1]
                    break
                else:
                    print("Número de participante inválido. Tente novamente")
            except ValueError:
                print("Número de participante inválido. Tente novamente.")

        # Exibe título com o nome do participante selecionado
        u.line()
        u.titleCentered(f'EVENTOS INSCRITOS POR PARTICIPANTE: {participant["name"]}')
        u.line()

        # Exibe informações dos workshops inscritos pelo participante, se houver
        if "workshopsSelected" in participant:
            u.simpleLine()
            print("Minicursos inscritos:")
            u.simpleLine()
            for event in participant["workshopsSelected"]:
                print(f'Nome: {event["name"]}')
                print(f'Data: {event["date"]}')
                print(f'Horário: {event["hours"]}')
                print(f'Local: {event["local"]}')
                print(f'Carga Horária: {event["workLoad"]} horas')
                print(f'Ministrante: {event["minister"]}')
            u.simpleLine()

        # Exibe informações das palestras inscritas pelo participante, se houver
        if "lecturesSelected" in participant:
            u.simpleLine()
            print("Palestras inscritas:")
            u.simpleLine()
            for event in participant["lecturesSelected"]:
                print(f'Nome: {event["name"]}')
                print(f'Data: {event["date"]}')
                print(f'Horário: {event["hours"]}')
                print(f'Local: {event["local"]}')
                print(f'Carga Horária: {event["workLoad"]} horas')
                print(f'Ministrante: {event["minister"]}')
            u.simpleLine()

        # Calcula a carga horária total de todos os eventos inscritos
        totalWorkLoad = 0
        if "workshopsSelected" in participant:
            totalWorkLoad += sum(
                event["workLoad"] for event in participant["workshopsSelected"]
            )
        if "lecturesSelected" in participant:
            totalWorkLoad += sum(
                event["workLoad"] for event in participant["lecturesSelected"]
            )

        # Exibe a carga horária total
        print(f"Carga Horária Total: {totalWorkLoad} horas.")

        u.simpleLine()

        # Obtém a data atual e exibe como data de emissão do certificado
        currentDate = datetime.date.today()
        issuanceDate = currentDate.strftime("%d/%m/%Y")
        print(f"Certificado emitido em {issuanceDate}.")

        u.simpleLine()

        # Chama a função 'back' para retornar ao menu principal
        u.back()
        sleep(3)
