import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def page():
	st.header("Home")
	st.subheader("Team: Marleah Puckett, Michael Wu,  Jonathan Wong, Christian Reyes, James Cheney")
	st.write("""
	University of California, Berkeley
	""")
	assets_path = 'webpages/webpage_assets'
	home_image = Image.open(f'{assets_path}/homeimg.png')
	st.image(home_image,
			 caption= '"Float like a Cadillac, sting like a Beemer." - Lightning McQueen',
			 use_column_width=True)

	st.write("""
	Hello and welcome to our 106a final project website. In this website, you
	will find a detailed report about our project. The menu on the side will
	introduce subsections of our report. They include an introduction of our
	whole project, design and implementation details, our results, and finally,
	some discussion of future work. We also have provided profiles and a rundown
	of team contributions as well as additional materials that might be of
	interest to you.

	### Mini Introduction
	Our project builds upon the existing ROAR platform, and it is designed to
	work in both simulation and in real vehicle (with a couple hyper parameter
	changes).

	**Our Goal:** Achieve the fastest lap in the Carla virtual environment.

	Our project is divided into 5 distinct areas:
	 - Real life PID controller
	 - Reinforcement Learning based PID Controller
	 - Ground Plane Detection + Roll Controller
	 - Stanley Controller
	 - Wheel Encoder Calibration and Tuning

	The first four areas focus on agents that we tried to implement and test
	in Carla's simulated environment. We use some of our agents to compete in the
	ROAR race. The last area of our project focuses on the simulation-to-reality
	pipeline, which will be important when we want to eventually port our controllers
	to the physical ROAR RC car. Our contribution of calibrating the car allows
	us to witness expected commands, i.e. the command to go straight will lead
	to the car actually going straight.
	""")
