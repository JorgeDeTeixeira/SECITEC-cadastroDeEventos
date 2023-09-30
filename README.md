def validatePassword(password):
"""
Valida a senha de um administrador comparando-a com as senhas registradas.

    Parâmetros:
    - password (str): A senha a ser validada.

    Retorno:
    - bool: Retorna True se a senha estiver correta, caso contrário, False.

    Comportamento:
    1. A função recebe uma senha como entrada e verifica se essa senha está presente na lista de senhas dos administradores.

    2. Se a senha fornecida corresponder a uma das senhas dos administradores, a função retorna True, indicando que a senha está correta.

    3. Se a senha fornecida não corresponder a nenhuma das senhas dos administradores, a função retorna False, indicando que a senha é incorreta.

    Uso:
    Esta função é utilizada para validar a senha de um administrador durante operações que exigem permissões especiais.

    Exemplo:
    users = {
        'administrators': [{'name': 'Admin1', 'password': '123456'}, {'name': 'Admin2', 'password': 'abcdef'}]
    }
    validatePassword('123456')  # Retorna True
    validatePassword('qwerty')  # Retorna False

    Observações:
    - As senhas dos administradores são armazenadas em uma lista de dicionários no formato {'name': 'Nome', 'password': 'Senha'}.
    - Esta função é útil para garantir que apenas administradores com senhas válidas possam realizar determinadas ações no sistema.
    """

def validateDate(date):
"""
Valida se uma string de data está no formato correto (DD/MM/AAAA).

    Parâmetros:
    - date (str): A string contendo a data a ser validada.

    Retorno:
    - bool: Retorna True se a data estiver no formato correto, caso contrário, retorna False.

    Comportamento:
    1. Tenta criar um objeto datetime a partir da string de data usando o formato "%d/%m/%Y".

    2. Se a conversão for bem-sucedida, a data é considerada válida e a função retorna True.

    3. Se ocorrer uma exceção ValueError durante a conversão, a data é considerada inválida e a função retorna False.

    Uso:
    Esta função pode ser usada para validar se uma string de data está no formato correto (DD/MM/AAAA).

    Exemplo:
    validateDate("20/09/2023")  # Retorna True
    validateDate("30/02/2023")  # Retorna False

    Observações:
    - O formato aceito é DD/MM/AAAA (dia, mês e ano).
    - Esta função é útil para garantir que as datas informadas pelo usuário estejam em um formato válido antes de serem utilizadas em outras partes do sistema.
    """

def validateHours(hours):
"""
Valida se uma string de horário está no formato correto (HH:MM).

    Parâmetros:
    - hours (str): A string contendo o horário a ser validado.

    Retorno:
    - bool: Retorna True se o horário estiver no formato correto, caso contrário, retorna False.

    Comportamento:
    1. Tenta criar um objeto datetime a partir da string de horário usando o formato "%H:%M".

    2. Se a conversão for bem-sucedida, o horário é considerado válido e a função retorna True.

    3. Se ocorrer uma exceção ValueError durante a conversão, o horário é considerado inválido e a função retorna False.

    Uso:
    Esta função pode ser usada para validar se uma string de horário está no formato correto (HH:MM).

    Exemplo:
    validateHours("09:30")  # Retorna True
    validateHours("25:00")  # Retorna False

    Observações:
    - O formato aceito é de 24 horas (HH:MM).
    - Esta função é útil para garantir que os horários informados pelo usuário estejam em um formato válido antes de serem utilizados em outras partes do sistema.
    """

def back():
"""
Esta função permite ao usuário voltar ao menu principal do sistema pressionando a tecla 'Q'.

    Parâmetros:
    Nenhum

    Comportamento:
    1. Imprime a mensagem "Pressione 'Q' para sair" para informar ao usuário como sair do menu atual.

    2. Desenha uma linha horizontal simples para fins de formatação.

    3. Inicia um loop que aguarda até que o usuário pressione a tecla 'Q' para sair.

    4. Quando 'Q' é pressionado, exibe uma mensagem indicando que o usuário está voltando para o menu principal.

    Uso:
    A função 'back' é usada para permitir que o usuário saia de um menu ou tela secundária e retorne ao menu principal.

    Exemplo:
    back()

    Observações:
    - A função utiliza um loop para aguardar a tecla 'Q' e, portanto, é adequada para situações em que o usuário precisa
      interagir com a interface do sistema antes de retornar ao menu principal.
    """

