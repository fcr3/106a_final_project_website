import streamlit as st
import numpy as np
import pandas as pd

def page():
	st.write("""
	### Real Life PID Controller
	Here's our first attempt at using data to create a table:
	""")

	df = pd.DataFrame({
	  'first column': [1, 2, 3, 4],
	  'second column': [10, 20, 30, 40]
	})
	df

	st.write("""
	Random chart data
	""")

	chart_data = pd.DataFrame(
	     np.random.randn(20, 3),
	     columns=['a', 'b', 'c'])

	st.line_chart(chart_data)

	map_data = pd.DataFrame(
	    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
	    columns=['lat', 'lon'])

	st.write("""
	Random map data
	""")
	st.map(map_data)
	st.video("https://www.youtube.com/watch?v=S3GxDf1XGBA")