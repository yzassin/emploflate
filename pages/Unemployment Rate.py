# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data.csv')


st.set_page_config(page_title="Unemployment Rate", page_icon="📈")
st.markdown("# Unemployment Rate Over the Years")
df['Unemployment Rate (%)'] = pd.to_numeric(df['Unemployment Rate (%)'].str.rstrip('%'), errors='coerce')
st.line_chart(df[['Year', 'Unemployment Rate (%)']].set_index('Year'))

fig_unemployment = px.line(df, x='Year', y='Unemployment Rate (%)', title='Unemployment Rate Over the Years')
st.plotly_chart(fig_unemployment)