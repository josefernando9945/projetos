import random

from django.core.management import BaseCommand
from instagran.models import Desafio

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Desafio.objects.all().delete()
        #
        #
        # for number in range(1, 11):
        #
        #
        #
        #     numero = random.random() * 100
        #
        #     ponto = round(numero)
        #
        #     # if (number%2) == 0:
        #
        #
        #     Desafio.objects.create(username=f"test {number}", name='nome', pontos=ponto)

        carros = [
            {'nome': 'vectra'},
            {'nome': 'fusca'},
            {'nome': 'kombi'},
            {'nome': 'verona'},

                   ]
        for carro in carros:

            carro['cor'] = 'branco'
            if carro['nome'] == 'vectra':
                carro['cor'] = 'azul'
            elif carro['nome'] == 'fusca':
                carro['cor'] = 'amarelo'
            elif carro['nome'] == 'kombi':
                carro['cor'] = 'verde'
            elif carro['nome'] == 'verona':
                carro['cor'] = 'preto'

            print(carro['nome'], carro['cor'])

        # contagem = 0
        #
        #
        #
        # for carro in carros:
        #     contagem = contagem + 1
        #
        #     # if contagem == 4:
        #     print(contagem, carro[0])


