

import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Dataviewer
""")

df_file = st.file_uploader('Import file', type = ['xlsx'] )

if df_file is not None :   
    df = pd.read_excel(df_file)

    # st.write(df)
    # st.dataframe(df)


