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
    print('=' * 30)


def linhaSimples():
    print('-' * 30)


def tituloCentralizado(titulo):
    print(f'"{titulo:^30}"')


def validarSenha(password):
    cont = 0

    while password not in [admin['pass'] for admin in users['admins']]:
        linhaSimples()
        print('ERRO! Senha incorreta!')
        cont += 1
        print(f'Mais {3 - cont} tentativas.')
        linhaSimples()
        password = str(input('Informe a senha:')).strip()

        if cont == 3:
            print('Tentativas esgotadas! Programa encerrado!')
            sys.exit()


def cadastrarEvento():
    linha()
    tituloCentralizado('CADASTRO DE EVENTOS')
    linha()

    listarParticipantes()

    nomeAdmin = str(input('Informe o nome do administrador com permissão de cadastro: ')
                    ).strip().capitalize()

    if nomeAdmin in [admin['name'] for admin in users['admins']]:
        senha = str(input('Informe a senha (3 tentativas):'))
        validarSenha(senha)

        linha()
        tituloCentralizado('ACESSO CONCEDIDO')
        linha()

        print('Opções de cadastro:')
        print('M - Minicurso')
        print('P - Palestra')

        tipo = str(input(
            'O que você deseja cadastrar? [M - minicurso | P - Palestra]:')).strip().upper()[0]

        if tipo == 'M':
            tipoEvento = 'Minicurso'
        elif tipo == 'P':
            tipoEvento = 'Palestra'
        else:
            print('Tipo de evento inválido.')
            return

        linha()
        print(f'{f"Cadastro de {tipoEvento}":^30}')
        linha()
        nome = str(input('Nome do evento: '))

        while not nome:
            nome = str(input('Nome vazio. Nome do evento: '))

        local = str(input('Informe o local: '))

        while not local:
            local = str(input('Local vazio. local do evento: '))

        data = str(input('Informe a data (XX/XX/XXXX): '))

        while validarData(data) == False:
            data = str(
                input('Use o formato correto. Informe a data (XX/XX/XXXX): '))
            if validarData(data):
                break

        horario = str(input('Informe o horario (XX:XX): '))

        while validarHorario(horario) == False:
            horario = str(
                input('Use o formato correto. Informe o horario (XX:XX): '))
            if validarHorario(horario):
                break

        while True:
            cargaHoraria = str(input('Carga horária (em horas): ')).strip()
            if cargaHoraria.isdigit() and int(cargaHoraria) > 0:
                cargaHoraria = int(cargaHoraria)
                break
            else:
                print('Valor de carga horária inválido. Informe um valor positivo.')

        ministrante = str(input('Informe o ministrante:'))

        while not ministrante:
            ministrante = str(
                input('Ministrante vazio. Informe o ministrante: '))

        novoEvento = {
            'tipo': tipo,
            'nome': nome,
            'data': data,
            'local': local,
            'horario': horario,
            'cargaHoraria': cargaHoraria,
            'ministrante': ministrante
        }

        if tipo == 'M':
            eventos['minicursos'].append(novoEvento)
        elif tipo == 'P':
            eventos['palestras'].append(novoEvento)
        else:
            print('TIPO INVÁLIDO!')

        print(f'{nome} adicionado com sucesso!')
    else:
        print('PERMISSÃO NEGADA! Nome de administrador não encontrado ou senha incorreta.')


def validarData(data):
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def validarHorario(horario):
    try:
        datetime.datetime.strptime(horario, '%H:%M')
        return True
    except ValueError:
        return False


def listarParticipantes():
    print(f"{'Todos os Usuários:':^30}")
    linha()
    for lista in ['admins', 'user']:
        for usuario in users[lista]:
            nome = usuario['name']
            instituicao = usuario['instituição']
            print(f'Nome: {nome} - Instituição: {instituicao}')


def cadastrarParticipante():

    linha()
    tituloCentralizado('CADASTRO DE USUÁRIO')
    linha()

    name = str(input('Inform seu nome:')).strip().capitalize()

    while not name:
        name = input('Nome inválido. Informe seu nome: ').strip().capitalize()

    telefone = str(input('Informe seu telefone (9 digitos apenas):'))

    while not telefone.isdigit() or len(telefone) != 9:
        telefone = str(input(
            'Número de telefone inválido. Certifique-se de inserir 9 dígitos numéricos:'))

    instituição = str(input('Instituição vinculado:')).strip().capitalize()

    while not instituição:
        instituição = input(
            'Nome inválido. Informe seu nome: ').strip().capitalize()

    novoParticipante = {
        'name': name,
        'telefone': telefone,
        'instituição': instituição,
        'minicursoSelecionados': [],
        'palestrasSelecionados': []
    }

    users['user'].append(novoParticipante)

    linha()
    print(f'Usuário {name} adicionado com sucesso!')
    linha()


def listarEventos():
    linha()
    tituloCentralizado('LISTA DE EVENTOS')
    linha()

    print('Minicursos:')
    for indice, evento in enumerate(eventos['minicursos']):
        print(f'Índice: {indice}')
        print(f'Nome: {evento["nome"]}')
        print(f'Data: {evento["data"]}')
        print(f'Local: {evento["local"]}')
        print(f'Horário: {evento["horario"]}')
        print(f'Carga Horária: {evento["cargaHoraria"]} horas')
        print(f'Ministrante: {evento["ministrante"]}')
        linha()

    print('Palestras:')
    for indice, evento in enumerate(eventos['palestras']):
        print(f'Índice: {indice}')
        print(f'Nome: {evento["nome"]}')
        print(f'Data: {evento["data"]}')
        print(f'Local: {evento["local"]}')
        print(f'Horário: {evento["horario"]}')
        print(f'Carga Horária: {evento["cargaHoraria"]} horas')
        print(f'Ministrante: {evento["ministrante"]}')
        linha()


