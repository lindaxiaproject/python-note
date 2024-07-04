
"""
   当向应用程序添加长时间运行的计算时，您可以使用 st.progress()实时显示状态。
   我们导入时间。我们将使用该time.sleep()方法来模拟长时间运行的计算

"""
import streamlit as st
import numpy as np
import pandas as pd
import time

'开始长时间计算...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'计算中 {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...计算结束!'