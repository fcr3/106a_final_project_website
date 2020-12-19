import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64

def page():
	st.write("""
	### Real Life PID Controller
	*By Marleah Puckett and Michael Wu*
	""")
	assets_path = 'webpages/project_pages/real_pid_assets'

	st.video("https://www.youtube.com/watch?v=hMaLXqPO5DM")

	st.header("Design Questions")
	st.subheader(
		"What design criteria must your project meet? What is the desired functionality?")
	st.write("""
	The main goal of the traditionally tuned PID controller on the physical car
	is to achieve the fastest physical lap possible without running into any
	barriers. Since part of the project was to assemble a race track for the
	physical car, there was no target velocity or lap time, just to design and
	iteratively tune to improve the traditional PID controller. Through this,
	our group will learn about traditional control methods and discrepancies
	between our simulation and the real-world.
	""")

	st.subheader("Describe the design you chose.")
	st.write("""
	The design we chose was a traditionally tuned PID controller.
	""")

	st.subheader(
		"What design choices did you make when you formulated your design?\
		What trade-offs did you have to make?")
	st.write("""
	The traditionally tuned PID controller was used as a baseline for our project.
	Our group wanted to pick k values according to the traditional algorithm for
	tuning a PID controller and understand discrepancies between our simulation
	and the real-world. In terms of trade-offs, to tune a PID controller according
	to the traditional algorithm takes time and guess-work. First, a P controller
	is implemented and tuned, then a PD controller, and lastly a PID controller.
	The k values were picked after many test runs on the race track when the car
	produced the fastest lap without running into barriers.
	""")

	st.subheader(
		"How do these design choices impact how well the project meets design\
		criteria that would be encountered in a real engineering application,\
		such as robustness, durability, and efficiency?")
	st.write("""
	We'll address this question by topic.

	**Robustness:** A real autonomous race car will endure more disturbances
	than introduced to our vehicle on our designed track. For example, the car
	may need to race up steep inclines or handle off-roading. Since we did not
	have the ability to introduce all of these disturbances to our physical car,
	it is very likely that if we were to traditionally tune the PID controller
	of a real autonomous race car, different k values would be chosen. However,
	our algorithm/design chosen is solid and effective against disturbances as
	it is the commonly used method across industry.

	**Durability:** The traditionally tuned PID controller avoids barriers by
	following the collected waypoints and, intuitively, rejects disturbances.
	Our code also sets maximum velocity and motor RPM for safety and a short
	lookahead to reduce crashes and produce a smoother trajectory.

	**Efficiency:** Although it takes time to tune a PID controller, once it’s
	tuned, the traditional PID controller is extremely efficient. This is
	because, when it is properly tuned, it quickly rejects disturbances and
	reaches steady state.
	""")

	st.header("Implementation Questions")
	st.subheader("Describe any hardware you used or built. Illustrate with\
	 			  pictures and diagrams.")
	st.write("""
	We set up and used a Vive Tracker for our localization service. A Vive
	Tracker works by creating a wireless connection between the car and the
	headset which allows for localization of the car. URL for VIVE Tracker
	photo is [here](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bhphotovideo.com%2Fc%2Fproduct%2F1413238-REG%2Fhtc_99hanl002_00_vive_tracker_2018_tracker_dongle_cradle_1m_usb_a_micro_b.html&psig=AOvVaw0NkfE-x1KJzxseFDtc9jsG&ust=1608440742615000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCMiZ5Oqi2e0CFQAAAAAdAAAAABAF).
	""")
	image = Image.open(f'{assets_path}/goggles.JPG')
	st.image(image, caption= 'An Image of VIVE Goggles',
			 use_column_width=True)
	image = Image.open(f'{assets_path}/vive_tracker.png')
	st.image(image, caption= 'An Image of a VIVE Tracker',
			 use_column_width=True)

	st.write("""
	We set up and used a race track at the Richmond Field Station for physically
	racing the car. The track included a 2m wide path with 3 tight curves and 1
	large curve.
	""")
	image = Image.open(f'{assets_path}/track.jpg')
	st.image(image, caption= 'The Track at Richmond Field Station',
			 use_column_width=True)
	image = Image.open(f'{assets_path}/track_graph.png')
	st.image(image, caption= 'Plotly 3D scatterplot of Track',
			 use_column_width=False)

	st.write("""
	We used the ROAR race car, lent to us by the ROAR research group. The ROAR
	race car uses a Jetson Nano + RealSense for sensing, a waypoint parser and analyzer
	for planning, and signals to the wheels and steering for actuation.
	""")
	image = Image.open(f'{assets_path}/homeimg.png')
	st.image(image, caption= 'The Squadron of ROAR RC cars',
			 use_column_width=True)

	st.subheader("What parts did you use to build your solution?")
	st.write("""
	Aside from the track, we did not build any of the hardware. The track was
	built on the ground of the Richmond Field Station using rope, tape, and
	other basic building materials.
	""")

	st.subheader(
		"Describe any software you wrote in detail. Illustrate with diagrams,\
		flow charts, and/or other appropriate visuals. This includes launch\
		files, URDFs, etc.")

	st.write("""
	Here is a code snippet of how we find our K values for our PID controller.
	Full code can be found [here](https://github.com/wuxiaohua1011/ROAR/blob/main/ROAR/control_module/pid_controller.py?fbclid=IwAR2FvSHhgStReKUQU9mnrzmXtdz9N4yPmzxAe9JsKTrqmJkjsjODyrCQIK0).
	""")
	image = Image.open(f'{assets_path}/findk_code.png')
	st.image(image, caption= 'findk(...) Code Snippet',
			 use_column_width=True)

	st.write("""
	Here is a code snippet of our finalized K values. JSON can also be found
	[here](https://github.com/augcog/ROAR_Jetson/blob/b71c3bd34467c2a975335781d78995c980c353ff/configurations/pid_config.json).
	""")
	image = Image.open(f'{assets_path}/kvals_snippet.png')
	st.image(image, caption= 'findk(...) Code Snippet',
			 use_column_width=False)

	st.write("""
	The PID controller is implemented in the pid_controller.py file that uses
	the find_k_values function to look up k values hard-coded into the
	pid_config.json file. The k values hard-coded into the pid_config.json file
	are the k values found through testing different k values and picking the
	best ones (least amount of oscillation and deviation from the desired waypoints).
	At first, different PID k values were tested at different vehicle speeds,
	however after testing it was found that the PID k values were not affected
	significantly by vehicle speed so PID k values were set to be constant,
	despite vehicle speed for both the lateral and longitudinal controllers.
	""")
	image = Image.open(f'{assets_path}/pid_figure.png')
	st.image(image, caption= 'Searching-for-K-Values Workflow',
			 use_column_width=True)

	st.write("""
	The simple_waypoint_following_local_planner.py file is used to feed recorded
	waypoints into the PID controller. It works by setting the correct lookahead
	for the current vehicle speed, then getting the correct waypoint, and feeding
	that waypoint into the controller. You can find the .py file [here](https://github.com/wuxiaohua1011/ROAR/blob/main/ROAR/planning_module/local_planner/simple_waypoint_following_local_planner.py?fbclid=IwAR3fjAyI3_m7ys2mOfearqVZmxBopHhsyiGxOwgwfGfQim1CXe2ftyhca1I).
	""")

	st.subheader("How does your complete system work? Describe each step.")
	st.write("""
	The complete system works by setting the correct k values for the PID controller
	and continuously feeding the controller the next waypoint. This is what is
	used to calculate the car’s next desired location and send the appropriate
	signals to the steering and wheels of the car.
	""")
