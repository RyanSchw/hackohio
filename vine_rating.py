# CLI that allows you to rate, modify, or delete vine quote.
# Outputs CSV file
import csv

out = []

fname = input('Provide file name: ')
with open(fname, 'r') as f:
    line = ' '
    while line != '':
        line = f.readline().rstrip()
        res = input(f'(#/m/d) {line}: ') # Rate, modify, delete line
        if res == 'm':
            newline = input('Enter new line: ')
            rating = input('Enter rating: ')
            out.append([rating, newline])
        elif res == 'd':
            continue
        else:
            out.append([res, line])

with open(f'{fname[:-4]}.csv', 'w+') as f:
    csvWriter = csv.writer(f, delimiter=',')
    csvWriter.writerows(out)