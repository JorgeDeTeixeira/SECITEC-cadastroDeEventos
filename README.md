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
