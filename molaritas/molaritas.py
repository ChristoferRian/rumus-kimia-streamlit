import streamlit as st

def molaritasStart():
  opsi_molaritas = st.radio(
    "silahkan pilih :",
    ('Molaritas', 'Molalitas'))

  if opsi_molaritas == 'Molaritas':
    def Molaritas():
      st.divider()
      mol_larut = st.number_input('masukkan nilai zat mol yang terlarut :')

      Volume = st.number_input('masukkan volume larutan : (L)')

      if Volume != 0:
        mol = mol_larut / Volume
      else:
        mol = 0
      
      
      st.latex("Kadar_PPM = \\frac{Mol yang terlarut}{Volume} = \\frac{%s}{%s} = %s" % (mol_larut, Volume, mol))


      st.write('nilai molaritas dari larutan tersebut adalah', mol, 'mol')
    Molaritas()

  elif opsi_molaritas == 'Molalitas':
    def Molalitas():
      st.divider()
      massa_terlarut = st.number_input("Massa zat terlarut (gram)")
      massa_molekul = st.number_input("Massa molekul reaktif (gram/mol)")
      massa_pelarut = st.number_input("Massa zat pelarut (gram)")

      if massa_pelarut != 0:
        molalitas = (massa_terlarut * 1000) / (massa_molekul * massa_pelarut)
      else:
        molalitas = 0


      st.latex("Molalitas = \\frac{{Massa_{Terlarut} \\times 1000}}{{Massa_{Molekul} \\times Massa_{Pelarut}}}= \\frac{{%s \\times 1000}}{{%s \\times %s}} = %s" % (massa_terlarut, massa_molekul, massa_pelarut, molalitas))
      

      st.divider()
      st.write("Molalitas:", molalitas, 'mol')


    Molalitas()
      # Tambahkan kode logika untuk normalitas biasa di sini

molaritasStart()