def escolherEvento():
    linha()
    tituloCentralizado('SELECIONAR PARTICIPANTE')
    linha()

    listarParticipantes()
    nomeParticipante = str(
        input('Informe o nome do participante: ')).strip().capitalize()

    participante = None
    for user in users['user']:
        if user['name'] == nomeParticipante:
            participante = user
            break

    if participante is None:
        print('Participante não encontrado!')
        return

    linha()
    tituloCentralizado('SELECIONAR EVENTOS')
    linha()

    listarEventos()

    selecaoMinicursos = participante.get('minicursoSelecionados', [])
    selecaoPalestras = participante.get('palestrasSelecionadas', [])

    maxMinicursos = 3
    maxPalestras = 4

    while True:
        if len(selecaoMinicursos) >= maxMinicursos and len(selecaoPalestras) >= maxPalestras:
            print('Você atingiu o limite máximo de minicursos e palestras.')
            break

        tipoEvento = input(
            'Digite o tipo do evento (M - Minicurso ou P - Palestra): ').strip().upper()

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

        if len(selecao) >= maxSelecao:
            print(
                f'Você já selecionou o máximo de {maxSelecao} eventos desse tipo.')
            continuar = input(
                'Deseja selecionar outro evento? (S/N): ').strip().upper()
            if continuar != 'S':
                break

        try:
            indiceEvento = int(
                input('Digite o índice do evento que deseja selecionar: '))
            if 0 <= indiceEvento < len(eventosDisponiveis):
                eventoSelecionado = eventosDisponiveis[indiceEvento]

                if eventoSelecionado in selecao:
                    print(
                        f'Você já selecionou o evento "{eventoSelecionado["nome"]}".')
                else:
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


def gerarCertificados():
    linha()
    tituloCentralizado('GERAR CERTIFICADOS')
    linha()

    participante = str(
        input('Informe o nome do participante: ')).strip().capitalize()

    participanteEncontrado = None
    for user in users['user']:
        if user['name'] == participante:
            participanteEncontrado = user
            break

    if participanteEncontrado is not None:
        linha()
        tituloCentralizado(
            f'EVENTOS INSCRITOS POR PARTICIPANTE: {participante}')
        linha()

        if 'minicursoSelecionados' in participanteEncontrado:
            if participanteEncontrado['minicursoSelecionados']:
                print('Minicursos inscritos:')
                linhaSimples()
                for evento in participanteEncontrado['minicursoSelecionados']:
                    tituloCentralizado('Minicurso')
                    print(f'Nome: {evento["nome"]}')
                    print(f'Data: {evento["data"]}')
                    print(f'Horário: {evento["horario"]}')
                    print(f'Carga Horária: {evento["cargaHoraria"]} horas')
                    print(f'Ministrante: {evento["ministrante"]}')
                    linha()
        else:
            print('O participante não se inscreveu em nenhum minucurso.')

        if 'palestrasSelecionadas' in participanteEncontrado:
            if participanteEncontrado['palestrasSelecionadas']:
                print('Palestras inscritas:')
                linhaSimples()
                for evento in participanteEncontrado['palestrasSelecionadas']:
                    tituloCentralizado('Palestra')
                    print(f'Nome: {evento["nome"]}')
                    print(f'Data: {evento["data"]}')
                    print(f'Horário: {evento["horario"]}')
                    print(f'Carga Horária: {evento["cargaHoraria"]} horas')
                    print(f'Ministrante: {evento["ministrante"]}')
                    linha()
        else:
            print('O participante não se inscreveu em nenhuma palestra.')

        cargaTotal = calcularCargaHoraria(participanteEncontrado)
        print(f'Carga Horária Total: {cargaTotal} horas')

    else:
        print(f'Participante "{participante}" não encontrado.')


def calcularCargaHoraria(participante):
    cargaHorariaTotal = 0

    for evento in participante.get('minicursoSelecionados', []):
        cargaHorariaTotal += evento['cargaHoraria']

    for evento in participante.get('palestrasSelecionadas', []):
        cargaHorariaTotal += evento['cargaHoraria']

    return cargaHorariaTotal


def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menuPrincipal():
    while True:

        linha()
        print(f'{"MENU DE OPÇÕES":^30}')
        linha()

        print('1 - Cadastro de participantes.')
        print('2 - Cadastro de eventos.')
        print('3 - Listar todos os eventos.')
        print('4 - Se cadastrar em eventos.')
        print('5 - Gerar certificados.')
        print('6 - Sair.')
        opc = str(input('Informe sua opção: '))
        limparTerminal()

        if opc == '1':
            cadastrarParticipante()
        elif opc == '2':
            cadastrarEvento()
        elif opc == '3':
            listarEventos()
        elif opc == '4':
            escolherEvento()
        elif opc == '5':
            gerarCertificados()
        elif opc == '6':
            print('OBRIGADO POR USAR NOSSO SISTEMA! FIM DO PROGRAMA!')
            break
        else:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')


menuPrincipal()
