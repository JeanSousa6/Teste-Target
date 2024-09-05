import json

with open("dados.json") as dadosJson:
    dados = json.load(dadosJson)

diasDoMes = 30 

def media(dados):
    diasUteis = 0
    somaValores = 0.0 
    
    for i in dados:
        if(i['valor'] != 0.0):
            somaValores += i['valor']
            diasUteis += 1
    
    mediaFaturamento = somaValores / diasUteis
    return mediaFaturamento



def minimoValor(dados):
    valorMin = dados[0]['valor']
    diaDoFaturamento = dados[0]['dia']

    for i in range(1, diasDoMes):
        if(dados[i]['valor'] < valorMin and dados[i]['valor'] != 0.0):
            valorMin = dados[i]['valor']
            diaDoFaturamento = dados[i]['dia']
        
    return valorMin , diaDoFaturamento



def maximoValor(dados):
    valorMax = dados[0]['valor']
    diaDoFaturamento = dados[0]['dia']
    
    for i in range(1, diasDoMes):
        if(dados[i]['valor'] > valorMax and dados[i]['valor'] != 0.0):
            valorMax = dados[i]['valor']
            diaDoFaturamento = dados[i]['dia']
    
    return valorMax , diaDoFaturamento
 

def diasAcimaMedia(dados):
    mediaGeral = media(dados)
    diasFaturamentoAcimaMedia = 0

    for i in range(diasDoMes):
        if(dados[i]['valor'] > mediaGeral):
            diasFaturamentoAcimaMedia += 1

    return diasFaturamentoAcimaMedia


print(media(dados)) 
print(minimoValor(dados))
print(maximoValor(dados))
print(diasAcimaMedia(dados))

