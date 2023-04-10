import pickle
import streamlit as st

# membaca model
model = pickle.load(open('estimasi_harga_camera.sav', 'rb'))

# judul web
st.title('Aplikasi Harga Kamera')

ReleaseDate = st.number_input('Input Tahun Kamera')
MaxResolution = st.number_input('Input Jumlah Max_Res')
StorageIncluded = st.number_input('Input Jumlah Storage')
WeightIncBatteries = st.number_input('Input Berat Battery')
Dimensions = st.number_input('Input Jumlah Dimensions')

# Code untuk prediksi
predict = ''

# membuat button
if st.button('Prediksi Harga'):
    predict = model.predict(
        [[ReleaseDate, MaxResolution, StorageIncluded, WeightIncBatteries, Dimensions]]
    )
    st.write('Estimasi harga kamera ($) : ', predict)
    st.write('Estimasi harga kamera IDR (Rp) : ', predict*15000)
