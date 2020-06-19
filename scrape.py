from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('word_rank1.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\r')
csv_writer.writerow(['rank', 'word'])

years=['1-1000', '1001-2000', '2001-3000', '3001-4000',  '4001-5000', '5001-6000', '6001-7000', '7001-8000', '8001-9000', '9001-10000', '10001-12000',
    '12001-14000',  '14001-16000', '16001-18000', '18001-20000', '20001-22000' ,'22001-24000', '24001-26000', '26001-28000', '28001-30000',
    '30001-32000', '32001-34000', '34001-36000', '36001-38000', '38001-40000', '40001-41284']

for year in years:
    link = f'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/TV/2006/{year}'
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    j=1
    k=1
    i=1
    table = soup.find('table')
    for row in table.find_all('tr'):
        if (i==1):
            i=0
            continue
        for data in row.find_all('td'):
            if (j==1):
                rank = data.text
                j=0
            elif (k==1):
                word = data.text
                k=0
        csv_writer.writerow([rank, word])
        print(rank, word)
        j=1
        k=1

csv_file.close()


