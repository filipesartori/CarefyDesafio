from DownloadV2 import Clica #Import da DEF que executa o código automático de Download

ano = ['20', '21', '22'] #Variavel com os anos pedidos no desafio
mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'] #Variavel com os meses

for i in ano: #Laço para correr a variavel com os anos
    for j in mes: #Laço para correr a variavel com os meses
        Clica('FurtoVeiculo', i, j) #DEF que executa o código
        


