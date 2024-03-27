import dados as dd
import utils as u
from time import sleep


class Participant:
    """
    Classe que representa um participante do evento.

    Atributos:
        name: Nome do participante.
        number: Número de telefone do participante.
        institution: Instituição à qual o participante está vinculado.
        minicoursesSelected: Lista de minicursos selecionados pelo participante.
        lecturesSelected: Lista de palestras selecionadas pelo participante.
    """

    def registerParticipant():
        """
        Função para registrar um novo participante no evento.

        Raises:
            Exception: Se ocorrer qualquer erro durante o registro do participante.
        """

        try:
            # Exibe linhas e título centralizado
            u.line()
            u.titleCentered("CADASTRO DE PARTICIPANTE")
            u.line()

            # Solicita e valida o nome do participante
            name = str(input("Informe seu nome: ")).strip().capitalize()
            while not name:
                name = (
                    str(input("Nome inválido. Informe seu nome: ")).strip().capitalize()
                )

            # Solicita e valida o número de telefone do participante
            number = str(input("Informe seu telefone (9 dígitos apenas): "))
            while not number.isdigit() or len(number) != 9:
                number = str(
                    input(
                        "Número de telefone inválido. Certifique-se de inserir 9 dígitos númericos: "
                    )
                )

            # Solicita e valida a instituição do participante
            institution = str(input("Instituição vinculada: ")).strip().capitalize()
            while not institution:
                institution = (
                    str(input("Nome inválido. Informe o nome da instituição: "))
                    .strip()
                    .capitalize()
                )

            # Cria um dicionário para armazenar os dados do novo participante
            newParticipant = {
                "name": name,
                "number": number,
                "institution": institution,
                "minicoursesSelected": [],  # Lista de minicursos selecionados vazia
                "lecturesSelected": [],  # Lista de palestras selecionadas vazia
            }

            # Adiciona o novo participante à lista de participantes
            dd.users["participants"].append(newParticipant)

            # Exibe linhas e mensagem de sucesso
            u.line()
            print(f"Usuário {name} adicionado com sucesso!")
            u.line()

            # Aguarda o usuário pressionar 'Q' para sair
            u.back()

            sleep(2)

        except Exception as e:
            # Exibe mensagem de erro e informações sobre o erro
            print(f"Ocorreu um erro durante o cadastro: {str(e)}")

    def listParticipants():
        """
        Função para listar todos os participantes cadastrados.
        """

        # Exibe linhas e título centralizado
        u.line()
        u.titleCentered("LISTA DE PARTICIPANTES")
        u.line()

        # Percorre a lista de participantes e exibe os dados de cada um
        for index, user in enumerate(dd.users["participants"]):
            # Exibe o índice e o nome do participante
            print(f'Índice: {index + 1} - Nome: {user["name"]} ')
            u.simpleLine()  # Função para imprimir uma linha divisória
