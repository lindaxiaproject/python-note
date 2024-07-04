
"""
    将选择框和滑块添加到侧边栏，使用st.sidebar.slider and st.sidebar.selectbox
    而不是st.sliderand st.selectbox：

"""
import streamlit as st
import numpy as np
import pandas as pd

add_selectbox = st.sidebar.selectbox(
    '你最喜欢的联系方式',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    '请选择一个范围',
    0.0, 100.0, (25.0, 75.0)
)


