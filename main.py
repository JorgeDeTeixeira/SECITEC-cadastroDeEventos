import datetime
import os
import sys
from time import sleep
import keyboard


events = {
    'workshops': [
        {
            'typeEvent': 'Minicurso',
            'name': 'Introdução à Programação Python',
            'date': '12/10/2023',
            'hours': '09:00 - 12:00',
            'local': 'Sala 101',
            'workLoad': 3,
            'minister': 'Prof. Ana Silva'
        },
        {
            'typeEvent': 'Minicurso',
            'name': 'Machine Learning Avançado',
            'date': '13/10/2023',
            'hours': '14:00 - 17:00',
            'local': 'Sala 102',
            'workLoad': 3,
            'minister': 'Dr. Pedro Lima'
        },
        {
            'typeEvent': 'Minicurso',
            'name': 'Desenvolvimento Mobile com Flutter',
            'date': '15/10/2023',
            'hours': '09:30 - 12:30',
            'local': 'Sala 103',
            'workLoad': 3,
            'minister': 'Prof. Maria Santos'
        },
        {
            'typeEvent': 'Minicurso',
            'name': 'Análise de Dados com Pandas',
            'date': '15/10/2023',
            'hours': '14:30 - 17:30',
            'local': 'Sala 104',
            'workLoad': 3,
            'minister': 'Dr. Carlos Rodrigues'
        },
        {
            'typeEvent': 'Minicurso',
            'name': 'Introdução à Inteligência Artificial',
            'date': '16/10/2023',
            'hours': '10:00 - 13:00',
            'local': 'Sala 105',
            'workLoad': 3,
            'minister': 'Dra. Sofia Alves'
        }

    ],
    'lectures': [
        {
            'typeEvent': 'Palestra',
            'name': 'Ética na Tecnologia',
            'date': '14/10/2023',
            'hours': '10:30 - 12:00',
            'local': 'Auditório Principal',
            'workLoad': 1.5,
            'minister': 'Dra. Sofia Alves'
        },
        {
            'typeEvent': 'Palestra',
            'name': 'O Impacto das Redes Sociais',
            'date': '14/10/2023',
            'hours': '14:00 - 15:30',
            'local': 'Auditório Principal',
            'workLoad': 1.5,
            'minister': 'Dr. Carlos Santos'
        },
        {
            'typeEvent': 'Palestra',
            'name': 'Inovação em Inteligência Artificial',
            'date': '15/10/2023',
            'hours': '11:00 - 12:30',
            'local': 'Auditório 2',
            'workLoad': 1.5,
            'minister': 'Dra. Laura Fernandes'
        },
        {
            'typeEvent': 'Palestra',
            'name': 'Segurança Cibernética',
            'date': '16/10/2023',
            'hours': '15:30 - 17:00',
            'local': 'Auditório 1',
            'workLoad': 1.5,
            'minister': 'Dr. Pedro Lima'
        },
        {
            'typeEvent': 'Palestra',
            'name': 'Inovações Tecnológicas',
            'date': '16/10/2023',
            'hours': '09:00 - 10:30',
            'local': 'Auditório 3',
            'workLoad': 1.5,
            'minister': 'Dr. Ana Silva'
        }
    ]
}

users = {
    'administrators': [{'name': 'Jorge', 'password': '123456', 'number': 998360879, 'institution': 'UFERSA'}],
    'participants': [{'name': 'João',
                      'number': '999999999',
                      'institution': 'UFERSA',
                      'workshopsSelected': [],
                      'lecturesSelected': []}]
}


def line():
    # Imprime uma linha horizontal formada por 30 caracteres "="
    print('=' * 40)


def simpleLine():
    # Imprime uma linha horizontal formada por 30 caracteres "-"
    print('-' * 60)


def titleCentered(title):
    # Imprime o "titulo" centralizado em uma linha de 30 caracteres
    print(f'{title:^40}')


def clearTerminal():
    # A função os.system() permite executar comandos no sistema operacional.
    # Dependendo do sistema operacional, ele executará 'cls' (Windows) ou 'clear' (Linux/Unix) para limpar a tela do terminal.
    os.system('cls' if os.name == 'nt' else 'clear')


def back():
    print("Pressione 'Q' para sair")
    simpleLine()
    while True:
        if keyboard.is_pressed('q'):
            print('Saindo...')
            break


