import streamlit as st
import pandas as pd
import plotly.express as px

# Title and description
st.title("Visualisasi Interaktif - Sleep Efficiency Dataset")
st.markdown("""
Aplikasi ini memungkinkan eksplorasi interaktif dari data efisiensi tidur. 
Dataset mencakup informasi tentang durasi tidur, efisiensi tidur, kebiasaan gaya hidup, dan lainnya.
""")

st.markdown("""
## Kelompok 15
Anggota kelompok:
- **1301210503** Az Zahrah Nur Sabrina  
- **1301213036** Razita Ghina Fayyadah  
- **1301213112** Sofia Nafiu Nur Rohmah  
""")

# Load dataset
df = pd.read_csv("Sleep_Efficiency.csv")

# Display dataset
st.subheader("Data Awal")
st.write(df)

# Clean column names (optional)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Sidebar filters
st.sidebar.header("Filter Data")
age_filter = st.sidebar.slider("Usia (Age)", int(df['age'].min()), int(df['age'].max()), (20, 40))
duration_filter = st.sidebar.slider("Durasi Tidur (Jam)", float(df['sleep_duration'].min()), float(df['sleep_duration'].max()), (6.0, 8.0))
efficiency_filter = st.sidebar.slider("Efisiensi Tidur (%)", float(df['sleep_efficiency'].min()), float(df['sleep_efficiency'].max()), (0.5, 0.75))

# Filter data based on user input
filtered_data = df[
    (df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1]) &
    (df['sleep_duration'] >= duration_filter[0]) & (df['sleep_duration'] <= duration_filter[1]) &
    (df['sleep_efficiency'] >= efficiency_filter[0]) & (df['sleep_efficiency'] <= efficiency_filter[1])
]

st.subheader("Data Setelah Filter")
st.write(filtered_data)

if not filtered_data.empty:
    # Line Chart: Age vs Sleep Efficiency
    st.subheader("Efisiensi Tidur Berdasarkan Usia")
    age_grouped = filtered_data.groupby("age")["sleep_efficiency"].mean().reset_index()
    line_fig = px.line(
        age_grouped,
        x="age",
        y="sleep_efficiency",
        title="Sleep Efficiency vs Age",
        labels={"age": "Usia", "sleep_efficiency": "Rata-Rata Efisiensi Tidur"},
    )
    st.plotly_chart(line_fig)
    
    # Scatter plot: Sleep Duration vs Sleep Efficiency
    st.subheader("Visualisasi Durasi Tidur vs Efisiensi Tidur")
    scatter_fig = px.scatter(
        filtered_data,
        x="sleep_efficiency",
        y="sleep_duration",
        color="gender",
        title="Durasi Tidur vs Efisiensi Tidur",
        labels={"sleep_efficiency": "Efisiensi Tidur","sleep_duration": "Durasi Tidur (Jam)", "gender": "Gender"},
    )
    st.plotly_chart(scatter_fig)

    # Scatter plot: Gender Comparison on Sleep Efficiency
    st.subheader("Efisiensi Tidur Berdasarkan Gender")
    scatter = px.scatter(
        filtered_data, 
        x='gender', 
        y='sleep_efficiency', 
        title="Sleep Efficiency vs Gender", 
        color='gender',
        labels={"gender": "Gender","sleep_efficiency": "Efisiensi Tidur"}
    )
    st.plotly_chart(scatter)
else:
    st.error("Data kosong setelah filter. Sesuaikan filter untuk melihat hasil.")
