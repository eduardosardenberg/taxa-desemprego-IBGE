#AUTOR: Eduardo Sardenberg Tavares

import pandas as pd
import requests
import matplotlib.pyplot as plt


def main():

    # Utilizando a API 
    request = requests.get('https://apisidra.ibge.gov.br/values/t/6381/n1/all/v/4099/p/all/d/v4099%201') 
    request = request.json()
    #print(request)

    #olhando o print do request, observei que o 'V' e o 'D3N' eram metricas importantes para o DataFrame
    taxa_desemprego = [float(i['V']) for i in request[1:]] 
    trimestre = [i['D3N'] for i in request[1:]]

    #Comecando a criar o DataFrame
    dfibge = pd.DataFrame( taxa_desemprego, index=trimestre, columns=['Taxa de Desemprego - IBGE'])

    dfibge.plot.line()
    plt.title('Taxa de Desemprego (2012 - Atualmente)')
    plt.xticks(rotation= 45) # ajustando a legenda para ficar legivel
    plt.ylabel('Taxa de desemprego - (%)') #colocando para ficar com porcentagem 
    plt.show()


if __name__ == '__main__':
    main()