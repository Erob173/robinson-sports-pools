import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://scores.espn.go.com/golf/leaderboard'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("mastersscores.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)