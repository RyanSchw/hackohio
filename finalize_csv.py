import csv
import os

files = []
vines = []

for file in os.listdir('.'):
    if file.endswith(".csv"):
        files.append(file)

for file in files:
    with open(file, 'r') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        for i in rows:
            print(i)
            if i not in vines:
                vines.append(i)

with open('vines.csv') as f:
    csvWriter = csv.writer(f, delimiter=',')
    csvWriter.writerows(vines)
