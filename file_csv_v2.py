import csv

siswa = [
        ('Suryana', 'IT', 'Programmer'),
        ('Septian', 'IT', 'Designer'),
        ('Farhan', 'IT', 'Programmer')
    ]

f = open('karyawan.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama', 'Divisi', 'Job Posisi'))

#membuat file csv
for s in siswa:
    w.writerow(s)

f.close()
