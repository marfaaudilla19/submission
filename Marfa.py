import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='whitegrid')

# Set tema Streamlit
st.set_page_config(
    page_title="Bike Sharing System Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Membaca data CSV dari GitHub
dayy_df = pd.read_csv("https://raw.githubusercontent.com/marfaaudilla19/submission/main/all_data_bike.csv")

# Header Streamlit dengan judul menarik
st.title('🚲 Bike Sharing System Dashboard')

# Menambahkan deskripsi untuk memberikan konteks
st.markdown(
    "Selamat datang di Dashboard Bike Sharing System! Pada Dashboard ini akan diberikan informasi terkait Hubungan Hari, Musim, dan Pola Penggunaan Sepeda"
)

# Membuat tab untuk subheader
selected_tab = st.sidebar.radio("Pilih Menu", ["Hubungan", "Hari", "Musim","Jumlah Sepeda"])

if selected_tab == "Hubungan":
    st.subheader("Hubungan")

    # Membuat matriks korelasi
    corr_matrix = day_df.corr()

    # Visualisasi matriks korelasi menggunakan heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriks Korelasi antara Variabel pada Dataset Bike Sharing System')
    plt.show()

# Tab "Jumlah Sepeda"
elif selected_tab == "Jumlah Sepeda":
    st.subheader("Jumlah Sepeda")

    # Mengelompokkan data berdasarkan bulan dan menghitung total sepeda yang dipinjam
    monthly_rentals = day_df.groupby('mnth')['cnt'].sum()

    #Membuat diagram garis untuk pola penggunaan sepeda
    plt.figure(figsize=(10, 6))
    monthly_rentals.plot(kind='line', marker='o')
    plt.title('Total Peminjaman Sepeda per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Total Peminjaman')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.grid(True)
    plt.show()

    # Mengelompokkan data berdasarkan musim dan menghitung total sepeda yang dipinjam
    season_rentals = day_df.groupby('season')['cnt'].sum()

    #Membuat diagram garis untuk pola penggunaan sepeda
    plt.figure(figsize=(10, 6))
    season_rentals.plot(kind='line', marker='o')
    plt.title('Total Peminjaman Sepeda per Musim')
    plt.xlabel('Season')
    plt.ylabel('Total Peminjaman')
    plt.xticks(range(1, 5), ['Semi', 'Panas','Gugur','Dingin'])
    plt.grid(True)
    plt.show()

    # Mengelompokkan data berdasarkan jenis hari (hari kerja/hari libur) dan menghitung total sepeda yang dipinjam
    rentals_by_holiday = day_df.groupby('holiday')['cnt'].sum()

    # Visualisasi
    plt.figure(figsize=(8, 6))
    colors = ['lightgreen', 'skyblue']
    plt.pie(rentals_by_holiday, labels=['Hari Kerja', 'Hari Libur'], colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Persentase Peminjaman Sepeda pada Hari Kerja dan Hari Libur')
    plt.axis('equal')  # Agar pie chart terlihat bulat
    plt.show()

    # Mengelompokkan data berdasarkan kondisi cuaca dan menghitung total sepeda yang dipinjam
    rentals_by_weather = day_df.groupby('weathersit')['cnt'].sum()

    # Visualisasi
    plt.figure(figsize=(8, 6))
    rentals_by_weather.plot(kind='bar', color=['lightblue', 'orange', 'lightgrey'])
    plt.title('Total Peminjaman Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Total Peminjaman')
    plt.xticks([0, 1, 2], ['Cerah/Mendung', 'Kabut/Kabut Berawan', 'Hujan/Salju'], rotation=45)
    plt.grid(axis='y')
    plt.show()


st.caption("Copyright by MarfaAudilla")