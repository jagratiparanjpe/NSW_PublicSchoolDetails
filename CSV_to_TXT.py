
# This file coverts CSV file to PSV#
import csv

with open('/Users/amitladsaongikar/Downloads/collections.csv', 'r') as fin, \
     open('NSWPublicSchoolData.txt', 'w') as fout:
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, reader.fieldnames, delimiter='|')
    writer.writeheader()
    writer.writerows(reader)
