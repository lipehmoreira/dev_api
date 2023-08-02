from flask import request
from flask_restful import Resource
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    # def put(self):
    #     dados = json.loads(request.data)
    #     lista_habilidades[id] = dados
    #     return dados

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]
