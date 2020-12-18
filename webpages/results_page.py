import streamlit as st
import numpy as np
import pandas as pd
import base64

def page():
	st.header("Results")
	st.write("""
	### Real Life PID Controller
	Results shown below. Here is a demo of our PID controller at
	Richmond Field Station.
	""")
	st.video("https://www.youtube.com/watch?v=S3GxDf1XGBA")

	st.write("""
	### Gym-Tuned PID Controller
	Here is a demo of our RL PID agent.
	""")
	st.video("https://www.youtube.com/watch?v=w2g0dKvVW-c")

	st.write("""
	### Roll Controller
	The Roll controller works better than expected, and was used to consistently
	set the fastest lap times. There are plans to modify and experiment with
	the controller to improve upon the design. One plan is to add a look ahead
	than adjust speed downward when the heading difference between the vehicle
	and the desired path is increasing.  This indicates the vehicle is
	approaching a turn.  In this way the vehicle can slow in anticipation of
	turning, and accelerate to maximum allowed roll as the road straightens.
	This will allow for more aggressive speeds at all points as the vehicle will
	not enter a turn at full speed and lose control.
	""")
	st.write("""
	Here is a demo of Roll controller agent.
	""")
	st.video("https://www.youtube.com/watch?v=kTxV4qfiV6o")

	st.write("""
	### Stanley
	While the Stanley controller works most of the time, it does not work very
	well, in that it has uncovered a situation where the next waypoint provided
	by the system does not always update. We plan to alleviate this problem by
	modifying the code to cycle through the way point queue to the next available
	whenever it is calculated the waypoint is behind the vehicle. The controller
	seems to work fine other than this glitch.
	""")
	st.write("""
	Here is a demo of Stanley controller agent.
	""")
	st.video("https://www.youtube.com/watch?v=Tj12WJK7HaE")

	st.write("""
	### Performance Breakdown
	Here is a table of showing the performance of our
	racing agents and their controllers.
	""")
	st.write(pd.DataFrame({
		"Controller": ['PID', 'RL PID', 'Roll', 'Stanley'],
		"Lap Time (Seconds)": [121.816164255, 119.655861378, 103.274860382, None],
		"Lap Time (Min:Sec)": ['2:01', '1:59', '1:43', None]
	}))

	st.write("""
	### Calibration
	Our calibration ends up being a success, being able to drive straight when
	issued our new command of 1554 on steering.  This will be our new “straight”
	command.
	""")
	st.write("""
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
