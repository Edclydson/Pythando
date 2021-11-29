import requests
import json

# CONSULTA CLIMA DE FORTALEZA VIA API CLIMATEMPO
# ID FORTALEZA 8050
token = "INSIRA O TOKEN AQUI"
idcidade = '8050'


def agorafortaleza():

    url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + \
        idcidade + "/current?token=" + token
    resposta = requests.request("GET", url)
    retorno = json.loads(resposta.text)
    for dados in retorno:
        if dados == 'id':
            continue
        elif dados == 'data':
            break
        print(dados + " : " + str(retorno[dados]))
    for dados in retorno['data']:
        print(dados+": "+str(retorno['data'][dados]))


# CHAMANDO A FUNÇÃO
agorafortaleza()
