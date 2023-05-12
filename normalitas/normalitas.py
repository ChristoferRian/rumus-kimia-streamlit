import streamlit as st
def normalitasStart():
    level = st.radio(
        "silahkan pilih rumus nya",
        ('biasa', 'lanjutan', 'advanced'))

    if level == 'biasa':
        def normalitas_biasa():
            st.write('Normalitas Biasa')
            print("Anda memilih Normalitas - Biasa.")
            # Tambahkan kode logika untuk normalitas biasa di sini
        normalitas_biasa()


    elif level == 'lanjutan':
        def normalitas_lanjutan():
            # Logika untuk normalitas lanjutan
            st.write('Normalitas lanjutan')
            print("Anda memilih Normalitas - Lanjutan.")
            # Tambahkan kode logika untuk normalitas lanjutan di sini
        normalitas_lanjutan()



    elif level == 'advanced':
        def normalitas_advanced():
            # Logika untuk normalitas advanced
            st.write('Normalitas advanced')
            print("Anda memilih Normalitas - Advanced.")
            # Tambahkan kode logika untuk normalitas advanced di sini
        normalitas_advanced()

    else:
        print('hello world')