import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Sunburst Chart: Proportion of SAT Score by Field of Study")

# Upload file
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="education_career_success")

    sat_by_field = df.groupby('Field_of_Study')['SAT_Score'].sum().reset_index()
    sat_by_field['Proportion'] = sat_by_field['SAT_Score'] / sat_by_field['SAT_Score'].sum()

    fig = px.sunburst(
        sat_by_field,
        path=['Field_of_Study'],
        values='Proportion',
        title='Proportion of SAT Score by Field of Study',
        color='Proportion',
        color_continuous_scale='Blues'
    )

    st.plotly_chart(fig)
