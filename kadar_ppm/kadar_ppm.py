import streamlit as st

col1, col2 = st.columns([3, 1])

def ppm_init():
  # with col1:
    st.divider()
    massa_zat_ppm = st.number_input('masukkan massa zat terlarut : (mg)')

    Volume_zat_ppm = st.number_input('masukkan volume larutan : (L)')

    if Volume_zat_ppm != 0:
      ppm = massa_zat_ppm / Volume
    else:
      ppm = 0
    st.write('nilai PPM dari larutan tersebut adalah', ppm, 'mg/L')

  # with col2:

    # rumus_ppm_ppm = "PPM = \frac {massa_zat_ppm} {Volume_zat_ppm}"

    # # st.latex(f'a \over b ')
    # st.latex(f'{massa_zat_ppm} \over {Volume_zat_ppm}')
    # # st.latex(r```
    # PPM = \frac{1-r^{n}}{1-r}\right
    # ```)
  # with col1:
    



      # Tambahkan kode logika untuk normalitas biasa di sini