def validatePassword(password):
    cont = 0  # Inicializa um contador de tentativas com valor 0

    # Enquanto a senha não estiver na lista de senhas dos administradores
    while password not in [admin['password'] for admin in users['administrators']]:
        simpleLine()
        print('ERRO! Senha incorreta!')
        cont += 1  # Incrementa o contador de tentativas

        # Exibe o número de tentativas restantes (até 3)
        print(f'Mais {3 - cont} tentativas.')
        simpleLine()

        # Solicita novamente a senha ao usuário
        password = str(input('Informe a senha:')).strip()

        # Se o número de tentativas chegar a 3, encerra o programa
        if cont == 2:
            print('Tentativas esgotadas! Programa encerrado!')
            sys.exit()  # Encerra o programa


def validateDate(date):
    try:
        # Tenta criar um objeto datetime a partir da string de data usando i formato "%d/%m%Y"
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        # Se ocorrer uma exceção ValueErro, a data é inválida, retorna False
        return False


def validateHours(hours):
    try:
        # Tenta criar um objeto datetime a partir da string de horário usando o formato "%H:%M"
        datetime.datetime.strptime(hours, '%H:%M')
        # Se a conversão for bem-sucedida, o horário é válido, retorna True
        return True
    except ValueError:
        # Se ocorrer uma exceção ValueError, o horário é inválido, retorna False
        return False


def registerParticipant():
    try:
        line()
        titleCentered('CADASTRO DE PARTICIPANTE')
        line()

        # Solicita ao usuário que informe o nome
        name = str(input('Informe seu nome: ')).strip().capitalize()

        # Validação do nome: verifica se o nome não está em branco
        while not name:
            name = str(input('Nome inválido. Informe seu nome: ')
                       ).strip().capitalize()

        # Solicita ao usuário que informe o telefone celular
        number = str(input('Informe seu telefone (9 dígitos apenas): '))

        # Validação do telefone: verifica se é um número de 9 dígitos
        while not number.isdigit() or len(number) != 9:
            number = str(input(
                'Número de telefone inválido. Certifique-se de inserir 9 dígitos númericos: '))

        # Solicita ao usuário que informe a instituição vinculada
        institution = str(input('Instituição vinculada: ')
                          ).strip().capitalize()

        # Validação da instituição: verifica se o nome não está em branco
        while not institution:
            institution = str(
                input('Nome inválido. Informe o nome da instituição: ')).strip().capitalize()

        newParticipant = {
            'name': name,
            'number': number,
            'institution': institution,
            'minicoursesSelected': [],  # Lista de minicursos selecionados vazia
            'lecturesSelected': []  # Lista de palestras selecionadas vazia
        }

        # Adicionar o novo participante á lista de participantes (users['participant'])
        users['participants'].append(newParticipant)

        line()
        print(f'Usuário {name} adicionado com sucesso!')
        line()

        # Agora, vamos aguardar até que o usuário pressione 'Q' para sair
        back()

        sleep(2)
    except Exception as e:
        # Lidar com exceções em gerais e fornecer informçaões sobre o erro
        print(f'Ocorreu um erro durante o cadastro: {str(e)}')


