# import dulu semua logic dari rumus rumus nya disini pakai 'from NAMA_FILENYA import NAMA_FUNCTIONNYA'

from perhitungan_ph import hasilpH #ini logic dari perhitungan ph
from normalitas import normalitasStart #ini logic dari rumus normalitas


#ini function untuk memproses hasil pilihan dari dropdown
def process_option(option):
    # Pemrosesan logika berdasarkan opsi yang dipilih
    if option == "Normalitas":
        normalitasStart()
        print('Normalitas')
    elif option == "Moralitas":
        # Logika untuk opsi Moralitas
        print("Anda memilih Moralitas. Lakukan pemrosesan Moralitas di sini.")
    elif option == "kadar(%b/v)":
        # Logika untuk opsi kadar(%b/v)
        print("Anda memilih kadar(%b/v). Lakukan pemrosesan kadar(%b/v) di sini.")
    elif option == "kadar(PPM)":
        # Logika untuk opsi kadar(PPM)
        print("Anda memilih kadar(PPM). Lakukan pemrosesan kadar(PPM) di sini.")
    elif option == "Penentuan jenis larutan berdasarkan pH":
        # Logika untuk opsi Penentuan jenis larutan berdasarkan pH
        print("Anda memilih Penentuan jenis larutan berdasarkan pH. Lakukan pemrosesan di sini.")
    elif option == "perhitungan pH":
        hasilpH()
        print("Anda memilih perhitungan pH. Lakukan pemrosesan perhitungan pH di sini.")
    else:
        # Opsi tidak valid
        print("Opsi tidak valid. Silakan pilih opsi yang lain.")
