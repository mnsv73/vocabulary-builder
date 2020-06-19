import requests
import json

#getting user input
x = input('Enter a word to search meaning for: ')
word = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + x
request = requests.get(word)
data = json.loads(request.text)
meaning = data[0]['meanings'][0]['definitions'][0]['definition']
synonyms = data[0]['meanings'][0]['definitions'][0]['synonyms']
#print(meaning,'\n',synonyms)

muse = 'https://api.datamuse.com/words?rel_gen=' + x
mureq = requests.get(muse)
data1 = json.loads(mureq.text)
#for entry in data1:
 #   print(entry['word'], entry['score'])

word2 = 'https://datayze.com/word-analyzer?word=book'
req2 = requests.get(word2)
print(req2.text)