def registerEvent():
    try:
        line()
        titleCentered('CADASTRO DE EVENTOS')
        line()

        # Verifica o nome do administrador com permissão de cadastrar algum evento
        nameAdmin = str(input(
            'Informe o nome do administrador com permissão de cadastro: ')).strip().capitalize()

        # Verifica se o nome do administrador está na lista de administradores
        if nameAdmin in [admin['name'] for admin in users['administrators']]:
            print(F'Usuário:{nameAdmin}.')
            # Solicita a senha do administrador (Com até 3 tentativas)
            password = str(input('Informe a senha (3 tentativas): '))
            validatePassword(password)

            simpleLine()
            titleCentered('ACESSO LIBERADO')
            simpleLine()

            # Exibe opções de cadastro (Minicurso ou palestras)
            print('Opções de cadastro:')
            print('M - Minicurso')
            print('P - Palestra')

            # Solicita o tipo de evento desejado (M ou P)
            t = str(input(
                'O que você deseja cadastrar? [M - Minicurso | P - Palestra]: ')).strip().upper()[0]

            # Define o tipo de evento com base na escolha do administrador
            if t == 'M':
                typeEvent = 'Minicurso'
            elif t == 'P':
                typeEvent = 'Palestra'
            else:
                print('Tipo de evento inválido.')
                return

            # Solicita informações do evento(nome, local, data, horário, carga horária, ministrante)
            line()
            titleCentered(f'CADASTRO DE {typeEvent.upper()}')
            line()

            # Solicita o nome do evento
            name = str(input('Nome do evento: ')).strip().capitalize()

            # Validação do nome do evento: não pode estar em branco
            while not name:
                name = str(input('Nome vazio. Nome do evento:'))
            # Solicita o local do evento onde será realizado

            local = str(input('Informe o local:')).strip().capitalize()

            while not local:
                local = str(input('Local vazio. Local do evento: '))

            # Solicita a data do evento
            date = str(input('Informe a data (XX/XX/XXXX): '))

            # Validação da data usando a função validarData(data)
            while validateDate(date) == False:
                date = str(
                    input('Use o formato correto. Informe a data (XX/XX/XXXX): '))
                if validateDate(date):
                    break

            # Solicita horario do evento
            hours = str(input('Informe o horário (XX-XX): '))

            # Validação do horário usando a função validarHorario(horario)
            while validateHours(hours) == False:
                hours = str(
                    input('Use o formato correto. Informe o horário (XX:XX): '))
                if validateHours(hours):
                    break

            # Solicita a carga horária do evento (em horas)
            while True:
                # Solicita a carga horária em horas
                workLoad = str(input('Carga horária (em horas): '))
                # Validação da carga horária: valor positivo
                if workLoad.isdigit() and int(workLoad) > 0:
                    workLoad = int(workLoad)
                    break
                else:
                    print('Valor de carga horária inválida. Informe um valor positivo.')

            # Solicita o nome do ministrante para o evento
            minister = str(input('Informe o ministrante: ')
                           ).strip().capitalize()

            # Validação do nome do ministrante: não pode estar em branco
            while not minister:
                minister = str(
                    input('Ministrante vazio. Informe o ministrante: '))

            # Cria um dicionário com as informações do novo evento
            newEvent = {
                'typeEvent': typeEvent,
                'name': name,
                'date': date,
                'local': local,
                'hours': hours,
                'workLoad': workLoad,
                'minister': minister
            }

            # Adiciona um novo evento á lista de eventos correspodente (Minicursos ou paletra)
            if t == 'M':
                events['workshops'].append(newEvent)
            elif t == 'P':
                events['lectures'].append(newEvent)
            else:
                print('TIPO DE EVENTO INVÁLIDO!')

            # Imprime uma mensagem de sucesso informando que o evento foi adicionado
            simpleLine()
            print(f'{typeEvent} {name} adicionado com sucesso ao sistema!')
            simpleLine()
        else:
            # Caso o nome do admnistrador não seja encontrado ou a senha esteja incorreta
            print(
                'PERMISSÃO NEGADA! Nome de administrador não encontrado ou senha incorreta!')

        back()
        sleep(2)
    except Exception as e:
        # Lidar com exceções em geral e fornecer informações sobre o erro
        print(f'Ocorreu um erro durante o cadastro do evento: {str(e)}')


def listEvents():
    line()
    titleCentered('LISTA DE EVENTOS')
    line()

    # Lista os minicursos cadastrados no sistema
    print('MINICURSOS:')
    simpleLine()
    for index, event in enumerate(events['workshops']):
        # Imprime informações de cada minicurso
        print(f'Índice: {index}.')
        print(f'Nome: {event["name"]}.')
        print(f'Data: {event["date"]}.')
        print(f'Horário: {event["hours"]}.')
        print(f'Local: {event["local"]}.')
        print(f'Carga horária: {event["workLoad"]} horas.')
        print(f'Ministrante: {event["minister"]}')
        simpleLine()

    # Lista as palestras cadastradas no sistemas
    print('PALESTRAS:')
    simpleLine()
    for index, event in enumerate(events['lectures']):
        # Imprime informações de cada palestra
        print(f'Índice: {index}')
        print(f'Nome: {event["name"]}.')
        print(f'Data: {event["date"]}.')
        print(f'Horário: {event["hours"]}.')
        print(f'Local: {event["local"]}.')
        print(f'Carga horária: {event["workLoad"]}.')
        print(f'Ministrante: {event["minister"]}.')
        simpleLine()
    back()
    sleep(3)


def listParticipants():
    line()
    titleCentered('LISTA DE PARTICIPANTES')
    line()

    # Loop para percorrer a lista de participantes e exibi-los
    for index, user in enumerate(users['participants']):
        # Exibe o índice e o nome do participante
        print(f'Índice: {index + 1} - Nome: {user["name"]} ')
        simpleLine()  # Função para imprimir uma linha divisória


