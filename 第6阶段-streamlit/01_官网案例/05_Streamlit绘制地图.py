"""
    st.map()在地图上显示数据点。让我们使用 Numpy 生成一些示例数据并将其绘制在旧金山地图上
"""
import streamlit as st
import numpy as np
import pandas as pd


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'],)

st.map(map_data)

