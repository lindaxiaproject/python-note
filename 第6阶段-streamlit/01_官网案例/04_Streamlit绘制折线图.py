"""
    streamlit支持多种流行的数据图表库，例如Matplotlib、Altair、deck.gl 等
    （1）应用程序中 st.line_chart()
    （2）使用 Numpy 生成随机样本，然后将其绘制成图表
"""
import streamlit as st
import numpy as np
import pandas as pd


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

