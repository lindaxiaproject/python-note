
"""

    用于st.selectbox从系列中进行选择。写入所需的选项，或者传递数组或数据框列。
"""
import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    '第1行': [1, 2, 3, 4],
    '第2行': [10, 20, 30, 40]
    })

option = st.selectbox(
    '哪个是你最喜欢的数?',
     df['第1行'])

'你的选择是: ', option



