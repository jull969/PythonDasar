while True:
    nilai_siswa = int(input("Maskkan nilai siswa: "))

    if nilai_siswa >=75:
        print("Tuntas")
        break
    else:
        mengulang = input("Nilai belum tuntas.Mengulang? (Ya/Tidak): ")
        
        if mengulang.lower() =="ya":
            continue
        else:
            print("Tidak Tuntas")
            break