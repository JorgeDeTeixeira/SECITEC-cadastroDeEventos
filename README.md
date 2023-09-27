Vamos supor que você foi contratado para criar um sistema de gerenciamento de eventos como o SECITEC.

Neste sistema, existem algumas especificações que o cliente gostaria que você atendesse:

1º O Cliente na condição de usuário admin pode cadastrar minicursos e palestras. Cada minicurso e palestra possui data, local, horário, carga horária e um ministrante.

2º O participante na condição de usuário participante iria primeiro fornecer seus dados: nome, telefone e instituição que está vinculado. Depois disso, o usuário participante poderia selecionar até 3 minicursos e 4 palestras no máximo. Durante a seleção dos minicursos e palestras deve ser observado o choque de horários. 

3º Ao final do evento, o sistema deverá emitir ao usuário um certificado com a listagem de todos os minicursos e palestras que ele se inscreveu e a carga horária total sendo a soma das cargas horárias de todos os minicursos e palestras que ele participou. 

Você sabiamente pensou e resolveu esse sistema usando estruturas condicionais, estruturas de repetição, listas, tuplas e dicionários.

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
