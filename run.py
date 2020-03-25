import requests
from bs4 import BeautifulSoup


data = {}
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Entire Table
dataTable = soup.find(id='main_table_countries_today')
tbody = dataTable.find('tbody')

trs = tbody.find_all('tr')
for tr in trs:
    countryDetail = tr.find_all('td')
    countryName = countryDetail[0].text.strip()
    totalDeadths = countryDetail[3].text.strip()
    totalRecovered = countryDetail[5].text.strip()
    activeCases = countryDetail[6].text.strip()
    data[countryName] = [activeCases, totalRecovered, totalDeadths]

'''
for key in data:
    print(key , "  ->  ", data[key][0], ", ", data[key][1], ", ", data[key][2])
'''
print('---------------------------')
print('-------- COVID-19 ---------')
print('---------------------------')
wantToQ = True
while(wantToQ):
    countryNameInput = input('Enter Country Name : ')
    print('---------------------------')
    print('🤒 Active Cases : ', data[countryNameInput][0])
    print('😊 Recovered Cases : ', data[countryNameInput][1])
    print('💀 Fatal Cases : ', data[countryNameInput][2])
    ask = input('\nOne more? ')
    if ask == 'N':
        wantToQ = False