def registerParticipant():
"""
Esta função permite o cadastro de novos participantes no sistema, coletando informações como nome, telefone, e instituição
vinculada. Também realiza validações para garantir que os dados fornecidos sejam adequados.

    Parâmetros:
    Nenhum

    Comportamento:
    1. Desenha uma linha horizontal para fins de formatação e legibilidade.

    2. Imprime um título centralizado "CADASTRO DE PARTICIPANTE" para identificar a seção de cadastro de participantes.

    3. Solicita ao usuário as seguintes informações:
       - Nome do participante.
       - Telefone celular (9 dígitos).
       - Instituição vinculada ao participante.

    4. Realiza validações para garantir que os dados fornecidos sejam adequados:
       - O nome não pode estar em branco.
       - O telefone celular deve ter exatamente 9 dígitos numéricos.
       - O nome da instituição não pode estar em branco.

    5. Cria um dicionário com as informações do novo participante, incluindo nome, telefone, instituição, e listas vazias de
       minicursos e palestras selecionadas.

    6. Adiciona o novo participante à lista de participantes no dicionário 'users'.

    7. Imprime uma mensagem de sucesso informando que o participante foi adicionado com sucesso ao sistema.

    8. Inicia um loop que aguarda até que o usuário pressione a tecla 'Q' para sair.

    9. Quando 'Q' é pressionado, exibe uma mensagem indicando que o usuário está voltando para o menu principal.

    10. A função aguarda por 2 segundos antes de encerrar a execução.

    Uso:
    A função 'registerParticipant' é usada para coletar informações de um novo participante, validar essas informações e
    adicioná-lo ao sistema.

    Exemplo:
    registerParticipant()

    Observações:
    - A função realiza validações para garantir a integridade dos dados fornecidos pelo usuário.
    - O participante é adicionado à lista de participantes no dicionário 'users' para futura referência.
    - A função utiliza um loop para aguardar a tecla 'Q' para sair, proporcionando tempo ao usuário para ler a mensagem de sucesso.
    """

def registerEvent():
"""
Permite o cadastro de eventos (Minicursos ou Palestras) no sistema.

    Esta função inicia o processo de cadastro de eventos, solicitando as credenciais do administrador
    com permissão para realizar o cadastro. Ela realiza os seguintes passos:

    Passos:
    1. Solicita o nome do administrador com permissão de cadastro.
       - O administrador deve fornecer seu nome para acessar a função de cadastro de eventos.

    2. Verifica se o nome do administrador está na lista de administradores do sistema.
       - Verifica se o nome fornecido corresponde a um administrador registrado no sistema.

    3. Solicita a senha do administrador com um limite de até 3 tentativas.
       - O administrador deve inserir a senha correta para confirmar sua identidade.
       - São permitidas até 3 tentativas de senha incorreta.

    4. Se as credenciais estiverem corretas, exibe as opções de cadastro (Minicurso ou Palestra) e solicita o tipo de evento.
       - O administrador pode escolher entre cadastrar um Minicurso (M) ou uma Palestra (P).

    5. Solicita informações detalhadas do evento, incluindo nome, local, data, horário, carga horária e ministrante.
       - O administrador fornece informações específicas sobre o evento a ser cadastrado.

    6. Valida as informações inseridas, incluindo a validação de formato de data, horário e carga horária.
       - As informações fornecidas pelo administrador são verificadas para garantir que sejam válidas.

    7. Cria um dicionário com as informações do novo evento.
       - As informações validadas são organizadas em um dicionário que representa o evento.

    8. Adiciona o novo evento à lista de eventos correspondente (Minicursos ou Palestras) no sistema.
       - O evento é adicionado à lista apropriada no sistema.

    9. Imprime uma mensagem de sucesso informando que o evento foi adicionado ao sistema.
       - Confirma que o evento foi cadastrado com êxito.

    Note:
        Para cadastrar um evento, o administrador deve ter permissões e fornecer credenciais corretas.
        A validação de dados garante que informações válidas sejam inseridas no sistema.

    Returns:
        None

    Raises:
        Exception: Se ocorrer um erro durante o cadastro do evento, uma exceção será lançada com informações detalhadas do erro.

    Examples:
        Exemplo de uso da função:
        registerEvent()

    """

