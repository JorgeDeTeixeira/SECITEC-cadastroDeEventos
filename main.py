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
        print(f'Mais {4 - cont} tentativas.')
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

