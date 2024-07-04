import streamlit as st
import numpy as np
import pandas as pd


"""
    生成10行20列表格，随机填充数据
    
    执行命令：streamlit run 02_凸显交互式表中的某些元素.py
"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

