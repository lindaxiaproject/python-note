
"""

    复选框的一种用例是隐藏或显示应用程序中的特定图表或部分。st.checkbox()采用单个参数，即小部件标签。
    在此示例中，复选框用于切换条件语句。
"""
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('单选框'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])



