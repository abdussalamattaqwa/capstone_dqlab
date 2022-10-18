import streamlit as st
import pandas as pd
import altair as alt

st.title("Korelasi rata-rata lama sekolah dan pengangguran di Indonesia")

st.write("Pengangguran sering dikaitkan dengan pendidikan seseorang, apakah pendidikan atau lama sekolah mempengaruhi jumlah pengangguran di Indonesia?")
df = pd.read_csv("Presentase pengangguran diindonesia.csv")
st.dataframe(df.style.format({'Rata rata lama sekolah (Tahun)': '{:.2f}', 
                             'Presentase pengangguran (%)': '{:.2f}',
                             'Presentase bekerja(%)' : '{:.2f}'}))



st.caption("Data diatas menunjukkan data rata rata lama sekolah dan pengangguran di indonesia yang diambil dari Badan Pusat Statistik Indonesia. Data yang tersedia adalah data dari 9 tahun terakhir.")



new_df1 = df[['tahun','Rata rata lama sekolah (Tahun)']]
new_df1 = new_df1.rename(columns={'Rata rata lama sekolah (Tahun)': 'value'})
new_df1 = new_df1.assign(label = 'Rata rata lama sekolah (Tahun)')

new_df2 = df[['tahun','Presentase pengangguran (%)']]
new_df2 = new_df2.rename(columns={'Presentase pengangguran (%)': 'value'})
new_df2 = new_df2.assign(label = 'Presentase pengangguran (%)')
new_df = pd.concat([new_df1, new_df2])

new_df['dates'] = pd.to_datetime(new_df['tahun'], format='%Y')

chart = alt.Chart(new_df).mark_line(point = True).encode(
    x = alt.X("dates", title="Year"),
    y="value",
    color='label',
).properties(
    title="Grafik Rata-rata Lama Sekolah (Tahun) dan Presentase Pengangguran (%)"
)
st.altair_chart(chart, use_container_width=True)

st.write("Grafik diatas menunjukkan rata rata lama sekolah di indonesia meningkat secara fluktuasif dari tahun ke tahun. Peningkatan tidak terjadi secara signifikan selama sembilan tahun terakhir. Data dari tahun 2013 hingga 2021 hanya meningkat sebanyak 0,70% dari awalnya 7,61 tahun ke 8,54 tahun. Sedangkan presentase pengangguran mengalami fluktuasi selama sembilan tahun terakhir.")

st.subheader("Rata-rata lama sekolah di Indonesia tidak terlalu mempengaruhi jumlah pengangguran diindonesia")