def choiceEvent(participant):
    # Exibe uma linha horizontal e um título centralizado para identificar a seção de seleção de eventos.
    line()
    titleCentered('SELECIONAR EVENTOS')
    line()

    # Define limites máximos de workshops e palestras que o participante pode selecionar.
    maxWorkshops = 3
    maxLectures = 4

    # Obtém as seleções anteriores de workshops e palestras do dicionário 'participant'.
    workshopsSelected = participant.get('workshopsSelected', [])
    lecturesSelected = participant.get('lecturesSelected', [])

    # Inicia um loop onde o participante pode selecionar workshops e palestras até atingir os limites máximos.
    while True:
        # Verifica se o participante atingiu o limite máximo de workshops e palestras.
        if len(workshopsSelected) >= maxWorkshops and len(lecturesSelected) >= maxLectures:
            # Exibe uma mensagem indicando que o limite máximo foi atingido e encerra o loop.
            print('Você atingiu o limite máximo de workshops e palestras.')
            simpleLine()
            break

        # Exibe opções disponíveis para o participante (minicurso ou palestra).
        print('Opções disponíveis:')
        print('M - Minicurso')
        print('P - Palestra')

        # Solicita ao participante que escolha entre minicursos (M) ou palestras (P).
        event_type = input('Informe o tipo do evento (M/P): ').strip().upper()

        # Verifica se o participante escolheu minicurso (M).
        if event_type == 'M':
            # Obtém a lista de workshops disponíveis e a seleção atual do participante.
            eventsAvailable = events['workshops']
            selection = workshopsSelected
            maxSelection = maxWorkshops
        # Verifica se o participante escolheu palestra (P).
        elif event_type == 'P':
            # Obtém a lista de palestras disponíveis e a seleção atual do participante.
            eventsAvailable = events['lectures']
            selection = lecturesSelected
            maxSelection = maxLectures
        else:
            # Exibe uma mensagem de erro se o tipo de evento escolhido for inválido e continua o loop.
            print(
                'Tipo de evento inválido. Digite "M" para minicurso ou "P" para palestra.')
            simpleLine()
            continue

        # Verifica se o participante já selecionou o número máximo de eventos desse tipo.
        if len(selection) >= maxSelection:
            # Exibe uma mensagem indicando que o limite máximo foi atingido e continua o loop.
            print(
                f'Você já selecionou o máximo de {maxSelection} eventos desse tipo.')
            simpleLine()
            continue

        # Exibe os eventos disponíveis do tipo escolhido com informações detalhadas.
        print('\nEventos disponíveis:')
        simpleLine()
        for index, event in enumerate(eventsAvailable):
            print(
                f'{index} - {event["name"]} ({event["date"]}, {event["hours"]})')
            simpleLine()

        try:
            # Solicita ao participante que insira o número do evento que deseja selecionar.
            indexEvent = int(
                input('Digite o número do evento que deseja selecionar: '))
            if 0 <= indexEvent < len(eventsAvailable):
                # Obtém o evento selecionado com base no índice inserido.
                eventSelected = eventsAvailable[indexEvent]

                # Verifica se o evento já foi selecionado anteriormente.
                if eventSelected in selection:
                    # Exibe uma mensagem se o evento já foi selecionado e continua o loop.
                    print(
                        f'Você já selecionou o evento "{eventSelected["name"]}".')
                    simpleLine()
                else:
                    # Registra a seleção do evento e fornece uma mensagem de sucesso.
                    selection.append(eventSelected)
                    participant.setdefault(
                        event_type.lower() + 'Selected', []).append(eventSelected)
                    print(
                        f'Evento "{eventSelected["name"]}" selecionado com sucesso!')
                    simpleLine()
            else:
                # Exibe uma mensagem de erro se o índice do evento estiver fora dos limites e continua o loop.
                print('Índice do evento fora dos limites.')
                simpleLine()
        except ValueError:
            # Exibe uma mensagem de erro se o valor inserido não for um número válido e continua o loop.
            print('Índice do evento inválido. Digite um número válido.')

        # Solicita ao participante se deseja selecionar outro evento (S/N).
        choice = input(
            'Deseja selecionar outro evento (S/N)? ').strip().upper()
        simpleLine()
        if choice != 'S':
            # Encerra o loop se o participante não desejar selecionar outro evento.
            break


