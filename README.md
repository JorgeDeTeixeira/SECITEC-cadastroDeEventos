Vamos supor que você foi contratado para criar um sistema de gerenciamento de eventos como o SECITEC.

Neste sistema, existem algumas especificações que o cliente gostaria que você atendesse:

1º O Cliente na condição de usuário admin pode cadastrar minicursos e palestras. Cada minicurso e palestra possui data, local, horário, carga horária e um ministrante.

2º O participante na condição de usuário participante iria primeiro fornecer seus dados: nome, telefone e instituição que está vinculado. Depois disso, o usuário participante poderia selecionar até 3 minicursos e 4 palestras no máximo. Durante a seleção dos minicursos e palestras deve ser observado o choque de horários.

3º Ao final do evento, o sistema deverá emitir ao usuário um certificado com a listagem de todos os minicursos e palestras que ele se inscreveu e a carga horária total sendo a soma das cargas horárias de todos os minicursos e palestras que ele participou.

Você sabiamente pensou e resolveu esse sistema usando estruturas condicionais, estruturas de repetição, listas, tuplas e dicionários.

#Bibliotecas importadas
datetime: O módulo datetime fornece classes para manipulação de datas e horários. Ele permite que você trabalhe com datas, horários, intervalos de tempo e realize operações de formatação e cálculos de data e hora.

os: O módulo os fornece funções para interagir com o sistema operacional subjacente. Você pode usá-lo para acessar o sistema de arquivos, listar diretórios, criar e excluir arquivos, manipular caminhos de arquivo, entre outras operações relacionadas ao sistema.

sys: O módulo sys fornece acesso a variáveis e funções específicas do sistema. Ele é usado para interagir com o interpretador Python e o ambiente de execução, permitindo a manipulação de argumentos de linha de comando, saída padrão e outros recursos do sistema.

def linha():
"""
Imprime uma linha de caracteres '=' para fins de formatação.

    Esta função imprime uma linha de caracteres '=' para criar uma linha separadora ou de formatação em um texto.

    Exemplo de uso:
    linha()
    # Saída:
    # ==============================
    """
    print('=' * 30)

def linhaSimples():
"""
Imprime uma linha de caracteres '-' para fins de formatação simples.

    Esta função imprime uma linha de caracteres '-' para criar uma linha separadora ou de formatação simples em um texto.

    Exemplo de uso:
    linhaSimples()
    # Saída:
    # ------------------------------
    """
    print('-' * 30)

def tituloCentralizado(titulo):
"""
Imprime um título centralizado em um espaço de 30 caracteres.

    Esta função recebe um título como argumento e o imprime centralizado em um espaço de 30 caracteres,
    com aspas duplas ao redor do título para destaque.

    Args:
        titulo (str): O título a ser centralizado e impresso.

    Exemplo de uso:
    tituloCentralizado("Título do Evento")
    # Saída:
    # "   Título do Evento   "
    """
    print(f'"{titulo:^30}"')

def validarSenha(password):
"""
Valida a senha fornecida em relação às senhas de administradores.

    Esta função recebe uma senha como entrada e verifica se ela corresponde a uma das senhas armazenadas
    na lista de senhas dos administradores.

    Args:
        password (str): A senha a ser validada.

    Retorna:
        None

    Comportamento:
        - A função entra em um loop enquanto a senha não corresponde a nenhuma das senhas dos administradores.
        - Se a senha estiver incorreta após 3 tentativas, o programa é encerrado.

    Exemplo de uso:
    validarSenha("senha_admin")
    # Comportamento dependente das senhas armazenadas na lista de administradores.
    """
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
"""
Permite a um administrador cadastrar um evento (minicurso ou palestra).

    Esta função interage com o usuário administrador para cadastrar um evento, incluindo nome, local, data, horário,
    carga horária e ministrante do evento. O administrador deve fornecer sua senha para acessar a função e pode
    escolher entre cadastrar um minicurso (M) ou uma palestra (P).

    Retorna:
        None

    Comportamento:
        - Solicita o nome do administrador com permissão de cadastro.
        - Valida a senha do administrador.
        - Permite ao administrador escolher entre cadastrar um minicurso ou palestra.
        - Solicita informações do evento (nome, local, data, horário, carga horária e ministrante).
        - Adiciona o evento à lista de eventos (minicursos ou palestras) apropriada.

    Exemplo de uso:
    cadastrarEvento()
    # Comportamento dependente da interação do usuário.
    """
    linha()
    tituloCentralizado('CADASTRO DE EVENTOS')
    linha()

    listarParticipantes()

    nomeAdmin = str(input('Informe o nome do administrador com permissão de cadastro: ')
                    ).strip().capitalize()

    # Valida se o nome do administrador está na lista de administradores
    if nomeAdmin in [admin['name'] for admin in users['admins']]:
        senha = str(input('Informe a senha (3 tentativas):'))
        validarSenha(senha)  # Chama a função para validar a senha do administrador

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

        # Valida a formatação correta da data
        while validarData(data) == False:
            data = str(
                input('Use o formato correto. Informe a data (XX/XX/XXXX): '))
            if validarData(data):
                break

        horario = str(input('Informe o horario (XX:XX): '))

        # Valida a formatação correta do horário
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

        # Adiciona o evento à lista apropriada (minicursos ou palestras)
        if tipo == 'M':
            eventos['minicursos'].append(novoEvento)
        elif tipo == 'P':
            eventos['palestras'].append(novoEvento)
        else:
            print('TIPO INVÁLIDO!')

        print(f'{nome} adicionado com sucesso!')
    else:
        print('PERMISSÃO NEGADA!')

