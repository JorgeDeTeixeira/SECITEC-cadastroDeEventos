import datetime
import os
import sys

eventos = {
    'minicursos': [
        {
            'tipo': 'Minicurso',
            'nome': 'Introdução à Programação Python',
            'data': '12/10/2023',
            'local': 'Sala 101',
            'horario': '09:00 - 12:00',
            'cargaHoraria': 3,
            'ministrante': 'Prof. Ana Silva'
        },
        {
            'tipo': 'Minicurso',
            'nome': 'Machine Learning Básico',
            'data': '13/10/2023',
            'local': 'Sala 102',
            'horario': '14:00 - 17:00',
            'cargaHoraria': 3,
            'ministrante': 'Dr. Pedro Lima'
        },
        {
            'tipo': 'Minicurso',
            'nome': 'Desenvolvimento Web com Django',
            'data': '15/10/2023',
            'local': 'Sala 103',
            'horario': '09:30 - 12:30',
            'cargaHoraria': 3,
            'ministrante': 'Prof. Maria Santos'
        },
        {
            'tipo': 'Minicurso',
            'nome': 'Introdução à Ciência de Dados',
            'data': '15/10/2023',
            'local': 'Sala 104',
            'horario': '14:30 - 17:30',
            'cargaHoraria': 3,
            'ministrante': 'Dr. Carlos Rodrigues'
        }
    ],
    'palestras': [
        {
            'tipo': 'Palestra',
            'nome': 'Ética na Tecnologia',
            'data': '14/10/2023',
            'local': 'Auditório Principal',
            'horario': '10:30 - 12:00',
            'cargaHoraria': 1.5,
            'ministrante': 'Dra. Sofia Alves'
        },
        {
            'tipo': 'Palestra',
            'nome': 'O Futuro da Robótica',
            'data': '14/10/2023',
            'local': 'Auditório Principal',
            'horario': '15:00 - 16:30',
            'cargaHoraria': 1.5,
            'ministrante': 'Dr. André Oliveira'
        },
        {
            'tipo': 'Palestra',
            'nome': 'Inteligência Artificial Aplicada em Saúde',
            'data': '16/10/2023',
            'local': 'Auditório 2',
            'horario': '11:00 - 12:30',
            'cargaHoraria': 1.5,
            'ministrante': 'Dra. Laura Fernandes'
        },
        {
            'tipo': 'Palestra',
            'nome': 'Tendências em Tecnologia da Informação',
            'data': '17/10/2023',
            'local': 'Auditório 1',
            'horario': '10:00 - 11:30',
            'cargaHoraria': 1.5,
            'ministrante': 'Dr. Rafael Silva'
        },
        {
            'tipo': 'Palestra',
            'nome': 'Python',
            'data': '29/10/2023',
            'local': 'Auditório 1',
            'horario': '10:00 - 11:30',
            'cargaHoraria': 1.5,
            'ministrante': 'Dr. Rafael Silva'
        }
    ]
}

users = {
    'admins': [{'name': 'Jorge', 'pass': '123456', 'telefone': 998360879, 'instituição': 'UFERSA'}],
    'user': [{'name': 'João',
              'telefone': '999999999',
              'instituição': 'UFERSA',
              'minicursoSelecionados': [],
              'palestrasSelecionadas': []}]
}


def linha():
    # Imprime uma linha horizontal formada por 30 caracteres "="
    print('=' * 30)


def linhaSimples():
    # Imprime uma linha horizontal formada por 30 caracteres "-"
    print('-' * 30)


def tituloCentralizado(titulo):
    # Imprime o "titulo" centralizado em uma linha de 30 caracteres
    print(f'"{titulo:^30}"')


def validarSenha(password):
    cont = 0  # Inicializa um contador de tentativas com valor 0

    # Enquanto a senha não estiver na lista de senhas dos administradores
    while password not in [admin['pass'] for admin in users['admins']]:
        linhaSimples()  # Função linhaSimples() cria uma linha horizontal simples para separar mensagens
        print('ERRO! Senha incorreta!')
        cont += 1  # Incrementa o contador de tentativas

        # Exibe o número de tentativas restantes (até 3)
        print(f'Mais {3 - cont} tentativas.')
        linhaSimples()

        # Solicita novamente a senha ao usuário
        password = str(input('Informe a senha: ')).strip()

        # Se o número de tentativas chegar a 3, encerra o programa
        if cont == 3:
            print('Tentativas esgotadas! Programa encerrado!')
            sys.exit()  # Encerra o programa


