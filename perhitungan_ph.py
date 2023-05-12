#Library
import streamlit as st

#sebelum nya itu lu pakai st.json buat bikin dictionary python nya, itu salah, cara buat 'dictionary' nama_variabel = { isi_dict }
#sebelum nya lu buat st.json({ isi dict }). itu salah, yang bener yang dibawah
dictPh = {
    'Merah': 'Asam Kuat',
    'Jingga': 'Asam Lemah',
    'Kuning': 'Asam Sangat Lemah',
    'Hijau': 'Netral',
    'Biru': 'Basa Sangat Lemah',
    'Ungu': 'Basa Lemah',
    'Violet': 'Basa Kuat'
}

# metode untuk menerima input dari user
#metode nya ada banyak, contoh :
# st.text_input, itu dia bakal nerima input dari user dalam bentuk string
# st.number_input, itu dia bakal nerima input dari user dalam bentuk float
# baca aja full nya di website streamlit
# options = st.selectbox(
#     'Pick a options',
#     ['Normalitas', 'Moralitas', "kadar(%b/v)", 'kadar(PPM)','Penentuan jenis larutan berdasarkan pH', 'perhitungan pH'])

# pH = st.number_input("Masukkan nilai pH nya: ")
# st.write('pH nya adalah ', pH)
# st.divider() #ini buat munculin garis yang ada ditengah kalimat ph nya adalah sama kekuatan ph nya
# hasil
def hasilpH():
    pH = st.number_input("Masukkan nilai pH nya: ")
    st.write('pH nya adalah ', pH)
    st.divider()


    if pH < 1:
        st.write("Asam sangat kuat")
    # if pH <= 1 or pH >= 14:
    #     st.write("Nilai Ph tidak valid")

#ini juga ada bug di nama array nya, seharusnya Merah M nya kapital, lu malah nulis merah m kecil
    elif pH >= 1 and pH <= 3:
        st.write("Nilai Ph memiliki sifat " + dictPh["Merah"])

#tadi ada bug di line ini lu malah nulis st.wite, seharusnya st.write dan itu susah loh nyari bug nya
#hadeh ini juga seharusnya lebih besar dari 3 dong, sebelum nya lu malah lebih kecil dari 4
    elif pH >= 3 and pH <= 5:
        st.write("Nilai Ph memiliki sifat " + dictPh["Jingga"])

#ini kan hasil input nya float ya,artinya bakal ada koma/desimal, jangan pakai angka fix dong :)
    elif pH >= 5 and pH <= 6:
        st.write("Nilai Ph memiliki sifat " + dictPh["Kuning"])
    
    elif pH >= 6 and pH <= 7:
        st.write("Nilai Ph memiliki sifat " + dictPh["Hijau"])
    
    elif pH >= 7 and pH <= 8:
        st.write("Nilai Ph memiliki sifat " + dictPh["Biru"])
    
    elif pH >= 8 and pH <= 10:
        st.write("Nilai Ph memiliki sifat " + dictPh["Ungu"])
    
    elif pH >= 10:
        st.write("Nilai Ph memiliki sifat " + dictPh["Violet"])
    # elif pH >= 10 and pH <= 14:
    #     st.write("Nilai Ph memiliki sifat " + dictPh["Violet"])

#panggil function nya, ini yang bakal eksekusi logic dari coding nya
hasilpH()