def validarData(data):
"""
Valida o formato de data (XX/XX/XXXX).

    Args:
        data (str): A data a ser validada.

    Returns:
        bool: True se a data estiver no formato correto, False caso contrário.
    """
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validarHorario(horario):
"""
Valida o formato de horário (XX:XX).

    Args:
        horario (str): O horário a ser validado.

    Returns:
        bool: True se o horário estiver no formato correto, False caso contrário.
    """
    try:
        datetime.datetime.strptime(horario, '%H:%M')
        return True
    except ValueError:
        return False

def listarParticipantes():
"""
Lista todos os usuários (administradores e usuários comuns) com seus nomes e instituições.

    Comportamento:
        - Imprime os nomes e instituições de todos os administradores e usuários comuns registrados.

    Retorna:
        None
    """
    # Título centralizado para indicar a seção de listagem de participantes
    print(f"{'Todos os Usuários:':^30}")

    # Linha horizontal para separar a lista dos participantes
    linha()

    # Itera sobre as listas de administradores e usuários
    for lista in ['admins', 'user']:
        for usuario in users[lista]:
            nome = usuario['name']  # Obtém o nome do usuário
            instituicao = usuario['instituição']  # Obtém a instituição do usuário (corrigido para 'instituição')

            # Imprime o nome e a instituição do usuário
            print(f'Nome: {nome} - Instituição: {instituicao}')

def menuPrincipal():
"""
Exibe um menu de opções para o usuário e direciona para as funcionalidades correspondentes.

    Comportamento:
        - Apresenta um menu com opções numeradas.
        - Solicita ao usuário que escolha uma opção.
        - Direciona para a funcionalidade correspondente com base na escolha do usuário.
        - Permite ao usuário sair do programa.

    Retorna:
        None
    """
    while True:
        linha()
        print(f'{"MENU DE OPÇÕES":^30}')
        linha()

        # Exibe as opções disponíveis no menu
        print('1 - Cadastro de participantes.')
        print('2 - Cadastro de eventos.')
        print('3 - Listar todos os eventos.')
        print('4 - Se cadastrar em eventos.')
        print('5 - Gerar certificados.')
        print('6 - Sair.')

        opc = str(input('Informe sua opção: '))  # Solicita a escolha do usuário
        limparTerminal()  # Limpa o terminal para melhorar a interface

        # Verifica a escolha do usuário e direciona para a funcionalidade correspondente
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
            break  # Encerra o programa
        else:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')

import os

def limparTerminal():
"""
Limpa a tela do terminal.

    Comportamento:
        - Detecta o sistema operacional em uso (Windows ou não-Windows).
        - Executa o comando apropriado para limpar a tela com base no sistema.

    Retorna:
        None
    """
    # Verifica se o sistema operacional é Windows (os.name == 'nt')
    if os.name == 'nt':
        # No Windows, utiliza 'cls' para limpar o terminal
        os.system('cls')
    else:
        # Em sistemas não-Windows, utiliza 'clear' para limpar o terminal
        os.system('clear')