def validarData(data):  # Função para validar uma data no formato "dia/mês/ano"
    try:
        # Tenta criar um objeto datetime a partir da string de data usando o formato "%d/%m/%Y"
        datetime.datetime.strptime(data, '%d/%m/%Y')
        # Se a conversão for bem-sucedida, a data é válida, retorna True
        return True
    except ValueError:
        # Se ocorrer uma exceção ValueError, a data é inválida, retorna False
        return False


def validarHorario(horario):  # Função para validar um horário no formato "hora:minuto"
    try:
        # Tenta criar um objeto datetime a partir da string de horário usando o formato "%H:%M"
        datetime.datetime.strptime(horario, '%H:%M')
        # Se a conversão for bem-sucedida, o horário é válido, retorna True
        return True
    except ValueError:
        # Se ocorrer uma exceção ValueError, o horário é inválido, retorna False
        return False


def cadastrarEvento():
    # Imprime uma linha para separar visualmente a seção de cadastro de eventos
    linha()
    # Função tituloCentralizado() deve imprimir um título centralizado para a seção de cadastro de eventos
    tituloCentralizado('CADASTRO DE EVENTOS')
    linha()

    # Solicita o nome do administrador com permissão de cadastro
    nomeAdmin = str(input(
        'Informe o nome do administrador com permissão de cadastro: ')).strip().capitalize()

    # Verifica se o nome do administrador está na lista de administradores
    if nomeAdmin in [admin['name'] for admin in users['admins']]:
        # Solicita a senha do administrador (com até 3 tentativas)
        senha = str(input('Informe a senha (3 tentativas): '))
        validarSenha(senha)

        # Acesso concedido, o administrador pode cadastrar eventos

        # Exibe opções de cadastro (Minicurso ou Palestra)
        linha()
        print('Opções de cadastro:')
        print('M - Minicurso')
        print('P - Palestra')

        # Solicita o tipo de evento desejado (M ou P)
        tipo = str(input(
            'O que você deseja cadastrar? [M - minicurso | P - Palestra]: ')).strip().upper()[0]

        # Define o tipo de evento com base na escolha do administrador
        if tipo == 'M':
            tipoEvento = 'Minicurso'
        elif tipo == 'P':
            tipoEvento = 'Palestra'
        else:
            print('Tipo de evento inválido.')
            return

        # Solicita informações do evento (nome, local, data, horário, carga horária, ministrante)
        linha()
        print(f'{f"Cadastro de {tipoEvento}":^30}')
        linha()
        nome = str(input('Nome do evento: '))

        # Validação do nome do evento: não pode estar em branco
        while not nome:
            nome = str(input('Nome vazio. Nome do evento: '))

        local = str(input('Informe o local: '))

        # Validação do local do evento: não pode estar em branco
        while not local:
            local = str(input('Local vazio. Local do evento: '))

        data = str(input('Informe a data (XX/XX/XXXX): '))

        # Validação da data usando a função validarData(data)
        while validarData(data) == False:
            data = str(
                input('Use o formato correto. Informe a data (XX/XX/XXXX): '))
            if validarData(data):
                break

        horario = str(input('Informe o horário (XX:XX): '))

        # Validação do horário usando a função validarHorario(horario)
        while validarHorario(horario) == False:
            horario = str(
                input('Use o formato correto. Informe o horário (XX:XX): '))
            if validarHorario(horario):
                break

        # Solicita a carga horária do evento (em horas)
        while True:
            cargaHoraria = str(input('Carga horária (em horas): ')).strip()
            # Validação da carga horária: deve ser um valor positivo
            if cargaHoraria.isdigit() and int(cargaHoraria) > 0:
                cargaHoraria = int(cargaHoraria)
                break
            else:
                print('Valor de carga horária inválido. Informe um valor positivo.')

        ministrante = str(input('Informe o ministrante: '))

        # Validação do nome do ministrante: não pode estar em branco
        while not ministrante:
            ministrante = str(
                input('Ministrante vazio. Informe o ministrante: '))

        # Cria um dicionário com as informações do novo evento
        novoEvento = {
            'tipo': tipo,
            'nome': nome,
            'data': data,
            'local': local,
            'horario': horario,
            'cargaHoraria': cargaHoraria,
            'ministrante': ministrante
        }

        # Adiciona o novo evento à lista de eventos correspondente (minicurso ou palestra)
        if tipo == 'M':
            eventos['minicursos'].append(novoEvento)
        elif tipo == 'P':
            eventos['palestras'].append(novoEvento)
        else:
            print('TIPO INVÁLIDO!')

        # Imprime uma mensagem de sucesso informando que o evento foi adicionado
        print(f'{nome} adicionado com sucesso!')
    else:
        # Caso o nome do administrador não seja encontrado ou a senha esteja incorreta
        print('PERMISSÃO NEGADA! Nome de administrador não encontrado ou senha incorreta.')


