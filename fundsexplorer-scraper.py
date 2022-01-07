from urllib.request import urlopen, Request
from pyquery import PyQuery as pq
import lxml, lxml.html
import os
import datetime


##carrega os papeis de stocksList.csv
##stocksList = open('meusFiis.csv', 'r')
stocksList = open('AllFiis.csv', 'r')
papeis = stocksList.read().split(';')
stocksList.close()

## pegando o dia e mês
now = datetime.datetime.now()
dia = now.day-1
mes = now.month
data = str(dia)+"."+str(mes)


## cria diretorio para a data de hoje-1
#if (not os.path.isdir('./'+data)):
    #os.mkdir(data)

#def faltam(papeis):
    #print(len(papeis))

def getpapel(papel_):
    try:
                    url = "https://www.fundsexplorer.com.br/funds/"
                    #print(papel+": "+str(content.code))
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    conteudo = pq(html)
                    #print (conteudo)
                    resultado = conteudo(".indicator-value").text()
                    #print(type(resultado))
                    x = resultado.replace("R$ ","").replace(" ","|")
                    print(papel+"|"+x)                    
                    papeis.remove(papel_)
                    #print("Faltam "+str(len(papeis)))
                    
                    
    except Exception as e:
        #print("#ERRO: ",papel," ", str(e))
        #print(papeis)
        papeis.remove(papel_)

while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)
            


