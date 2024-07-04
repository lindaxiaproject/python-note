"""
    创建demo
        "/Users/linhong/PycharmProjects/python-note/第6阶段-streamlit/01_官网案例"
        streamlit run 01_创建第一个streamlit案例.py
        支持热加载
"""
import streamlit as st
import pandas as pd


x = st.slider("x")
st.write(x, 'squared is', x * x)