def chooseEvent():
    # Exibe a lista de participantes cadastrados
    listParticipants()

    # Solicita o nome do participante desejado e formata para capitalizar e remover espaços em excesso
    nameParticipant = str(
        input('Insira o nome do participante: ')).capitalize().strip()

    participant = None

    # Procura o participante na lista de participantes
    for user in users['participants']:
        if user['name'] == nameParticipant:
            participant = user
            break

    # Se o participante não for encontrado, exibe uma mensagem e encerra a função
    if participant is None:
        print(
            f'Participante {nameParticipant} não encontrado na nossa base de dados.')
        return

    # Chama a função choiceEvent para permitir que o participante selecione eventos
    choiceEvent(participant)

    # Volta para a função anterior após a seleção dos eventos
    back()
    sleep(3)


def generateCertificate():
    line()
    titleCentered('GERAR CERTIFICADO')
    line()

    listParticipants()

    # Loop para selecionar um participante com tratamento de exceções
    while True:
        try:
            choice = int(input('Selecione o número do participante: '))
            if 1 <= choice <= len(users['participants']):
                participant = users['participants'][choice - 1]
                break
            else:
                print('Número de participante inválido. Tente novamente')
        except ValueError:
            print('Número de participante inválido. Tente novamente.')

    # Exibe título com o nome do participante selecionado
    line()
    titleCentered(F'EVENTOS INSCRITOS POR PARTICIPANTE: {participant["name"]}')
    line()

    # Exibe informações dos workshops inscritos pelo participante, se houver
    if 'workshopsSelected' in participant:
        simpleLine()
        print('Minicursos inscritos:')
        simpleLine()
        for event in participant['workshopsSelected']:
            print(f'Nome: {event["name"]}')
            print(f'Data: {event["date"]}')
            print(f'Horário: {event["hours"]}')
            print(f'Local: {event["local"]}')
            print(f'Carga Horária: {event["workLoad"]} horas')
            print(f'Ministrante: {event["minister"]}')
            simpleLine()

    # Exibe informações das palestras inscritas pelo participante, se houver
    if 'lecturesSelected' in participant:
        simpleLine()
        print('Palestras inscritas:')
        simpleLine()
        for event in participant['lecturesSelected']:
            print(f'Nome: {event["name"]}')
            print(f'Data: {event["date"]}')
            print(f'Horário: {event["hours"]}')
            print(f'Local: {event["local"]}')
            print(f'Carga Horária: {event["workLoad"]} horas')
            print(f'Ministrante: {event["minister"]}')
            simpleLine()

    # Calcula a carga horária total de todos os eventos inscritos
    totalWorkLoad = 0
    if 'workshopsSelected' in participant:
        totalWorkLoad += sum(
            event['workLoad'] for event in participant['workshopsSelected'])
    if 'lecturesSelected' in participant:
        totalWorkLoad += sum(
            event['workLoad'] for event in participant['lecturesSelected'])

    # Exibe a carga horária total
    print(f'Carga Horária Total: {totalWorkLoad} horas.')

    simpleLine()

    # Obtém a data atual e exibe como data de emissão do certificado
    currentDate = datetime.date.today()
    issuanceDate = currentDate.strftime('%d/%m/%Y')
    print(f'Certificado emitido em {issuanceDate}.')

    simpleLine()

    # Chama a função 'back' para retornar ao menu principal
    back()
    sleep(3)


def mainMenu():
    while True:
        line()
        titleCentered('MENU DE OPÇÕES')
        line()

        # Exibe as opções do menu numeradas
        print('1 - Cadastro de participantes.')
        print('2 - Cadastro de eventos.')
        print('3 - Listar eventos do sistema.')
        print('4 - Escolher evento.')
        print('5 - Gerar certificado.')
        print('6 - Sair.')

        # Solicita a escolha do usuário
        choice = str(input('Informe sua opção:'))
        clearTerminal()

        if choice == '1':
            registerParticipant()
        elif choice == '2':
            registerEvent()
        elif choice == '3':
            listEvents()
        elif choice == '4':
            chooseEvent()
        elif choice == '5':
            generateCertificate()
        elif choice == '6':
            # Imprime uma mensagem de saída e sai do loop infinito, encerrando o programa
            print('OBRIGADO POR USAR NOSSO SISTEMA! FIM DO PROGRAMA!')
            break
        else:
            # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        # Limpa o terminal depois de sair do menu
        sleep(2)
        clearTerminal()


mainMenu()
