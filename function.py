# Penggunaan function pada python
def hello():
	print("Hello World")

hello()

#Penggunaan function pada python menggunakan parameter

def salam(ucapan):
    print(ucapan)

salam("Selamat Siang")

def luas_segitiga(alas, tinggi):
	luas = (alas * tinggi) / 2
	print "Luas Segitiga = %f" % luas;

luas_segitiga(6, 6)

#Penggunaan function dengan mengembalikan nilai

def luas_persegi(sisi):
	luas = sisi * sisi
	return luas

print "Luas Persegi: %d" % luas_persegi(6)

luas_persegi(6)