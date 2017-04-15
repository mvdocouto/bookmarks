# -*- coding: utf-8 -*-
u"""Definição inicial de views."""
from flask import Flask, url_for, jsonify, redirect
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.secret_key = 's3cr3t'


@app.errorhandler(404)
def rotas(error):
    u"""Retorna o status 404 e alista das urls diponíveis."""
    if app.debug == True:
        lista_urls = []
        for i in app.url_map.iter_rules():
            item = {'url': i.rule,
                    'view': i.endpoint,
                    'metodo': list(i.methods),
                    'argumentos': list(i.arguments)}
            lista_urls.append(item)
        reposta = {'erro': 'url not found', 'status_code': 404,
                   'urls_disponiveis': lista_urls}
    else:
        reposta = {'erro': 'url not found', 'status code': 404}
    return jsonify(reposta), 404

