#Perulangan menggunakan fungsi 'while' pada angka

i = 1
while True:
  if i < 10:
    print "Saat ini i bernilai: ", i
    i = i + 1
  elif i >= 10:
    break

#Perulangan menggunakan fungsi 'for' pada angka

for i in range(1, 10):
  print i

#Perulangan menggunakan fungsi 'for' pada karakter huruf

resident_evil = ["Chris Redfield", "Leon Scott Kennedy", "Jill Valentine", "Ada Wong", "Claire Redfield"]
for tampil in resident_evil:
  print tampil