def listarEventos():
    # Imprime uma linha para separar visualmente a seção de listagem de eventos
    linha()
    # Função tituloCentralizado() deve imprimir um título centralizado para a seção de listagem de eventos
    tituloCentralizado('LISTA DE EVENTOS')
    linha()

    # Lista os minicursos
    print('Minicursos:')
    for indice, evento in enumerate(eventos['minicursos']):
        # Imprime informações de cada minicurso
        print(f'Índice: {indice}')
        print(f'Nome: {evento["nome"]}')
        print(f'Data: {evento["data"]}')
        print(f'Local: {evento["local"]}')
        print(f'Horário: {evento["horario"]}')
        print(f'Carga Horária: {evento["cargaHoraria"]} horas')
        print(f'Ministrante: {evento["ministrante"]}')
        # Função linha() deve imprimir uma linha para separar visualmente os eventos
        linha()

    # Lista as palestras
    print('Palestras:')
    for indice, evento in enumerate(eventos['palestras']):
        # Imprime informações de cada palestra
        print(f'Índice: {indice}')
        print(f'Nome: {evento["nome"]}')
        print(f'Data: {evento["data"]}')
        print(f'Local: {evento["local"]}')
        print(f'Horário: {evento["horario"]}')
        print(f'Carga Horária: {evento["cargaHoraria"]} horas')
        print(f'Ministrante: {evento["ministrante"]}')
        # Função linha() deve imprimir uma linha para separar visualmente os eventos
        linha()


def listarParticipantes():
    # Imprime um título centralizado para a seção de listagem de participantes
    print(f"{'Todos os Participantes:':^30}")
    # Chama a função linha() para imprimir uma linha para separar visualmente a lista
    linha()

    # Itera sobre a lista de participantes no dicionário 'users'
    for participante in users['user']:
        # Obtém informações do participante, como nome, telefone e instituição
        nome = participante['name']
        telefone = participante['telefone']
        instituicao = participante['instituição']

        # Imprime as informações do participante formatadas
        print(f'Nome: {nome} - Instituição: {instituicao}')


def cadastrarParticipante():
    # Imprime uma linha para separar visualmente a seção de cadastro de usuário
    linha()
    # Função tituloCentralizado() deve imprimir um título centralizado para a seção de cadastro de usuário
    tituloCentralizado('CADASTRO DE USUÁRIO')
    linha()

    # Solicita ao usuário que informe o nome
    name = str(input('Informe seu nome:')).strip().capitalize()

    # Validação do nome: verifica se o nome não está em branco
    while not name:
        name = input('Nome inválido. Informe seu nome: ').strip().capitalize()

    # Solicita ao usuário que informe o telefone
    telefone = str(input('Informe seu telefone (9 dígitos apenas):'))

    # Validação do telefone: verifica se é um número de 9 dígitos
    while not telefone.isdigit() or len(telefone) != 9:
        telefone = str(input(
            'Número de telefone inválido. Certifique-se de inserir 9 dígitos numéricos:'))

    # Solicita ao usuário que informe a instituição vinculada
    instituição = str(input('Instituição vinculada:')).strip().capitalize()

    # Validação da instituição: verifica se o nome não está em branco
    while not instituição:
        instituição = input(
            'Nome inválido. Informe o nome da instituição: ').strip().capitalize()

    # Cria um dicionário com as informações do novo participante
    novoParticipante = {
        'name': name,
        'telefone': telefone,
        'instituição': instituição,
        'minicursoSelecionados': [],   # Lista de minicursos selecionados vazia
        'palestrasSelecionadas': []    # Lista de palestras selecionadas vazia
    }

    # Adiciona o novo participante à lista de participantes (users['user'])
    users['user'].append(novoParticipante)

    # Imprime uma linha para separar visualmente a mensagem de sucesso
    linha()
    # Imprime uma mensagem de sucesso informando que o usuário foi adicionado
    print(f'Usuário {name} adicionado com sucesso!')
    # Imprime uma linha para separar visualmente a mensagem de sucesso
    linha()


