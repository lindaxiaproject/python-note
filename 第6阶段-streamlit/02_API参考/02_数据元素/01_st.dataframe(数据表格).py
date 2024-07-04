
"""
    将数据框显示为交互式表格。
    此命令适用于 Pandas、PyArrow、Snowpark 和 PySpark 的数据帧。
    它还可以显示可以转换为数据帧的其他几种类型，例如 numpy 数组、列表、集合和字典。

    st.dataframe(data=None, width=None, height=None, *, use_container_width=False,
                 hide_index=None, column_order=None, column_config=None)
"""
import streamlit as st
import pandas as pd
import numpy as np
import random

st.write("-----【1】传递Pandas Styler 对象来更改渲染的 DataFrame 的样式-----")
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
# st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0))


st.write("-----【2】通过column_config、hide_index或column_order自定义数据框------")
df = pd.DataFrame(
    {
        "name": ["路线图", "附加信息", "问题"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "应用名称",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("应用地址"),
        "views_history": st.column_config.LineChartColumn(
            "折线图 (最近30天)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.write("-----【3】st.dataframe支持use_container_width参数拉伸整个容器宽度-----")
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
st.checkbox("Use container width", value=False, key="use_container_width")
df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)