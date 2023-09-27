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


def linha():
    print('=' * 30)


def linhaSimples():
    print('-' * 30)
