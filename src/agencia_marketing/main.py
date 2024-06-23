#!/usr/bin/env python
import sys
from agencia_marketing.crew import AgenciaMarketingCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Preciso de uma estrategia e copys tanto para anuncio para menssagen de whatsapp e o script de vendas para ser usado no whatsappp para converter lead em vendas do meu info produto que é um ebook, que vai te ensinar a como inbvestir em açoes e estar lucrando com a vaorizaçao das açoes e multiplicando seu patrimonio do absoluto zero, e meu publico alvo é homens de 23 a 35 anos, gostao de viajar, tem familia, tem de 1 a dois filhos, gostam de carros, poker, e tambem gostam de investir em açoes'
    }
    AgenciaMarketingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        AgenciaMarketingCrew().crew().train(n_iterations=int(sys.argv[1]))

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
