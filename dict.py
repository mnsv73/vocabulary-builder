import requests
import json
import csv

#getting user input
x = input('Enter a word to search meaning for: ')
word = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + x
request = requests.get(word)
data = json.loads(request.text)
meaning = data[0]['meanings'][0]['definitions'][0]['definition']
print(meaning)

muse2 = 'https://api.datamuse.com/words?rel_trg=' + x
mureq2 = requests.get(muse2)
data2 = json.loads(mureq2.text)

csv_file = open('relatedlist.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\r')

for entry in data2:
    csv_writer.writerow([entry['word']])
    print(entry['word'])

csv_file.close()

