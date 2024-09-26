import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("Dashboard/all_data.csv")

# Set title for the dashboard
st.title("Dashboard Analisis Penggunaan Sepeda")

# Sidebar for navigation
st.sidebar.header("Pilih Analisis")

# Dropdown menu for choosing the analysis type
analysis_type = st.sidebar.selectbox(
    "Pilih Jenis Analisis", 
    ["Data Penggunaan Sepeda", "Penggunaan Berdasarkan Kelembapan", 
     "Penggunaan Berdasarkan Kecepatan Angin", "Penggunaan Berdasarkan Situasi Cuaca", 
     "Penggunaan Berdasarkan Bulan"]
)

# Slider for filtering data based on the number of users
user_filter = st.sidebar.slider(
    "Filter Berdasarkan Jumlah Pengguna Sepeda", 
    min_value=int(day_df['cnt'].min()), 
    max_value=int(day_df['cnt'].max()), 
    value=(0, 1000)
)

# Filter data based on user input
filtered_df = day_df[(day_df['cnt'] >= user_filter[0]) & (day_df['cnt'] <= user_filter[1])]

# Display filtered data
st.subheader(f"Menampilkan Data untuk Jumlah Pengguna Sepeda antara {user_filter[0]} dan {user_filter[1]}")
st.dataframe(filtered_df)

# Analysis 1: Display basic data
if analysis_type == "Data Penggunaan Sepeda":
    st.subheader("Data Penggunaan Sepeda")
    st.dataframe(filtered_df)

# Analysis 2: Penggunaan Sepeda Berdasarkan Kelembapan
elif analysis_type == "Penggunaan Berdasarkan Kelembapan":
    st.subheader("Rata-rata Penggunaan Sepeda Berdasarkan Kelembapan")
    
    humidity_usage = filtered_df.groupby(pd.cut(filtered_df['hum'], bins=10))['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='hum', y='cnt', data=humidity_usage, palette='Blues', ax=ax)
    ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Kelembapan', fontsize=16)
    ax.set_xlabel('Kelembapan (%)', fontsize=12)
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda', fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

# Analysis 3: Penggunaan Sepeda Berdasarkan Kecepatan Angin
elif analysis_type == "Penggunaan Berdasarkan Kecepatan Angin":
    st.subheader("Hubungan antara Kecepatan Angin dan Penggunaan Sepeda")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=filtered_df, ax=ax)
    ax.set_title("Hubungan antara Kecepatan Angin dan Penggunaan Sepeda", fontsize=16)
    ax.set_xlabel('Kecepatan Angin (m/s)', fontsize=12)
    ax.set_ylabel('Jumlah Pengguna Sepeda', fontsize=12)
    sns.regplot(x='windspeed', y='cnt', data=filtered_df, ax=ax, scatter=False, color='red')
    plt.tight_layout()
    st.pyplot(fig)

# Analysis 4: Penggunaan Berdasarkan Situasi Cuaca
elif analysis_type == "Penggunaan Berdasarkan Situasi Cuaca":
    st.subheader("Rata-rata Penggunaan Sepeda Berdasarkan Situasi Cuaca")
    
    weather_usage = filtered_df.groupby('weathersit')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_usage, palette='viridis', ax=ax)
    ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Situasi Cuaca', fontsize=16)
    ax.set_xlabel('Situasi Cuaca', fontsize=12)
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda', fontsize=12)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Berat'])
    ax.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

# Analysis 5: Penggunaan Berdasarkan Bulan
elif analysis_type == "Penggunaan Berdasarkan Bulan":
    st.subheader("Pola Penggunaan Sepeda Berdasarkan Bulan")

    monthly_usage = filtered_df.groupby('mnth')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', data=monthly_usage, ax=ax, marker='o')
    ax.set_title("Pola Penggunaan Sepeda Berdasarkan Bulan", fontsize=16)
    ax.set_xlabel('Bulan', fontsize=12)
    ax.set_ylabel('Rata-rata Jumlah Pengguna', fontsize=12)
    plt.xticks(monthly_usage['mnth'])  # Set xticks to show all months
    plt.tight_layout()
    st.pyplot(fig)

# Display footer with your name
st.sidebar.markdown("---")
st.sidebar.markdown("Dibuat oleh: **Haeqal Salehudin**")