def cadastrarParticipante():
"""
Permite o cadastro de um novo participante no sistema.

    Comportamento:
        - Solicita ao usuário as informações necessárias para o cadastro (nome, telefone e instituição).
        - Realiza validações para garantir que as informações inseridas sejam válidas.
        - Cria um novo participante com as informações fornecidas e o adiciona à lista de usuários comuns.
        - Imprime uma mensagem de confirmação após o cadastro.

    Retorna:
        None
    """
    # Exibe uma linha horizontal para separar visualmente o cadastro de participante
    linha()
    # Título centralizado indicando a seção de cadastro de usuário
    tituloCentralizado('CADASTRO DE USUÁRIO')
    # Exibe outra linha horizontal
    linha()

    # Solicita o nome do participante e valida
    name = str(input('Informe seu nome:')).strip().capitalize()
    while not name:
        name = input('Nome inválido. Informe seu nome: ').strip().capitalize()

    # Solicita o telefone do participante e valida
    telefone = str(input('Informe seu telefone (9 dígitos apenas):'))
    while not telefone.isdigit() or len(telefone) != 9:
        telefone = str(input(
            'Número de telefone inválido. Certifique-se de inserir 9 dígitos numéricos:'))

    # Solicita a instituição do participante e valida
    instituição = str(input('Instituição vinculada:')).strip().capitalize()
    while not instituição:
        instituição = input(
            'Nome inválido. Informe sua instituição: ').strip().capitalize()

    # Cria um dicionário representando o novo participante
    novoParticipante = {
        'name': name,
        'telefone': telefone,
        'instituição': instituição,
        'minicursoSelecionados': [],
        'palestrasSelecionados': []
    }

    # Adiciona o novo participante à lista de usuários comuns ('user')
    users['user'].append(novoParticipante)

    # Exibe uma linha horizontal para indicar o sucesso do cadastro
    linha()
    # Imprime uma mensagem de confirmação com o nome do participante cadastrado
    print(f'Usuário {name} adicionado com sucesso!')
    # Exibe outra linha horizontal para separar visualmente
    linha()

def listarEventos():
"""
Lista todos os eventos (minicursos e palestras) registrados no sistema.

    Comportamento:
        - Exibe a lista de minicursos, incluindo informações como nome, data, local, horário, carga horária e ministrante.
        - Exibe a lista de palestras, incluindo informações semelhantes.
        - Cada evento é identificado por um índice.

    Retorna:
        None
    """
    # Exibe uma linha horizontal para separar visualmente a lista de eventos
    linha()
    # Título centralizado indicando a seção de lista de eventos
    tituloCentralizado('LISTA DE EVENTOS')
    # Exibe outra linha horizontal
    linha()

    # Lista os minicursos
    print('Minicursos:')
    for indice, evento in enumerate(eventos['minicursos']):
        print(f'Índice: {indice}')
        print(f'Nome: {evento["nome"]}')
        print(f'Data: {evento["data"]}')
        print(f'Local: {evento["local"]}')
        print(f'Horário: {evento["horario"]}')
        print(f'Carga Horária: {evento["cargaHoraria"]} horas')
        print(f'Ministrante: {evento["ministrante"]}')
        # Exibe uma linha horizontal para separar cada evento
        linha()

    # Lista as palestras
    print('Palestras:')
    for indice, evento in enumerate(eventos['palestras']):
        print(f'Índice: {indice}')
        print(f'Nome: {evento["nome"]}')
        print(f'Data: {evento["data"]}')
        print(f'Local: {evento["local"]}')
        print(f'Horário: {evento["horario"]}')
        print(f'Carga Horária: {evento["cargaHoraria"]} horas')
        print(f'Ministrante: {evento["ministrante"]}')
        # Exibe uma linha horizontal para separar cada evento
        linha()

