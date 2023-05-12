import streamlit as st
from utils import process_option
# Daftar opsi untuk dropdown
options = ['Normalitas', 'Moralitas', "kadar(%b/v)", 'kadar(PPM)','Penentuan jenis larutan berdasarkan pH', 'perhitungan pH']

# Tampilkan dropdown di aplikasi web
selected_option = st.selectbox("Pilih opsi:", options)

# Periksa apakah opsi sudah dipilih
if selected_option:
  # Panggil fungsi process_option dengan opsi yang dipilih
  # disinilah function process_option di eksekusi
  process_option(selected_option)
