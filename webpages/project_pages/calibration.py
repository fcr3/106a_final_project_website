import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64
import streamlit.components.v1 as st_comps

def page():
	st.write("""
	### Calibration
	*By Jonathan Wong and Michael Wu*
	""")
	assets_path = 'webpages/project_pages/calibration_assets'

	st.video("https://www.youtube.com/watch?v=80_u7MuXQJk")

	st.write("""
	Calibration is the first step from taking the ROAR project from simulations
	to the real world.  By first installing wheel encoders, we are able to test
	if the difference in motors and slip causes any drift in steering.
	From a quick up-side-down test, running the motors freely for a few seconds,
	we can see that there are no innate differences in the motors by their
	encoder readings as seen below, with entries 3-6 being the encoder values:
	""")
	proof_image = Image.open(f'{assets_path}/proof_encoders_work.PNG')
	st.image(proof_image, caption= 'Proof Encoders Work', use_column_width=True)

	st.write("""
	Running the car with a straight command (throttle 1500, steering 1500)
	uncalibrated has a severe drift to the left.  For clarification, steering
	1500 comes from the center value between 1000 and 2000, our steering range.
	With a quick visual check, we realize the encoder values are still
	relatively the same, even with this turning, so we conclude that the
	steering is a much bigger factor in our drift and needs to be calibrated.
	""")
	file_ = open(f'{assets_path}/uncalibrated.gif', 'rb')
	contents = file_.read()
	data_url = base64.b64encode(contents).decode('utf-8')
	file_.close()
	st.markdown(
	    f'<img src="data:image/gif;base64,{data_url}" alt="Uncalibrated"><br/>',
	    unsafe_allow_html=True,
	)

	st.write("""
	With mostly visual tuning, and assuming the camera is straight on the car,
	a straight command must not allow the center pixel of the camera view to
	change.  Thus we end up with a calibrated command of (throttle 1500,
	steering 1554).  To get this, our steering range is now set to 1054 to 2054.
	This yields the following result:
	""")
	file_ = open(f'{assets_path}/calibrated.gif', 'rb')
	contents = file_.read()
	data_url = base64.b64encode(contents).decode('utf-8')
	file_.close()
	st.markdown(
	    f'<img src="data:image/gif;base64,{data_url}" alt="Uncalibrated"><br/>',
	    unsafe_allow_html=True,
	)

	st.write("""
	Much better!  If a straight command from the simulations is now mapped to
	this calibrated straight command, we can expect similar performance.  Even
	if we ran the car blind of simulations, we expect it to have a more relaxed
	control system since the system does not have to make corrections every time
	the car drifts left out of bounds.  With a more relaxed system, we can
	expect better performance as well.
	""")

	st.header("Design Questions")
	st.subheader(
		"What design criteria must your project meet? What is the desired functionality?")
	st.write("""
	The main goal of calibration is to meld simulation and the real world together.
	This can be done by focusing on a simple straight throttle command.  If a
	straight command actually goes straight in real life, then our design
	criteria is met.
	""")

	st.subheader("Describe the design you chose.")
	st.write("""
	The final chosen method of calibration is 100% visual.  By keeping track of
	the middle pixel of the camera, assuming it is mounted straight, we can
	track the “straightness” of our car path.
	""")

	st.subheader(
		"What design choices did you make when you formulated your design?\
		What trade-offs did you have to make?")
	st.write("""
	Our original method was to use wheel encoders to track the path of the car.
	However, we realized that the deviation based on wheel slippage and motor
	differences was negligible, and our error was largely based on steering error.
	Thus, we switched to a visual method of calibration.
	""")

	st.subheader(
		"How do these design choices impact how well the project meets design\
		criteria that would be encountered in a real engineering application,\
		such as robustness, durability, and efficiency?")
	st.write("""
	In a real engineering application, this visual method technically yields more
	error, as it could propagate from an incorrect assumption that the camera is
	mounted perfectly straight.  However, in our case, it was a very quick and
	effective fix in scale with our project.
	""")

	st.header("Implementation Questions")
	st.subheader("Describe any hardware you used or built. Illustrate with pictures and diagrams.")
	st.write("""
	The ROAR car itself and the wheel encoders installed were the full set of
	hardware used for our calibration.  By default, our car has a large drift
	to the right due to steering, so this would not be caught by the wheel
	encoders.
	""")

	st.subheader("What parts did you use to build your solution?")
	st.write("""
	Originally we planned that the wheel encoders would be the solution to our
	drift problem, but we realized this was not the case, and we simply had to
	remap our steering base command to steer straight.  Thus, we used the
	encoders for testing, but actually only used the car’s steering system and
	camera for calibration.
	""")

	st.subheader(
		"Describe any software you wrote in detail. Illustrate with diagrams,\
		flow charts, and/or other appropriate visuals. This includes launch\
		files, URDFs, etc.")
	st.write("""
	Not applicable.
	""")

	st.subheader("How does your complete system work? Describe each step.")
	st.write("""
	Using the aforementioned straightness calibration method (look above for details),
	we are able to find that the calibrated “1500” centered steering command,
	corresponding to a steering range of 1000 to 2000, drifts left.  Our
	corrected steering center becomes 1554, corresponding to a steering range
	of 1054 and 2054.
	""")
