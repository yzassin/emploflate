import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data.csv')

st.set_page_config(page_title="Time Trends", page_icon="📈")
st.markdown("## Time Trends: Economic Indicators from1991 to 2022")
# Convert percentage columns to numeric
percentage_columns = ['Inflation Rate (%)', 'Unemployment Rate (%)', 'Youth Unemployment Rate (%)', 'Labor Participation Rate (%)', 'GDP Growth Rate (%)']
for col in percentage_columns:
    df[col] = pd.to_numeric(df[col].str.rstrip('%'), errors='coerce')

# Filter data for the years 1991 to 2022
df_filtered = df[(df['Year'] >= 1991) & (df['Year'] <= 2022)]

# Allow user to select variables
selected_variables = st.multiselect('Select Variables', percentage_columns)

# Line plot for selected variables
fig = px.line(df_filtered, x='Year', y=selected_variables, title='Line Plot: Selected Variables over Time',
              labels={'value': 'Percentage', 'variable': 'Variable'})

# Display the line plot
st.plotly_chart(fig)