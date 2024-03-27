import dados as dd
import utils as u
from time import sleep


class Participant:
    def registerParticipant():
        try:
            u.line()
            u.titleCentered("CADASTRO DE PARTICIPANTE")
            u.line()

            # Solicita ao usuário que informe o nome
            name = str(input("Informe seu nome: ")).strip().capitalize()

            # Validação do nome: verifica se o nome não está em branco
            while not name:
                name = (
                    str(input("Nome inválido. Informe seu nome: ")).strip().capitalize()
                )

            # Solicita ao usuário que informe o telefone celular
            number = str(input("Informe seu telefone (9 dígitos apenas): "))

            # Validação do telefone: verifica se é um número de 9 dígitos
            while not number.isdigit() or len(number) != 9:
                number = str(
                    input(
                        "Número de telefone inválido. Certifique-se de inserir 9 dígitos númericos: "
                    )
                )

            # Solicita ao usuário que informe a instituição vinculada
            institution = str(input("Instituição vinculada: ")).strip().capitalize()

            # Validação da instituição: verifica se o nome não está em branco
            while not institution:
                institution = (
                    str(input("Nome inválido. Informe o nome da instituição: "))
                    .strip()
                    .capitalize()
                )

            newParticipant = {
                "name": name,
                "number": number,
                "institution": institution,
                "minicoursesSelected": [],  # Lista de minicursos selecionados vazia
                "lecturesSelected": [],  # Lista de palestras selecionadas vazia
            }

            # Adicionar o novo participante á lista de participantes (users['participant'])
            dd.users["participants"].append(newParticipant)

            u.line()
            print(f"Usuário {name} adicionado com sucesso!")
            u.line()

            # Agora, vamos aguardar até que o usuário pressione 'Q' para sair
            u.back()

            sleep(2)
        except Exception as e:
            # Lidar com exceções em gerais e fornecer informçaões sobre o erro
            print(f"Ocorreu um erro durante o cadastro: {str(e)}")

    def listParticipants():
        u.line()
        u.titleCentered("LISTA DE PARTICIPANTES")
        u.line()

        # Loop para percorrer a lista de participantes e exibi-los
        for index, user in enumerate(dd.users["participants"]):
            # Exibe o índice e o nome do participante
            print(f'Índice: {index + 1} - Nome: {user["name"]} ')
            u.simpleLine()  # Função para imprimir uma linha divisória