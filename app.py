import streamlit as st
import pandas as pd

st.title("Korelasi rata-rata lama sekolah dan pengangguran di Indonesia")

st.write("Pengangguran sering dikaitkan dengan pendidikan seseorang, apakah pendidikan atau lama sekolah mempengaruhi jumlah pengangguran di Indonesia?")
df = pd.read_csv("Presentase pengangguran diindonesia.csv")
st.dataframe(df)

st.caption("Data diatas menunjukkan data rata rata lama sekolah dan pengangguran di indonesia yang diambil dari Badan Pusat Statistik Indonesia. Data yang tersedia adalah data dari 9 tahun terakhir.")

# st.line_chart(df)
st.line_chart(data=df,x='tahun', y=['Rata rata lama sekolah (Tahun)', 'Presentase pengangguran (%)'])
st.write("Grafik diatas menunjukkan rata rata lama sekolah di indonesia meningkat secara fluktuasif dari tahun ke tahun. Peningkatan tidak terjadi secara signifikan selama sembilan tahun terakhir. Data dari tahun 2013 hingga 2021 hanya meningkat sebanyak 0,70% dari awalnya 7,61 tahun ke 8,54 tahun. Sedangkan presentase pengangguran mengalami fluktuasi selama sembilan tahun terakhir.")

st.subheader("Rata-rata lama sekolah di Indonesia tidak terlalu mempengaruhi jumlah pengangguran diindonesia, namun rata-rata lama sekolah dapat mengurangi jumlah pengangguran meskipun tidak secara signifikan")
