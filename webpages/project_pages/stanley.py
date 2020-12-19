import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64

def page():
	st.write("""
	### Stanley Controller
	*By James Cheney and Michael Wu*
	""")
	st.video("https://www.youtube.com/watch?v=Tj12WJK7HaE")
	assets_path = 'webpages/project_pages/stanley_assets'

	st.header("Design Questions")
	st.subheader(
		"What design criteria must your project meet? What is the desired functionality?")
	st.write("""
	The design criteria is to smoothly, reliably, and quickly be able to autonomously
    maneuver a vehicle around a given road course. For now, we are concerned with
	simulated racing environments, so our ultimate goal is to achieve the fastest lap
    around the given Carla track while taking into account the previosly mentioned items.
    To this end, it was desired to test a variety of controllers and see which one
    performs best.
	""")

	st.subheader("Describe the design you chose.")
	st.write("""
	A classic Stanley Controller was selected and coded.
	""")

	st.subheader(
		"What design choices did you make when you formulated your design?\
		What trade-offs did you have to make?")
	st.write("""
	We stuck with the specifications that were described in the Stanley controller paper.
	We also consulted numerous resources on how to implement the Stanley controller,
	which are introduced in the references section.
	""")

	st.subheader(
		"How do these design choices impact how well the project meets design\
		criteria that would be encountered in a real engineering application,\
		such as robustness, durability, and efficiency?")
	st.write("""
	The Stanley controller is tried and true, being used in the first autonomous
	vehicle to win the DARPA Grand Challenge in the contest’s second year (no
	vehicles finished the off road course in the first year). It has been adapted
	and tested in other situations and is a well known alternative to controllers
	such as standard PID and Pure Pursuit controllers.
	""")

	st.header("Implementation Questions")
	st.subheader("Describe any hardware you used or built. Illustrate with pictures and diagrams.")
	st.write("""
	Not applicable.
	""")

	st.subheader("What parts did you use to build your solution?")
	st.write("""
	Not applicable.
	""")

	st.subheader("Describe any software you wrote in detail. Illustrate with diagrams, flow charts, and/or other appropriate visuals. This includes launch files, URDFs, etc.")
	st.write("""
	For each controller functions were written to take inputs and process needed
	information from them.  This information was converted to needed data and
	sent to the algorithm that determined the outputs of the controller.  Other
	system modifications were minor - such as copying an agent and modifying it
	to call the Stanley Controller instead of the already existing PID controller,
	and changing the initiating file to call this agent instead of the original.
	""")
	image = Image.open(f'{assets_path}/software_flow.png')
	st.image(image, caption='Flow Chart of Controller Software Events',
			 use_column_width=True)

	st.subheader("How does your complete system work? Describe each step.")
	st.write("""
	The Stanley lateral controller takes as inputs the position and pose of the
	vehicle and waypoints in the simulated world. This data is converted in a
	function into the vehicle reference frame, which is used to further process
	the data. The data is processed to determine the distance the vehicle is
	away from the desired path as well as the difference in heading of the
	desired path trajectory and the vehicle. This information is returned to
	where controller parent as cross track error and heading error, where it is
	fed into the following formula to determine the steering information sent to
	the vehicle actuator:
	""")

	st.latex(r'''
		f(x) = \begin{dcases}
					-1 & x \leq -1 \\
					\text{HeadingError} + \tan^{-1}\left( \frac{k \cdot \text{PositionError}}{\text{VehicleSpeed} + 10^{-5}} \right) & -1 < x < 1 \\
					1 & x \geq 1 \\
			  \end{dcases}
    ''')

	st.write("""
	From our observations, $k=1.8$ worked the best.

	While the Stanley controller works most of the time, it does not work reliably,
	in that it has uncovered a situation where the next waypoint provided by the
	system does not always update. Because the Stanley controller uses both heading
	and crosstrack error as inputs to the steering command, the misinformation
	provided by the expired waypoint sometimes causes the heading error to cancel
	the crosstrack error, resulting in a near zero steering command in a turn.
	This causes the vehicle to proceed straight to the outside edge of the curve.
	We plan to alleviate this problem by modifying the code to cycle through the
	way point queue to the next available whenever it is calculated the waypoint
	is behind the vehicle.  The controller seems to work fine other than this
	glitch.
	""")

	st.subheader("References")
	st.write("""
	 - [Three Methods of Vehicle Lateral Control: Pure Pursuit, Stanley and MPC](https://dingyan89.medium.com/three-methods-of-vehicle-lateral-control-pure-pursuit-stanley-and-mpc-db8cc1d32081)
	 - [Autonomous Automobile Trajectory Tracking for Off-Road Driving: Controller Design, Experimental Validation and Racing](http://ai.stanford.edu/~gabeh/papers/hoffmann_stanley_control07.pdf)
	 - [Path tracking controller of an autonomous armoured vehicle using modified Stanley controller optimized with particle swarm optimization](https://link.springer.com/article/10.1007/s40430-017-0945-z)
	 - [Geometric Lateral Control - Stanley](https://www.coursera.org/lecture/intro-self-driving-cars/lesson-3-geometric-lateral-control-stanley-bJoWh)
	""")
