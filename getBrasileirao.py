from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
turno1url = 'https://pt.wikipedia.org/wiki/Resultados_do_Campeonato_Brasileiro_de_Futebol_de_2018_-_S%C3%A9rie_A_(primeiro_turno)'
turno2url = 'https://pt.wikipedia.org/wiki/Resultados_do_Campeonato_Brasileiro_de_Futebol_de_2018_-_S%C3%A9rie_A_(segundo_turno)'

# opens the connection and downloads html page from url
turno1 = urlopen(turno1url)
turno2 = urlopen(turno2url)

# parses html into a soup data structure to traverse html

# as if it were a json data type.
t1 = soup(turno1.read(), "html.parser")
turno1.close()

t2 = soup(turno2.read(), "html.parser")
turno2.close()

# name the output file to write to local disk
out_filename = "partidas2018.csv"
# header of csv file to be written
headers = "data,time1,gols1,x,gols2,time2\n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)


geral1 = t1.findAll('table', {'style': 'width:100%; background: transparent; border-spacing: 0; border-collapse: collapse;'})
geral2 = t2.findAll('table', {'style': 'width:100%; background: transparent; border-spacing: 0; border-collapse: collapse;'})


datas = []
casa = []
placares = []
fora = []

for geral in geral1:
    data = geral.tbody.td.text
    tcasa = geral.tbody.findAll('td')[1].b.a.text
    tfora = geral.tbody.findAll('td')[3].b.findAll('a')[1].text
    placar = geral.tbody.findAll('td')[2].b.text
    
    datas.append(data[:-1])
    casa.append(tcasa)
    fora.append(tfora)
    placares.append(placar)
    
    
for geral in geral2:
    data = geral.tbody.td.text
    tcasa = geral.tbody.findAll('td')[1].b.a.text
    tfora = geral.tbody.findAll('td')[3].b.findAll('a')[1].text
    placar = geral.tbody.findAll('td')[2].b.text
    
    datas.append(data[:-1])
    casa.append(tcasa)
    fora.append(tfora)
    placares.append(placar)


golc = [int(placar[0]) for placar in placares]
golf = [int(placar[4]) for placar in placares]

for i in range(len(datas)):
    f.write(f'{datas[i]},{casa[i]},{golc[i]},x,{golf[i]},{fora[i]}\n')

f.close()  # Close the file
