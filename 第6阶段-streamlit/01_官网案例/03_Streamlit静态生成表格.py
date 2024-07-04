"""
    生成10行20列表格，随机填充数据(不支持下载、缩放)
    Streamlit还有一个静态表生成的方法： st.table()
        执行命令：streamlit run 03_Streamlit静态表生成表格.py
"""
import streamlit as st
import numpy as np
import pandas as pd
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

st.table(dataframe)
