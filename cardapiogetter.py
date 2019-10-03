from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd

data = []

def getCardapio(url):
    
    html = urlopen(url)
    res = soup(html.read(),"html5lib");

    table = res.find('table')
    tbody = res.find('tbody')

    tableRows = tbody.find_all('tr')
    tableRows.pop(0)

    for row in tableRows:
        columns = row.find_all('td')
        if row:
            output_row = []
            for column in columns:
                    output_row.append(column.text)
            data.append(output_row)

    df = pd.DataFrame(data)
    dfLunch = df.iloc[0:7]
    dfLunch.reset_index(drop=True)

    dfDinner = df.iloc[8:16]
    dfDinner.reset_index(drop=True)

    new_header = dfLunch.iloc[0]
    new_header[4] = "Quinta-Feira"
    dfLunch = dfLunch[1:]
    dfLunch.columns = new_header
    new_header = dfDinner.iloc[0]
    new_header[4] = "Quinta-Feira"
    dfDinner = dfDinner[1:]
    dfDinner.columns = new_header

    if (dfLunch is not None) and (dfDinner is not None):
        print("Resultado pronto!")
        return [dfLunch, dfDinner]
    else:
        print("Erro")