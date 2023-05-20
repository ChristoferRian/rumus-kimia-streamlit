import streamlit as st

col1, col2 = st.columns([2, 2])

def ppm_init():
  # with col1:
    st.divider()
    massa_zat_ppm = st.number_input('masukkan massa zat terlarut : (mg)')

    Volume_zat_ppm = st.number_input('masukkan volume larutan : (L)')

    if Volume_zat_ppm != 0:
      ppm = massa_zat_ppm / Volume_zat_ppm
    else:
      ppm = 0
    


    st.latex("Kadar_{PPM} = \\frac{Massa Zat}{Volume} = \\frac{%s}{%s} = %s" % (massa_zat_ppm, Volume_zat_ppm, ppm))

    st.divider()
    st.write('nilai PPM dari larutan tersebut adalah', ppm, 'mg/L')