# CLI that allows you to rate, modify, or delete vine quote.
# Outputs CSV file
import csv

out = []

fname = input('Provide file name: ')
with open(fname, 'r') as f:
    for line in f:
        res = input(f'(#/m/d) {line.rstrip()}: ') # Rate, modify, delete line
        if res == 'm':
            newline = input('Enter new line: ')
            rating = input('Enter rating: ')
            out.append([rating, newline])
        elif res == 'd':
            continue
        else:
            out.append([res, line.rstrip()])

with open(f'{fname[:-4]}.csv', 'w+') as f:
    csvWriter = csv.writer(f, delimiter=',')
    csvWriter.writerows(out)