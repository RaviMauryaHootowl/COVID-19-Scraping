import requests
from bs4 import BeautifulSoup

data = {}
URL = 'https://www.worldometers.info/coronavirus/#countries'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Entire Table
dataTable = soup.find(id='main_table_countries_today')
tbody = dataTable.find('tbody')

#Save results to file
file=open("results.txt","w")
file.write("")                   # to make file empty
file.close()

file=open("results.txt","a")


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

print("  ______   ______   ____    ____  __   _______                 __    ___   ")
print(" /      | /  __  \  \   \  /   / |  | |       \               /_ |  / _ \  ")
print("|  ,----'|  |  |  |  \   \/   /  |  | |  .--.  |    ______     | | | (_) | ")
print("|  |     |  |  |  |   \      /   |  | |  |  |  |   |______|    | |  \__, | ")
print("|  `----.|  `--'  |    \    /    |  | |  '--'  |               | |    / /  ")
print(" \______| \______/      \__/     |__| |_______/                |_|   /_/   \n")
wantToQ = True
while(wantToQ):
    countryNameInput = input('Enter Country Name : ')
    print(data)
    country='Country : '+countryNameInput
    acases='🤒 Active Cases : '+data[countryNameInput][0]
    rcases='😊 Recovered Cases : '+data[countryNameInput][1]
    fcases='💀 Fatal Cases : '+ data[countryNameInput][2]

    file.write('---------------------------')
    file.write(country)
    file.write(acases)
    file.write(rcases)
    file.write(fcases)

    print('---------------------------')
    print(acases)
    print(rcases)
    print(fcases)
    ask = input('\nOne more? ')

    if ask == 'N':
        wantToQ = False

file.close()
print('---------------------------')
print("Results saved to results.txt")
print('---------------------------')
