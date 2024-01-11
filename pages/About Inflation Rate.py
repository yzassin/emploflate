import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('data.csv')

st.set_page_config(page_title="Inflation Rate", page_icon="📈")
st.markdown("## Inflation Rate Over the Years")

if df['Inflation Rate (%)'].dtype != 'float64':
    df['Inflation Rate (%)'] = pd.to_numeric(df['Inflation Rate (%)'].str.rstrip('%'), errors='coerce')

selected_years_inflation = st.slider(
    "Select a range of years:",
    min_value=int(df['Year'].min()),
    max_value=int(df['Year'].max()),
    value=(int(df['Year'].min()), int(df['Year'].max()))
)

filtered_df_inflation = df[(df['Year'] >= selected_years_inflation[0]) & (df['Year'] <= selected_years_inflation[1])]

fig_inflation = px.line(filtered_df_inflation, x='Year', y='Inflation Rate (%)')
fig_inflation.update_layout(xaxis_title='Year', yaxis_title='Inflation Rate (%)')

st.plotly_chart(fig_inflation)
