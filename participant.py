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

    @staticmethod
    def registerParticipant():
        """
        Registra um novo participante no evento.
        """

        try:
            u.line()
            u.titleCentered("CADASTRO DE PARTICIPANTE")
            u.line()

            name = u.get_valid_input(
                "Informe seu nome: ", lambda x: x.strip().capitalize()
            )
            number = u.get_valid_input(
                "Informe seu telefone (9 dígitos apenas): ",
                lambda x: x.isdigit() and len(x) == 9,
            )
            institution = u.get_valid_input(
                "Instituição vinculada: ", lambda x: x.strip().capitalize()
            )

            newParticipant = {
                "name": name,
                "number": number,
                "institution": institution,
                "minicoursesSelected": [],
                "lecturesSelected": [],
            }

            dd.users["participants"].append(newParticipant)

            u.line()
            print(f"Usuário {name} adicionado com sucesso!")
            u.line()

            u.back()
            sleep(2)

        except Exception as e:
            print(f"Ocorreu um erro durante o cadastro: {str(e)}")

    @staticmethod
    def listParticipants():
        """
        Lista todos os participantes cadastrados.
        """

        u.line()
        u.titleCentered("LISTA DE PARTICIPANTES")
        u.line()

        participants = dd.users["participants"]

        for index, participant in enumerate(participants, start=1):
            print(f'Índice: {index} - Nome: {participant["name"]} ')
            u.simpleLine()
