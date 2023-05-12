import streamlit as st

def molaritasStart():
  opsi = st.radio(
    "silahkan pilih ",
    ('Molaritas', 'Molalitas'))

  if opsi == 'Molaritas':
    def Molaritas():
      mol_larut = st.number_input('masukkan nilai zat mol yang terlarut :')

      Volume = st.number_input('masukkan volume larutan : (L)')

      if Volume != 0:
        mol = mol_larut / Volume
      else:
        mol = 0
      st.write('nilai molaritas dari larutan tersebut adalah', mol, 'mol')
      # Tambahkan kode logika untuk normalitas biasa di sini
    Molaritas()

  elif opsi == 'Molalitas':
    def Molalitas():
      massa_terlarut = st.number_input("Massa zat terlarut (gram)")
      massa_molekul = st.number_input("Massa molekul reaktif (gram/mol)")
      massa_pelarut = st.number_input("Massa zat pelarut (gram)")

      if massa_pelarut != 0:
        molalitas = (massa_terlarut * 1000) / (massa_molekul * massa_pelarut)
      else:
        molalitas = 0
      st.write("Molalitas:", molalitas, 'mol')


    Molalitas()
      # Tambahkan kode logika untuk normalitas biasa di sini

molaritasStart()