def listEvents():
"""
Esta função lista os eventos registrados no sistema, incluindo workshops e palestras, fornecendo informações detalhadas
sobre cada evento.

    Parâmetros:
    Nenhum

    Comportamento:
    1. Desenha uma linha horizontal e imprime um título centralizado "LISTA DE EVENTOS" para identificar a seção de listagem de eventos.

    2. Em seguida, lista os workshops registrados no sistema, imprimindo as seguintes informações para cada workshop:
       - Índice do evento na lista.
       - Nome do workshop.
       - Data do workshop.
       - Horário do workshop.
       - Local do workshop.
       - Carga horária do workshop em horas.
       - Nome do apresentador do workshop.

    3. A função continua listando as palestras registradas no sistema, imprimindo as seguintes informações para cada palestra:
       - Índice da palestra na lista.
       - Nome da palestra.
       - Data da palestra.
       - Horário da palestra.
       - Local da palestra.
       - Carga horária da palestra.
       - Nome do palestrante.

    4. Após listar todos os eventos, a função chama a função 'back' para permitir que o usuário retorne ao menu principal.

    5. A função aguarda 3 segundos antes de encerrar a execução.

    Uso:
    A função 'listEvents' é usada para exibir uma lista organizada de todos os eventos registrados no sistema, incluindo
    informações detalhadas sobre cada evento.

    Exemplo:
    listEvents()

    Observações:
    - A função assume que os eventos já foram registrados no sistema, pois ela apenas lista os eventos existentes.
    - Os eventos são separados em duas categorias: workshops e palestras, e suas informações são formatadas de maneira clara
      e legível.
    """

def listParticipants():
"""
Lista os participantes cadastrados no sistema.

    Esta função exibe uma lista de todos os participantes cadastrados no sistema, incluindo o índice, nome e uma linha divisória para cada participante.

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.

    Exemplo:
    listParticipants()

    Saída:
    ----------------------------------------
    LISTA DE PARTICIPANTES
    ----------------------------------------
    Índice: 0 - Nome: João
    ----------------------------------------
    Índice: 1 - Nome: Maria
    ----------------------------------------

    Observações:
    - Esta função exibe uma lista de participantes cadastrados no sistema.
    - Cada participante é exibido com um índice numérico, seu nome e uma linha divisória para facilitar a leitura.
    - Se não houver participantes cadastrados, a função não exibirá nada.
    """

def choiceEvent(participant):
"""
Permite que um participante escolha workshops e palestras para participar.

    Parâmetros:
    participant (dict): Um dicionário que representa o participante.

    Comportamento:
    1. Exibe um título centralizado "SELECIONAR EVENTOS" para identificar a seção de seleção de eventos.
    2. Define limites máximos de workshops e palestras que o participante pode selecionar (maxWorkshops e maxLectures).
    3. Obtém as seleções anteriores de workshops e palestras do dicionário 'participant'.
    4. Inicia um loop onde o participante pode selecionar workshops e palestras até atingir os limites máximos.
    5. Solicita ao participante que escolha entre minicursos (M) ou palestras (P).
    6. Lista os eventos disponíveis do tipo escolhido com informações detalhadas.
    7. Solicita que o participante insira o número do evento que deseja selecionar.
    8. Registra a seleção no dicionário 'participant' e fornece mensagens informativas.
    9. Lida com erros como entrada inválida, índice fora dos limites e eventos já selecionados.
    10. Pergunta se o participante deseja selecionar mais eventos e encerra o loop se necessário.

    Uso:
    A função 'choiceEvent' é chamada para permitir que um participante selecione workshops e palestras para participar.

    Exemplo:
    choiceEvent(participant)

    Observações:
    - Certifique-se de que o participante foi previamente registrado no sistema e tenha um dicionário associado a ele.
    - Os limites máximos de workshops e palestras podem ser ajustados conforme necessário.
    - A função exibe mensagens informativas e trata erros para tornar a seleção de eventos mais intuitiva e robusta.
    """

