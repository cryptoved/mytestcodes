import requests
from bs4 import BeautifulSoup
import csv

# define the URLs to scrape
url1 = 'https://www.rootdata.com/Fundraising'
url2 = 'https://cryptorank.io/funding-rounds'

# send requests to the URLs and get the HTML content
html1 = requests.get(url1).content
html2 = requests.get(url2).content

# parse the HTML content with BeautifulSoup
soup1 = BeautifulSoup(html1, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')

# find the tables on the web pages
table1 = soup1.find('table')
table2 = soup2.find('table')

# create lists to store the data
data1 = []
data2 = []

# loop through the rows in the first table and store the data in the list
for row in table1.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    data1.append(row_data)

# loop through the rows in the second table and store the data in the list
for row in table2.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    data2.append(row_data)

# write the data to a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Table 1'])
    for row in data1:
        writer.writerow(row)
    writer.writerow(['Table 2'])
    for row in data2:
        writer.writerow(row)