def escolherEvento():
    # Imprime uma linha para separar visualmente a seção de seleção de participante
    linha()
    # Imprime um título centralizado para a seção de seleção de participante
    tituloCentralizado('SELECIONAR PARTICIPANTE')
    linha()

    # Lista todos os participantes disponíveis
    listarParticipantes()

    # Solicita ao usuário que informe o nome do participante
    nomeParticipante = str(
        input('Informe o nome do participante: ')).strip().capitalize()

    # Inicializa a variável "participante" como None
    participante = None

    # Procura o participante com o nome informado na lista de participantes
    for user in users['user']:
        if user['name'] == nomeParticipante:
            participante = user
            break

    # Se o participante não for encontrado, exibe uma mensagem e sai da função
    if participante is None:
        print('Participante não encontrado!')
        return

    # Imprime uma linha para separar visualmente a seção de seleção de eventos
    linha()
    # Imprime um título centralizado para a seção de seleção de eventos
    tituloCentralizado('SELECIONAR EVENTOS')
    linha()

    # Lista todos os eventos disponíveis
    listarEventos()

    # Obtém as seleções atuais de minicursos e palestras do participante
    selecaoMinicursos = participante.get('minicursoSelecionados', [])
    selecaoPalestras = participante.get('palestrasSelecionadas', [])

    # Define o número máximo de minicursos e palestras que o participante pode selecionar
    maxMinicursos = 3
    maxPalestras = 4

    # Entra em um loop que permite ao participante selecionar eventos até atingir o limite máximo
    while True:
        # Verifica se o participante atingiu o limite máximo de minicursos e palestras
        if len(selecaoMinicursos) >= maxMinicursos and len(selecaoPalestras) >= maxPalestras:
            print('Você atingiu o limite máximo de minicursos e palestras.')
            break

        # Solicita ao usuário que digite o tipo de evento (M para Minicurso ou P para Palestra)
        tipoEvento = input(
            'Digite o tipo do evento (M - Minicurso ou P - Palestra): ').strip().upper()

        # Verifica se o tipo de evento é válido (M ou P)
        if tipoEvento == 'M':
            eventosDisponiveis = eventos['minicursos']
            selecao = selecaoMinicursos
            maxSelecao = maxMinicursos
        elif tipoEvento == 'P':
            eventosDisponiveis = eventos['palestras']
            selecao = selecaoPalestras
            maxSelecao = maxPalestras
        else:
            print(
                'Tipo de evento inválido. Digite "M" para Minicurso ou "P" para Palestra.')
            continue

        # Verifica se o participante já selecionou o número máximo de eventos do tipo escolhido
        if len(selecao) >= maxSelecao:
            print(
                f'Você já selecionou o máximo de {maxSelecao} eventos desse tipo.')
            continuar = input(
                'Deseja selecionar outro evento? (S/N): ').strip().upper()
            if continuar != 'S':
                break

        try:
            # Solicita ao usuário que digite o índice do evento que deseja selecionar
            indiceEvento = int(
                input('Digite o índice do evento que deseja selecionar: '))
            if 0 <= indiceEvento < len(eventosDisponiveis):
                eventoSelecionado = eventosDisponiveis[indiceEvento]

                # Verifica se o evento já foi selecionado pelo participante
                if eventoSelecionado in selecao:
                    print(
                        f'Você já selecionou o evento "{eventoSelecionado["nome"]}".')
                else:
                    # Adiciona o evento à seleção do participante e atualiza seus dados
                    selecao.append(eventoSelecionado)
                    participante.setdefault(
                        tipoEvento.lower() + 'Selecionadas', []).append(eventoSelecionado)
                    linha()
                    print(
                        f'Evento "{eventoSelecionado["nome"]}" selecionado com sucesso!')
                    linha()
            else:
                print('Índice do evento fora dos limites.')
        except ValueError:
            print('Índice do evento inválido. Digite um número válido.')

        continuar = input(
            'Deseja selecionar outro evento? (S/N): ').strip().upper()
        if continuar != 'S':
            break


