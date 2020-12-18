import streamlit as st
import numpy as np
import pandas as pd
import base64

def page():
	st.header("Results")
	st.subheader("How well did your project work? What tasks did it perform?")
	st.write("""
	**Calibration:**
	Our calibration ends up being a success, being able to drive straight when
	issued our new command of 1554 on steering.  This will be our new “straight”
	command.
	""")

	st.subheader("Illustrate with pictures and at least one video.")
	st.write("""
	**Real Life PID Controller:**
	Results shown below. Here is a demo of our PID controller at
	Richmond Field Station.
	""")
	st.video("https://www.youtube.com/watch?v=S3GxDf1XGBA")

	st.write("""
	**Gym-Tuned PID Controller:**
	Here is a demo of our RL PID agent.
	""")
	st.video("https://www.youtube.com/watch?v=xJemmKPnML4")

	st.write("""
	**Roll Controller:**
	Here is a demo of Roll controller agent.
	""")
	st.video("https://www.youtube.com/watch?v=kTxV4qfiV6o")

	st.write("""
	**Stanley Controller:**
	Here is a demo of Stanley controller agent.
	""")
	st.video("https://www.youtube.com/watch?v=Tj12WJK7HaE")

	st.write("""
	**Performance Breakdown:** Here is a table of showing the performance of our
	racing agents and their controllers.
	""")
	st.write(pd.DataFrame({
		"Controller": ['PID', 'RL PID', 'Roll', 'Stanley'],
		"Lap Time (Seconds)": [121.816164255, 119.655861378, 103.274860382, None],
		"Lap Time (Min:Sec)": ['2:01', '1:59', '1:43', None]
	}))

	st.write("""
	**Calibration:**
	Results shown below.
	""")
	calib_assets_path = 'webpages/project_pages/calibration_assets'
	file_ = open(f'{calib_assets_path}/calibrated.gif', 'rb')
	contents = file_.read()
	data_url = base64.b64encode(contents).decode('utf-8')
	file_.close()
	st.markdown(
	    f'<img src="data:image/gif;base64,{data_url}" alt="Uncalibrated"><br/>',
	    unsafe_allow_html=True,
	)
