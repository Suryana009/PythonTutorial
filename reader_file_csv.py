import csv

f = open('karyawan.csv', 'r')
reader = csv.reader(f)

for row in reader:
    print row

f.close()