def gerarCertificado():
    # Imprime uma linha para separar visualmente a seção do certificado
    linha()
    # Função tituloCentralizado() deve imprimir um título centralizado para a seção de geração de certificados
    tituloCentralizado('GERAR CERTIFICADOS')
    linha()

    # Exibe a lista de participantes para que o usuário possa escolher
    print('Lista de Participantes:')
    for i, participante in enumerate(users['user']):
        print(f'{i + 1}. {participante["name"]}')

    # Solicita ao usuário que selecione o número do participante
    while True:
        try:
            escolha = int(input('Selecione o número do participante: '))
            if 1 <= escolha <= len(users['user']):
                participante = users['user'][escolha - 1]
                break
            else:
                print('Número de participante inválido. Tente novamente.')
        except ValueError:
            print('Número de participante inválido. Tente novamente.')

    # Imprime uma linha para separar visualmente a seção do certificado
    linha()
    # Função tituloCentralizado() deve imprimir um título centralizado com o nome do participante
    tituloCentralizado(
        f'EVENTOS INSCRITOS POR PARTICIPANTE: {participante["name"]}')
    linha()

    # Verifica se o participante está inscrito em minicursos e exibe informações sobre eles
    if 'minicursoSelecionados' in participante:
        print('Minicursos inscritos:')
        # Função linhaSimples() deve imprimir uma linha simples para separar a lista de eventos
        linhaSimples()
        for evento in participante['minicursoSelecionados']:
            # Exibe informações sobre cada minicurso
            print(f'Nome: {evento["nome"]}')
            print(f'Data: {evento["data"]}')
            print(f'Horário: {evento["horario"]}')
            print(f'Carga Horária: {evento["cargaHoraria"]} horas')
            print(f'Ministrante: {evento["ministrante"]}')
            # Função linha() deve imprimir uma linha para separar visualmente os eventos
            linha()

    # Verifica se o participante está inscrito em palestras e exibe informações sobre elas
    if 'palestrasSelecionadas' in participante:
        print('Palestras inscritas:')
        # Função linhaSimples() deve imprimir uma linha simples para separar a lista de eventos
        linhaSimples()
        for evento in participante['palestrasSelecionadas']:
            # Exibe informações sobre cada palestra
            print(f'Nome: {evento["nome"]}')
            print(f'Data: {evento["data"]}')
            print(f'Horário: {evento["horario"]}')
            print(f'Carga Horária: {evento["cargaHoraria"]} horas')
            print(f'Ministrante: {evento["ministrante"]}')
            # Função linha() deve imprimir uma linha para separar visualmente os eventos
            linha()

    # Calcula a carga horária total do participante com base nas atividades selecionadas
    carga_horaria_total = 0
    if 'minicursoSelecionados' in participante:
        carga_horaria_total += sum(
            evento['cargaHoraria'] for evento in participante['minicursoSelecionados'])
    if 'palestrasSelecionadas' in participante:
        carga_horaria_total += sum(
            evento['cargaHoraria'] for evento in participante['palestrasSelecionadas'])

    # Exibe a carga horária total do participante
    print(f'Carga Horária Total: {carga_horaria_total} horas')

    # Imprime uma linha para separar visualmente a seção do certificado
    linha()

    # Obtém a data atual e formata como uma string
    data_atual = datetime.date.today()
    data_emissao = data_atual.strftime('%d/%m/%Y')
    print(f'Certificado emitido em {data_emissao}')

    # Imprime uma linha para separar visualmente a seção do certificado
    linha()


