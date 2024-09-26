import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("Dashboard/all_data.csv")

# Set title for the dashboard
st.title("Dashboard Analisis Penggunaan Sepeda")

# Sidebar for navigation
st.sidebar.header("Pilih Analisis")

# Display the data in the dashboard
st.subheader("Data Penggunaan Sepeda")
st.dataframe(day_df)

# Option to display humidity analysis
if st.sidebar.checkbox("Rata-rata Penggunaan Sepeda Berdasarkan Kelembapan", key="humidity"):
    st.subheader("Rata-rata Penggunaan Sepeda Berdasarkan Kelembapan")
    humidity_usage = day_df.groupby(pd.cut(day_df['hum'], bins=10))['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='hum', y='cnt', data=humidity_usage, palette='Blues', ax=ax)
    ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Kelembapan', fontsize=16)
    ax.set_xlabel('Kelembapan (%)', fontsize=12)
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda', fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    
    st.pyplot(fig)

# Option to display windspeed analysis
if st.sidebar.checkbox("Hubungan antara Kecepatan Angin dan Penggunaan Sepeda", key="windspeed"):
    st.subheader("Hubungan antara Kecepatan Angin dan Penggunaan Sepeda")
    
    # Filter data to show only up to 1000 users
    filtered_windspeed_data = day_df[day_df['cnt'] <= 1000]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=filtered_windspeed_data, alpha=0.6, ax=ax)
    sns.regplot(x='windspeed', y='cnt', data=filtered_windspeed_data, scatter=False, color='red', ax=ax)
    ax.set_title('Hubungan antara Kecepatan Angin dan Penggunaan Sepeda', fontsize=16)
    ax.set_xlabel('Kecepatan Angin (m/s)', fontsize=12)
    ax.set_ylabel('Jumlah Pengguna Sepeda', fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    
    st.pyplot(fig)

# Option to display weather situation analysis
if st.sidebar.checkbox("Rata-rata Penggunaan Sepeda Berdasarkan Situasi Cuaca", key="weather"):
    st.subheader("Rata-rata Penggunaan Sepeda Berdasarkan Situasi Cuaca")
    weather_usage = day_df.groupby('weathersit')['cnt'].mean().reset_index()
    
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

# Option to display monthly usage analysis
if st.sidebar.checkbox("Pola Penggunaan Sepeda Berdasarkan Bulan", key="monthly"):
    st.subheader("Pola Penggunaan Sepeda Berdasarkan Bulan")
    monthly_usage = day_df.groupby('mnth')['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', data=monthly_usage, marker='o', color='purple', ax=ax)
    ax.set_title('Pola Penggunaan Sepeda Berdasarkan Bulan', fontsize=16)
    ax.set_xlabel('Bulan', fontsize=12)
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda', fontsize=12)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.grid(True)
    plt.tight_layout()
    
    st.pyplot(fig)

# Display footer with your name
st.sidebar.markdown("---")
st.sidebar.markdown("Dibuat oleh: **Haeqal Salehudin**")