def escolherEvento():
"""
Permite aos participantes selecionar eventos (minicursos e palestras) para participar.

    Comportamento:
        - Solicita ao usuário o nome do participante.
        - Localiza o participante na lista de usuários comuns.
        - Exibe a lista de eventos (minicursos e palestras) disponíveis.
        - Permite que o participante selecione eventos de acordo com as regras (limite de minicursos e palestras).
        - Adiciona os eventos selecionados à lista do participante.
        - Possibilita a seleção de múltiplos eventos até atingir os limites máximos ou até o participante optar por encerrar.

    Retorna:
        None
    """
    # Exibe uma linha horizontal para separar visualmente a seção de seleção de eventos
    linha()
    # Título centralizado indicando a seção de seleção de participante
    tituloCentralizado('SELECIONAR PARTICIPANTE')
    # Exibe outra linha horizontal
    linha()

    # Lista todos os participantes disponíveis
    listarParticipantes()

    # Solicita o nome do participante a ser selecionado
    nomeParticipante = str(
        input('Informe o nome do participante: ')).strip().capitalize()

    participante = None

    # Localiza o participante na lista de usuários comuns
    for user in users['user']:
        if user['name'] == nomeParticipante:
            participante = user
            break

    if participante is None:
        print('Participante não encontrado!')
        return

    # Exibe uma linha horizontal para separar visualmente a seção de seleção de eventos
    linha()
    # Título centralizado indicando a seção de seleção de eventos
    tituloCentralizado('SELECIONAR EVENTOS')
    # Exibe outra linha horizontal
    linha()

    # Lista todos os eventos disponíveis (minicursos e palestras)
    listarEventos()

    # Obtém a seleção atual de minicursos e palestras do participante
    selecaoMinicursos = participante.get('minicursoSelecionados', [])
    selecaoPalestras = participante.get('palestrasSelecionadas', [])

    maxMinicursos = 3  # Limite máximo de minicursos
    maxPalestras = 4   # Limite máximo de palestras

    while True:
        # Verifica se o participante atingiu o limite máximo de minicursos e palestras
        if len(selecaoMinicursos) >= maxMinicursos and len(selecaoPalestras) >= maxPalestras:
            print('Você atingiu o limite máximo de minicursos e palestras.')
            break

        # Solicita o tipo de evento (Minicurso ou Palestra)
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
            # Solicita o índice do evento a ser selecionado
            indiceEvento = int(
                input('Digite o índice do evento que deseja selecionar: '))
            if 0 <= indiceEvento < len(eventosDisponiveis):
                eventoSelecionado = eventosDisponiveis[indiceEvento]

                if eventoSelecionado in selecao:
                    print(
                        f'Você já selecionou o evento "{eventoSelecionado["nome"]}".')
                else:
                    selecao.append(eventoSelecionado)
                    # Adiciona o evento selecionado à lista do participante
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
"""
Gera certificados para os participantes com base nos eventos que selecionaram.

    Comportamento:
        - Solicita o nome do participante para o qual deseja gerar o certificado.
        - Verifica se o participante existe na lista de usuários comuns.
        - Lista os eventos (minicursos e palestras) inscritos pelo participante.
        - Calcula a carga horária total dos eventos inscritos.
        - Exibe as informações dos eventos e a carga horária total.
        - Caso o participante não seja encontrado, exibe uma mensagem de erro.

    Retorna:
        None
    """
    # Exibe uma linha horizontal para separar visualmente a seção de geração de certificados
    linha()
    # Título centralizado indicando a seção de geração de certificados
    tituloCentralizado('GERAR CERTIFICADOS')
    # Exibe outra linha horizontal
    linha()

    # Solicita o nome do participante para o qual deseja gerar o certificado
    participante = str(
        input('Informe o nome do participante: ')).strip().capitalize()

    participanteEncontrado = None

    # Verifica se o participante existe na lista de usuários comuns
    for user in users['user']:
        if user['name'] == participante:
            participanteEncontrado = user
            break

    if participanteEncontrado is not None:
        # Exibe uma linha horizontal para separar visualmente a seção de eventos inscritos
        linha()
        # Título centralizado indicando a seção de eventos inscritos pelo participante
        tituloCentralizado(
            f'EVENTOS INSCRITOS POR PARTICIPANTE: {participante}')
        # Exibe outra linha horizontal
        linha()

        # Lista os minicursos inscritos pelo participante
        if participanteEncontrado['minicursoSelecionados']:
            print('Minicursos inscritos:')
            # Exibe uma linha horizontal simples para separar os eventos
            linhaSimples()
            for evento in participanteEncontrado['minicursoSelecionados']:
                # Título centralizado indicando que é um Minicurso
                tituloCentralizado('Minicurso')
                print(f'Nome: {evento["nome"]}')
                print(f'Data: {evento["data"]}')
                print(f'Horário: {evento["horario"]}')
                print(f'Carga Horária: {evento["cargaHoraria"]} horas')
                print(f'Ministrante: {evento["ministrante"]}')
                # Exibe uma linha horizontal simples para separar os eventos
                linha()

        # Lista as palestras inscritas pelo participante
        if participanteEncontrado['palestrasSelecionadas']:
            print('Palestras inscritas:')
            # Exibe uma linha horizontal simples para separar os eventos
            linhaSimples()
            for evento in participanteEncontrado['palestrasSelecionadas']:
                # Título centralizado indicando que é uma Palestra
                tituloCentralizado('Palestra')
                print(f'Nome: {evento["nome"]}')
                print(f'Data: {evento["data"]}')
                print(f'Horário: {evento["horario"]}')
                print(f'Carga Horária: {evento["cargaHoraria"]} horas')
                print(f'Ministrante: {evento["ministrante"]}')
                # Exibe uma linha horizontal simples para separar os eventos
                linha()

        # Calcula a carga horária total dos eventos inscritos
        cargaTotal = calcularCargaHoraria(participanteEncontrado)
        print(f'Carga Horária Total: {cargaTotal} horas')

    else:
        # Caso o participante não seja encontrado, exibe uma mensagem de erro
        print(f'Participante "{participante}" não encontrado.')
