if __name__ == '__main__':
    print('----------------------------')
    print('Aplikasi Testing')
    print('----------------------------')
    
    pilihan = raw_input('Login\nRegister\n----------------------------\nPilih mode     : ')

    if pilihan == 'Login':
        import getpass

        username = raw_input("Username: ")
        password = getpass.getpass()
        # password = raw_input("Password : ")
        if(username == 'SSSuryana009' and password == '300994'):
            print 'Selamat Datang'
        else:
            print 'Username atau Password Salah'

    elif pilihan == 'Register':
        username = raw_input("Masukkan Username : ")
        password = raw_input("Masukkan Password : ")

        print "Username anda = {} dan Password anda = {}".format(username, password)
    else:
        print('Masukkan pilihan 1 atau 2 !!')