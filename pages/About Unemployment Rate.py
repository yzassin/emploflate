import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data.csv')

st.set_page_config(page_title="Unemployment Rate", page_icon="📈")
st.markdown("## Unemployment Rate Over the Years")
if df['Unemployment Rate (%)'].dtype != 'float64':
    df['Unemployment Rate (%)'] = pd.to_numeric(df['Unemployment Rate (%)'].str.rstrip('%'), errors='coerce')

selected_years = st.slider(
    "Select a range of years:",
    min_value=int(df['Year'].min()),
    max_value=int(df['Year'].max()),
    value=(int(df['Year'].min()), int(df['Year'].max()))
)

filtered_df = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]

fig_unemployment = px.line(filtered_df, x='Year', y='Unemployment Rate (%)')
fig_unemployment.update_layout(xaxis_title='Year', yaxis_title='Unemployment Rate (%)')

st.plotly_chart(fig_unemployment)
