import utils as u
import dados as dd
from time import sleep

from participant import Participant


class Event:
    def registerEvent():
        try:
            u.line()
            u.titleCentered("CADASTRO DE EVENTOS")
            u.line()

            # Verifica o nome do administrador com permissão de cadastrar algum evento
            nameAdmin = (
                str(
                    input("Informe o nome do administrador com permissão de cadastro: ")
                )
                .strip()
                .capitalize()
            )

            # Verifica se o nome do administrador está na lista de administradores
            if nameAdmin in [admin["name"] for admin in dd.users["administrators"]]:
                print(f"Usuário:{nameAdmin}.")
                # Solicita a senha do administrador (Com até 3 tentativas)
                password = str(input("Informe a senha (3 tentativas): "))
                u.validatePassword(password)

                u.simpleLine()
                u.titleCentered("ACESSO LIBERADO")
                u.simpleLine()

                # Exibe opções de cadastro (Minicurso ou palestras)
                print("Opções de cadastro:")
                print("M - Minicurso")
                print("P - Palestra")

                # Solicita o tipo de evento desejado (M ou P)
                t = (
                    str(
                        input(
                            "O que você deseja cadastrar? [M - Minicurso | P - Palestra]: "
                        )
                    )
                    .strip()
                    .upper()[0]
                )

                # Define o tipo de evento com base na escolha do administrador
                if t == "M":
                    typeEvent = "Minicurso"
                elif t == "P":
                    typeEvent = "Palestra"
                else:
                    print("Tipo de evento inválido.")
                    return

                # Solicita informações do evento(nome, local, data, horário, carga horária, ministrante)
                u.line()
                u.titleCentered(f"CADASTRO DE {typeEvent.upper()}")
                u.line()

                # Solicita o nome do evento
                name = str(input("Nome do evento: ")).strip().capitalize()

                # Validação do nome do evento: não pode estar em branco
                while not name:
                    name = str(input("Nome vazio. Nome do evento:"))
                # Solicita o local do evento onde será realizado

                local = str(input("Informe o local:")).strip().capitalize()

                while not local:
                    local = str(input("Local vazio. Local do evento: "))

                # Solicita a data do evento
                date = str(input("Informe a data (XX/XX/XXXX): "))

                # Validação da data usando a função validarData(data)
                while u.validateDate(date) == False:
                    date = str(
                        input("Use o formato correto. Informe a data (XX/XX/XXXX): ")
                    )
                    if u.validateDate(date):
                        break

                # Solicita horario do evento
                hours = str(input("Informe o horário (XX-XX): "))

                # Validação do horário usando a função validarHorario(horario)
                while u.validateHours(hours) == False:
                    hours = str(
                        input("Use o formato correto. Informe o horário (XX:XX): ")
                    )
                    if u.validateHours(hours):
                        break

                # Solicita a carga horária do evento (em horas)
                while True:
                    # Solicita a carga horária em horas
                    workLoad = str(input("Carga horária (em horas): "))
                    # Validação da carga horária: valor positivo
                    if workLoad.isdigit() and int(workLoad) > 0:
                        workLoad = int(workLoad)
                        break
                    else:
                        print(
                            "Valor de carga horária inválida. Informe um valor positivo."
                        )

                # Solicita o nome do ministrante para o evento
                minister = str(input("Informe o ministrante: ")).strip().capitalize()

                # Validação do nome do ministrante: não pode estar em branco
                while not minister:
                    minister = str(input("Ministrante vazio. Informe o ministrante: "))

                # Cria um dicionário com as informações do novo evento
                newEvent = {
                    "typeEvent": typeEvent,
                    "name": name,
                    "date": date,
                    "local": local,
                    "hours": hours,
                    "workLoad": workLoad,
                    "minister": minister,
                }

                # Adiciona um novo evento á lista de eventos correspodente (Minicursos ou paletra)
                if t == "M":
                    dd.events["workshops"].append(newEvent)
                elif t == "P":
                    dd.events["lectures"].append(newEvent)
                else:
                    print("TIPO DE EVENTO INVÁLIDO!")

                # Imprime uma mensagem de sucesso informando que o evento foi adicionado
                u.simpleLine()
                print(f"{typeEvent} {name} adicionado com sucesso ao sistema!")
                u.simpleLine()
            else:
                # Caso o nome do admnistrador não seja encontrado ou a senha esteja incorreta
                print(
                    "PERMISSÃO NEGADA! Nome de administrador não encontrado ou senha incorreta!"
                )

            u.back()
            sleep(2)
        except Exception as e:
            # Lidar com exceções em geral e fornecer informações sobre o erro
            print(f"Ocorreu um erro durante o cadastro do evento: {str(e)}")

    def listEvents():
        u.line()
        u.titleCentered("LISTA DE EVENTOS")
        u.line()

        # Lista os minicursos cadastrados no sistema
        print("MINICURSOS:")
        u.simpleLine()
        for index, event in enumerate(dd.events["workshops"]):
            # Imprime informações de cada minicurso
            print(f"Índice: {index}.")
            print(f'Nome: {event["name"]}.')
            print(f'Data: {event["date"]}.')
            print(f'Horário: {event["hours"]}.')
            print(f'Local: {event["local"]}.')
            print(f'Carga horária: {event["workLoad"]} horas.')
            print(f'Ministrante: {event["minister"]}')
            u.simpleLine()

        # Lista as palestras cadastradas no sistemas
        print("PALESTRAS:")
        u.simpleLine()
        for index, event in enumerate(dd.events["lectures"]):
            # Imprime informações de cada palestra
            print(f"Índice: {index}")
            print(f'Nome: {event["name"]}.')
            print(f'Data: {event["date"]}.')
            print(f'Horário: {event["hours"]}.')
            print(f'Local: {event["local"]}.')
            print(f'Carga horária: {event["workLoad"]}.')
            print(f'Ministrante: {event["minister"]}.')
            u.simpleLine()
        u.back()
        sleep(3)

    def choiceEvent(participant):
        # Exibe uma linha horizontal e um título centralizado para identificar a seção de seleção de eventos.
        u.line()
        u.titleCentered("SELECIONAR EVENTOS")
        u.line()

        # Define limites máximos de workshops e palestras que o participante pode selecionar.
        maxWorkshops = 3
        maxLectures = 4

        # Obtém as seleções anteriores de workshops e palestras do dicionário 'participant'.
        workshopsSelected = participant.get("workshopsSelected", [])
        lecturesSelected = participant.get("lecturesSelected", [])

        # Inicia um loop onde o participante pode selecionar workshops e palestras até atingir os limites máximos.
        while True:
            # Verifica se o participante atingiu o limite máximo de workshops e palestras.
            if (
                len(workshopsSelected) >= maxWorkshops
                and len(lecturesSelected) >= maxLectures
            ):
                # Exibe uma mensagem indicando que o limite máximo foi atingido e encerra o loop.
                print("Você atingiu o limite máximo de workshops e palestras.")
                u.simpleLine()
                break

            # Exibe opções disponíveis para o participante (minicurso ou palestra).
            print("Opções disponíveis:")
            print("M - Minicurso")
            print("P - Palestra")

            # Solicita ao participante que escolha entre minicursos (M) ou palestras (P).
            eventType = input("Informe o tipo do evento (M/P): ").strip().upper()

            # Verifica se o participante escolheu minicurso (M).
            if eventType == "M":
                # Obtém a lista de workshops disponíveis e a seleção atual do participante.
                eventsAvailable = dd.events["workshops"]
                selection = workshopsSelected
                maxSelection = maxWorkshops
            # Verifica se o participante escolheu palestra (P).
            elif eventType == "P":
                # Obtém a lista de palestras disponíveis e a seleção atual do participante.
                eventsAvailable = dd.events["lectures"]
                selection = lecturesSelected
                maxSelection = maxLectures
            else:
                # Exibe uma mensagem de erro se o tipo de evento escolhido for inválido e continua o loop.
                print(
                    'Tipo de evento inválido. Digite "M" para minicurso ou "P" para palestra.'
                )
                u.simpleLine()
                continue

            # Verifica se o participante já selecionou o número máximo de eventos desse tipo.
            if len(selection) >= maxSelection:
                # Exibe uma mensagem indicando que o limite máximo foi atingido e continua o loop.
                print(
                    f"Você já selecionou o máximo de {maxSelection} eventos desse tipo."
                )
                u.simpleLine()
                continue

            # Exibe os eventos disponíveis do tipo escolhido com informações detalhadas.
            print("\nEventos disponíveis:")
            u.simpleLine()
            for index, event in enumerate(eventsAvailable):
                print(f'{index} - {event["name"]} ({event["date"]}, {event["hours"]})')
                u.simpleLine()

            try:
                # Solicita ao participante que insira o número do evento que deseja selecionar.
                indexEvent = int(
                    input("Digite o número do evento que deseja selecionar: ")
                )
                if 0 <= indexEvent < len(eventsAvailable):
                    # Obtém o evento selecionado com base no índice inserido.
                    eventSelected = eventsAvailable[indexEvent]

                    # Verifica se o evento já foi selecionado anteriormente.
                    if eventSelected in selection:
                        # Exibe uma mensagem se o evento já foi selecionado e continua o loop.
                        print(f'Você já selecionou o evento "{eventSelected["name"]}".')
                        u.simpleLine()
                    else:
                        # Registra a seleção do evento e fornece uma mensagem de sucesso.
                        selection.append(eventSelected)
                        participant.setdefault(
                            eventType.lower() + "Selected", []
                        ).append(eventSelected)
                        print(
                            f'Evento "{eventSelected["name"]}" selecionado com sucesso!'
                        )
                        u.simpleLine()
                else:
                    # Exibe uma mensagem de erro se o índice do evento estiver fora dos limites e continua o loop.
                    print("Índice do evento fora dos limites.")
                    u.simpleLine()
            except ValueError:
                # Exibe uma mensagem de erro se o valor inserido não for um número válido e continua o loop.
                print("Índice do evento inválido. Digite um número válido.")

            # Solicita ao participante se deseja selecionar outro evento (S/N).
            choice = input("Deseja selecionar outro evento (S/N)? ").strip().upper()
            u.simpleLine()
            if choice != "S":
                # Encerra o loop se o participante não desejar selecionar outro evento.
                break

    def chooseEvent():
        # Exibe a lista de participantes cadastrados
        Participant.listParticipants()

        # Solicita o nome do participante desejado e formata para capitalizar e remover espaços em excesso
        nameParticipant = (
            str(input("Insira o nome do participante: ")).capitalize().strip()
        )

        participant = None

        # Procura o participante na lista de participantes
        for user in dd.users["participants"]:
            if user["name"] == nameParticipant:
                participant = user
                break

        # Se o participante não for encontrado, exibe uma mensagem e encerra a função
        if participant is None:
            print(
                f"Participante {nameParticipant} não encontrado na nossa base de dados."
            )
            return

        # Chama a função choiceEvent para permitir que o participante selecione eventos
        Event.choiceEvent(participant)

        # Volta para a função anterior após a seleção dos eventos
        u.back()
        sleep(3)
