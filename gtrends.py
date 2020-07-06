from pytrends.request import TrendReq
import csv

pytrends = TrendReq(hl='en-US', tz=360)

with open('relatedlist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 5
    for row in csv_reader:
        if (i<1): break
        pytrends.build_payload(row, cat=0, timeframe='today 5-y', geo= '', gprop='')
        df = pytrends.interest_over_time()
        x = (df[row].sum())
        if (x[0]>2000 and x[0]< 20000):
            print(x)
        i=i-1

#get full list
with open('relatedlist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

            


