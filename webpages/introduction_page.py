import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def page():
	st.header("Introduction")
	intro_image = Image.open('introimg.png')
	st.image(intro_image, caption= 'Project Diagram', use_column_width=True)
	st.subheader("Describe the end goal of your project.")
	st.write("""
	ROAR stands for Robot Open Autonomous Racing and is Berkeley's first AI race car competition. Our project aims to achieve the fastest lap in this virtual race by implementing a controller that can accomplish the following tasks: multicar interactions, real world mapping with Realsense, and autonomous driving with Autoware.
	Our project applies robotic concepts learned in UC Berkeley's EECS C106a class including dynamics, control theory, and path planning.
	As seen in the "Project Diagram" above, our project implements and tests various controllers, both physical and virtually, to lay the foundation for our team to build our own controller, optimized through reinforcement learning.
	Our physical car was lent to us through Berkeley's ROAR research group and uses a Raspberry Pi for sensing, a waypoint parser and analyzer for planning, and signaling to wheels and steering for actuation. Our virtual car was simulated using Carla (an autonomous driving software) in various racing environments.
	On our physical car, our project implemented a traditionally tuned PID controller with calibrated wheel encoders to understand the physical limitations of racing.
	On our virtual car, our project implemented Stanford's award-winning Stanley controller to explore renowned controllers that improve speed and handling.

	Using our physical and virtual car findings, we were able to create our own PID controller using reinforcement learning that we submitted to be used in the Berkeley ROAR race.
	""")
	st.subheader("Why is this an interesting project?")
	st.write("""
	Answer
	""")
	st.subheader("What interesting problems do you need to solve to make your solution work?")
	st.write("""
	Answer
	""")
	st.subheader("In what real-world robotics applications could the work from your project be useful?")
	st.write("""
	Answer
	""")