def calcularCargaHoraria(participante):
    # Inicializa a variável para armazenar a carga horária total
    cargaHorariaTotal = 0

    # Itera sobre os minicursos selecionados pelo participante
    for evento in participante.get('minicursoSelecionados', []):
        # Adiciona a carga horária do minicurso à carga horária total
        cargaHorariaTotal += evento['cargaHoraria']

    # Itera sobre as palestras selecionadas pelo participante
    for evento in participante.get('palestrasSelecionadas', []):
        # Adiciona a carga horária da palestra à carga horária total
        cargaHorariaTotal += evento['cargaHoraria']

    # Retorna a carga horária total calculada
    return cargaHorariaTotal


def listarParticipantesComEventos():
    # Função linha() deve imprimir uma linha para separar visualmente as seções da lista
    linha()
    # Função tituloCentralizado() deve imprimir um título centralizado para a lista
    tituloCentralizado('LISTA DE PARTICIPANTES COM EVENTOS')
    linha()

    # Itera sobre os participantes no dicionário 'users'
    for participante in users['user']:
        nome = participante['name']
        telefone = participante['telefone']
        instituicao = participante['instituição']

        # Imprime informações do participante
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print(f'Instituição: {instituicao}')

        eventosInscritos = []

        # Verifica se o participante está inscrito em minicursos e palestras
        if 'minicursoSelecionados' in participante:
            eventosInscritos.extend(participante['minicursoSelecionados'])

        if 'palestrasSelecionadas' in participante:
            eventosInscritos.extend(participante['palestrasSelecionadas'])

        # Se o participante estiver inscrito em algum evento
        if eventosInscritos:
            print('Eventos Inscritos:')
            # Função linhaSimples() deve imprimir uma linha simples para separar a lista de eventos
            linhaSimples()
            # Itera sobre os eventos inscritos pelo participante
            for evento in eventosInscritos:
                # Função tituloCentralizado() deve imprimir um título centralizado para cada tipo de evento
                tituloCentralizado(evento['tipo'])
                print(f'Nome: {evento["nome"]}')
                print(f'Data: {evento["data"]}')
                print(f'Horário: {evento["horario"]}')
                print(f'Carga Horária: {evento["cargaHoraria"]} horas')
                print(f'Ministrante: {evento["ministrante"]}')
                # Função linha() deve imprimir uma linha para separar visualmente os eventos
                linha()
        else:
            # Se o participante não estiver inscrito em nenhum evento, exibe uma mensagem
            print('O participante não está inscrito em nenhum evento.')

        # Imprime uma linha para separar visualmente os participantes na lista
        linha()


def limparTerminal():
    # A função os.system() permite executar comandos no sistema operacional.
    # Dependendo do sistema operacional, ele executará 'cls' (Windows) ou 'clear' (Linux/Unix) para limpar a tela do terminal.
    os.system('cls' if os.name == 'nt' else 'clear')


def menuPrincipal():
    while True:
        # Função linha() deve imprimir uma linha para separar visualmente as seções do menu
        linha()
        # Imprime o cabeçalho do menu centralizado
        print(f'{"MENU DE OPÇÕES":^30}')
        # Outra linha para separação
        linha()

        # Exibe as opções do menu numeradas
        print('1 - Cadastro de participantes.')
        print('2 - Cadastro de eventos.')
        print('3 - Listar todos os eventos.')
        print('4 - Se cadastrar em eventos.')
        print('5 - Gerar certificados.')
        print('6 - Listar os participantes.')
        print('7 - Sair.')

        # Solicita a escolha do usuário
        opc = str(input('Informe sua opção: '))

        # Função limparTerminal() deveria realizar alguma ação que não está definida aqui

        # Verifica a escolha do usuário e executa a ação correspondente
        if opc == '1':
            # Chama a função para cadastrar participantes
            cadastrarParticipante()
        elif opc == '2':
            # Chama a função para cadastrar eventos
            cadastrarEvento()
        elif opc == '3':
            # Chama a função para listar todos os eventos
            listarEventos()
        elif opc == '4':
            # Chama a função para o usuário se cadastrar em eventos
            escolherEvento()
        elif opc == '5':
            # Chama a função para gerar certificados
            gerarCertificado()
        elif opc == '6':
            # Chama a função para listar os participantes com eventos
            listarParticipantesComEventos()
        elif opc == '7':
            # Imprime uma mensagem de saída e sai do loop infinito, encerrando o programa
            print('OBRIGADO POR USAR NOSSO SISTEMA! FIM DO PROGRAMA!')
            break
        else:
            # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')


menuPrincipal()
