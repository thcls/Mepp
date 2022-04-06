import requests
from bs4 import BeautifulSoup
from get_day_menu import *

url = 'https://www.ufca.edu.br/assuntos-estudantis/refeitorio-universitario/cardapios/'

def downloadmenu(url):

    site = requests.get(url)

    soup = BeautifulSoup(site.content, 'html.parser')
    month = soup.find('div', class_='ui accordion')
    links = month.findAll('a')

    response = requests.get(links[-1].get('href'))
    
    pdf = open("menu.pdf", 'wb')
    pdf.write(response.content)
    pdf.close()
    
downloadmenu(url)

## Agora a partir daqui é só implementar uma função para
## verificar periodicamente o menu e retornar o almoço ou
## a janta do respectivo dia
get_day_menu("menu.pdf", 3, almoco=False)
