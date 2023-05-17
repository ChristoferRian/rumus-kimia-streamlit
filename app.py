import streamlit as st
from utils import process_option

def main():
    st.title("Aplikasi Kimia")

    # Sidebar
    st.sidebar.title("Menu")
    option = ["Normalitas", "Molaritas", "kadar(%b/v)", "kadar(PPM)", "Penentuan jenis larutan berdasarkan pH", "perhitungan pH"]

    selected_option = st.sidebar.selectbox("Pilih Fitur", option)

    if selected_option:
        process_option(selected_option)

if __name__ == "__main__":
    main()
