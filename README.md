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
