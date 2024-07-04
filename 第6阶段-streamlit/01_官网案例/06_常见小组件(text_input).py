import streamlit as st
import numpy as np
import pandas as pd


x = st.slider("x")
st.write(x, "平方是：", x * x)

st.text_input("请输入您的名字", key="name")
st.session_state.name