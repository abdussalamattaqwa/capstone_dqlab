import streamlit as st
import pandas as pd
import altair as alt

st.title("Korelasi rata-rata lama sekolah dan pengangguran di Indonesia")


st.write("Penelitian Polla (2021) mengungkapkan Pendidikan berpengaruh terhadap pengangguran. Pendidikan diposisikan sebagai sarana untuk peningkatan kesejahteraan melalui pemanfaatan kesempatan kerja yang ada dan mencerminkan tingkat kepandaian dan pencapaian pendidikan formal dari penduduk karena semakin tinggi pula kemampuan kerja atau produktivitas seseorang dalam bekerja. Pendidikan yang tinggi dapat mempengaruhi banyak sektor salah satunya ialah tingkat pengangguran. Jadi apakah Pendidikan dalam hal ini Rata rata lama sekolah memiliki korelasi dengan tingkat pengangguran di Indonesia?")

df = pd.read_csv("Presentase pengangguran diindonesia.csv")
st.dataframe(df.style.format({'Rata rata lama sekolah (Tahun)': '{:.2f}', 
                             'Presentase pengangguran (%)': '{:.2f}',
                             'Presentase bekerja(%)' : '{:.2f}'}))



st.caption("Badan Pusat Statistik merilis Rata-rata Lama Sekolah (RLS) dan Persentase Penduduk yang Pengangguran di Indonesia periode 2013 hingga 2021.")



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
    title="Grafik Rata-rata Lama Sekolah (Tahun) dan Persentase Pengangguran (%)"
)
st.altair_chart(chart, use_container_width=True)

st.write("Grafik diatas menunjukkan rata rata lama sekolah di indonesia cenderung stabil selama 9 tahun terakhir. Hal tersebut tercermin membaiknya rata-rata lama sekolah di Indonesia. Data dari tahun 2013 hingga 2021 hanya meningkat sebanyak 0,70% dari awalnya 7,61 tahun ke 8,54 tahun. Sedangkan persentase pengangguran mengalami fluktuasi selama sembilan tahun terakhir. Tingkat perubahan signifikan persentase pengangguran terjadi pada tahun 2019 hingga 2021 yang telah diketahui padaa periode tersebut merupakan awal dari munculnya COVID-19.")


st.subheader("Kesimpulan")
st.markdown("1. Rata-rata lama sekolah di Indonesia tidak mempengaruhi persentase pengangguran diindonesia.")
st.markdown("2. Rata-rata lama sekolah meningkat cenderung stabil dari tahun ke tahun")
st.markdown("3. Persentase pengangguran meningkat secara signifikan saat munculnya wabah COVID-19.")