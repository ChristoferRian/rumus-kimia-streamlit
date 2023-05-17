import sys
sys.path.append("./normalitas")
sys.path.append("./molaritas")
sys.path.append("./kadar_ppm")
sys.path.append("./kadar(bv)")
sys.path.append("./perhitungan_pH")



# import dulu semua logic dari rumus rumus nya disini pakai 'from NAMA_FILENYA import NAMA_FUNCTIONNYA'

from perhitungan_ph import hasilpH #ini logic dari perhitungan ph
from normalitas import normalitasStart #ini logic dari rumus normalitas
from molaritas import molaritasStart
from kadar_ppm import ppm_init

#ini function untuk memproses hasil pilihan dari dropdown
def process_option(option):
    # Pemrosesan logika berdasarkan opsi yang dipilih
    if option == "Normalitas":
        normalitasStart()
        print('Normalitas')
    elif option == "Molaritas":
        # Logika untuk opsi Moralitas
        molaritasStart()
        print("Anda memilih Moralitas. Lakukan pemrosesan Moralitas di sini.")
    elif option == "kadar(%b/v)":
        # Logika untuk opsi kadar(%b/v)
        print("Anda memilih kadar(%b/v). Lakukan pemrosesan kadar(%b/v) di sini.")
    elif option == "kadar(PPM)":
        ppm_init()
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
