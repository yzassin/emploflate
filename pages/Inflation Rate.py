import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv('data.csv')


st.set_page_config(page_title="Inflation Rate", page_icon="📈")
st.markdown("## Inflation Rate Over the Years")
df['Inflation Rate (%)'] = pd.to_numeric(df['Inflation Rate (%)'].str.rstrip('%'), errors='coerce')
st.area_chart(df[['Year', 'Inflation Rate (%)']].set_index('Year'))

fig_inflation = px.line(df, x='Year', y='Inflation Rate (%)', title='Inflation Rate Over the Years')
st.plotly_chart(fig_inflation)