def chooseEvent():
"""
Função que permite que um participante selecione workshops e palestras para participar.

    Esta função exibe a lista de participantes cadastrados, solicita o nome do participante desejado,
    procura o participante na lista de participantes e, se encontrado, permite que o participante selecione
    eventos usando a função 'choiceEvent'. Após a seleção dos eventos, a função retorna ao menu principal.

    Parâmetros:
        Nenhum.

    Comportamento:
    1. Exibe a lista de participantes cadastrados usando a função 'listParticipants'.

    2. Solicita ao usuário o nome do participante desejado e formata o nome para capitalizar a primeira letra
       e remover espaços em excesso.

    3. Inicializa a variável 'participant' como 'None' para armazenar as informações do participante após a busca.

    4. Entra em um loop que percorre a lista de participantes procurando pelo participante com o nome inserido.

    5. Se o participante for encontrado, a variável 'participant' é atualizada com as informações desse participante.

    6. Se o participante não for encontrado, exibe uma mensagem informando que o participante não foi encontrado
       e encerra a função.

    7. Após encontrar o participante, a função chama 'choiceEvent(participant)' para permitir que o participante selecione eventos.

    8. Após a seleção dos eventos, a função chama 'back()' para voltar à função anterior (menu principal).

    9. Aguarda por 3 segundos antes de encerrar a execução.

    Uso:
    A função 'chooseEvent' é chamada quando um participante deseja selecionar workshops e palestras para participar.

    Exemplo:
    chooseEvent()

    Observações:
    - Esta função atua como um intermediário para permitir que um participante específico selecione seus eventos
      usando a função 'choiceEvent'. Ela fornece uma maneira conveniente de navegar entre as funcionalidades do sistema de eventos.
    """

def generateCertificate():
"""
Função que permite gerar um certificado para um participante, exibindo as informações dos eventos
inscritos pelo participante e a carga horária total.

    A função começa exibindo um título "GERAR CERTIFICADO" e a lista de participantes cadastrados.
    O usuário é solicitado a selecionar um número de participante. Em seguida, a função exibe as informações
    dos eventos (workshops e palestras) inscritos pelo participante selecionado, incluindo nome, data, horário,
    local, carga horária e ministrante para cada evento.

    Além disso, a função calcula a carga horária total de todos os eventos inscritos e a exibe. Também exibe a data
    de emissão do certificado.

    Parâmetros:
        Nenhum.

    Comportamento:
    1. Exibe um título centralizado "GERAR CERTIFICADO" e a lista de participantes cadastrados usando 'listParticipants'.

    2. Entra em um loop que permite ao usuário selecionar um número de participante. O loop trata exceções de entrada
       inválida.

    3. Após a seleção do participante, a função exibe um título com o nome do participante selecionado e, em seguida,
       exibe as informações dos eventos (workshops e palestras) inscritos por esse participante, incluindo nome, data,
       horário, local, carga horária e ministrante para cada evento.

    4. Calcula a carga horária total somando a carga horária de todos os eventos inscritos.

    5. Exibe a carga horária total, a data de emissão do certificado e chama a função 'back' para retornar ao menu principal.

    6. Aguarda por 3 segundos antes de encerrar a execução.

    Uso:
    A função 'generateCertificate' é usada quando um administrador deseja gerar um certificado para um participante específico.

    Exemplo:
    generateCertificate()

    Observações:
    - O participante selecionado deve estar cadastrado no sistema e ter eventos inscritos para que um certificado seja gerado.
    """
