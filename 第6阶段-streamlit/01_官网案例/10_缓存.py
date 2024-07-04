
"""
  Streamlit 缓存使您的应用程序即使在从 Web 加载数据、操作大型数据集或执行昂贵的计算时也能保持高性能。
  要在 Streamlit 中缓存函数，您需要使用两个装饰器（st.cache_data和st.cache_resource）之一来装饰它

"""
import streamlit as st
import numpy as np
import pandas as pd
import time


@st.cache_data
def long_running_function(param1, param2):
    return "cache"