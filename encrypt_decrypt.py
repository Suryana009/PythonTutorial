import string

abjad = string.printable


def enkrip(pesan):
    global abjad
    
    key = input('Masukkan key   : ')
    cipher = ''
    for i in pesan:
        if i in abjad:
            k = abjad.find(i)
            k = (k + key)%100
            cipher = cipher+abjad[k]
        else:
            cipher = cipher + i

    return cipher

def dekrip(cipher):
    global abjad
    key = input ('Masukkan key  : ')
   
    pesan = ''
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + i

    return pesan

if __name__ == '__main__':
    print('----------------------------')
    print('Caesar cipher by www.Ajarkoding.com')
    print('----------------------------')
    pilihan = int(raw_input('1. Enkripsi\n2. Dekripsi\n----------------------------\nPilih mode     : '))

    if pilihan == 1:
        pesan = raw_input('Masukkan pesan : ')
        print(enkrip(pesan))
    elif pilihan == 2:
        cipher= raw_input('Masukkan pesan : ')
        print(dekrip(cipher))
    else:
        print('Masukkan pilihan 1 atau 2 !!')