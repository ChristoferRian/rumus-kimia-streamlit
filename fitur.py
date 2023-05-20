import streamlit as st
from utils import process_option

def main():
    #membuat menu di side bar bagian kiri
    st.sidebar.title("Menu")

    #ini opsi yang tersedia, bisa dikatakan ini fitur nya
    option = ["Normalitas", "Molaritas", "kadar(%b/v)", "kadar(PPM)", "Penentuan jenis larutan berdasarkan pH", "perhitungan pH"]

    #ini variabel yang cara kerja nya mengambil input dari user ketika dia memilih fitur
    selected_option = st.sidebar.selectbox("Pilih Fitur", option)
    
    #ini untuk title nya, yang tulisan paling gede di halaman home. kenapa gw taro di bagian bawah kode dan bukan dibagian atas kode?karna kalau gw taro diatas, python gak bakal bisa ngedapetin hasil input dari user karna python itu menjalankan kode baris per baris
    st.title(f"{selected_option}")

    #ini untuk mentrigger input fitur nya, dan menjalankan logic dari fitur nya
    if selected_option:
        process_option(selected_option)


#ini buat menjalankan file nya. jangan dihapus
if __name__ == "__main__":
    main()
