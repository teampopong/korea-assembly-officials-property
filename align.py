# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import csv
import re

price_re = re.compile(r',"?[\d,]+"?,')
int_re = re.compile(r'^\d+$')


def _rows():
    rows = []

    with open('2012_open_19assembly_20130214.csv', 'r') as f:
        for line in f:
            line = line.decode('utf-8').strip()
            no = line.split(',')[0]
            if not int_re.match(no) or int(no) != len(rows):
                rows.append(rows.pop() + line)
            else:
                rows.append(line)

    return rows



def main():
    rows = []
    category = ''
    with open('sanitized.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row = [cell.decode('utf-8') for cell in row]
            row = row[:3] + [cell for cell in row[3:] if cell]

            if '▶' in row[1]:
                category = row[1]
                continue

            elif '본인과의 관계' == row[1]:
                continue

            elif len(row) < 5:
                continue

            try:
                no, second, subcategory, item, price = row[:5]
            except Exception, e:
                line = ','.join(row)
                print e, line.encode('utf-8')

            if row[-2] == '성명':
                name = row[-1]
                continue

            owner = second
            row = [name, owner, category, subcategory, item, price]
            rows.append([cell.encode('utf-8') for cell in row])

    with open('aligned.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

if __name__ == '__main__':
    main()
