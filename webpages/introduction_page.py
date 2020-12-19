import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def page():
	st.header("Introduction")
	assets_path = 'webpages/webpage_assets'
	intro_image = Image.open(f'{assets_path}/OverviewFigure.png')
	st.image(intro_image, caption= 'Project Diagram', use_column_width=True)

	st.write("""
	This project is part of a larger research project called ROAR. ROAR stands
	for Robot Open Autonomous Racing and is Berkeley's first AI race car competition.
	Our project is primarily concerned with making racing agents in the virtual
	environment. In the future, once we finalize our algorithms through computer simulations,
	we can port our algorithms to actual cars and try out strategies in reality.
	For this project, we built four agents that use different control strategies.
	These controllers include:
	 - A traditional PID controller
	 - A gym-tuned PID controller where K values are determined by learned policy with current state as input
	 - A controller with latitudinal control via PID and longitudinal control via roll calculated using depth camera data
	 - A Stanley contoller

	We test these agents using Carla, an autonomous driving software that acts
	as a framework for testing driving algorithms, and our results are reported
	in the results section of this website. Furthermore, we were able to test
	the traditional PID controller agent in a physical car at Richmond Field
	Station.

	Our project also implements and showcases a calibration of the ROAR car, which
	is ultimately helpful for the next step in the ROAR research pipeline since we
	would like our live trials to match up with our simulations (i.e. if we
	tell a car to go straight, it goes straight, just like in a virtual simulation).

	In the end, our project not only contributes (1) different types of agents for students
	and researchers to compare to and (2) improves the simulation-to-reality transition,
	but we also:
	 - Set up the Vive Tracker system in Richmond Field Station for GPS/State messages
	 - Built a gym environment for researchers in ROAR to train their RL agents

	These side contributions were necessary for us to develop our virtual agents
	and eventually test them in real life.
	""")

	st.subheader("Describe the end goal of your project.")
	st.write("""
	Our end goal was to achieve the fastest lap, whether that be in physical
	or virtual simulations. For the purposes of this project and the ROAR race
	this semester, we were primarily focused on getting the fastest lap time in
	the virtual race simulation that was open to students. We sent our RL PID
	agent to represent our group in the race because at the time, this was our
	fastest agent based on our experiments.
	""")

	st.subheader("Why is this an interesting project? What interesting problems\
	 			  do you need to solve to make your solution work?")
	st.write("""
	This is an interesting project for a number of reasons. First of all, the
	field of autonomous driving is a hot topic in research today, and companies
	have invested a lot of time and money into creating reliable and performant
	systems that could be used in production level environments. The public as a
	whole has not embraced automous driving strategies due to (but not limited to)
	(1) saftey concerns and (2) economic impact (automous vehicles could take
	away jobs). Although our research group is not actively solving this latter
	systemic issue, we are aware of the consequences of self-driving vehicles.

	What our project is primarily concerned with is speed and reliability, which
	relates to the safety concerns that the general public has about
	autonomous vehicles and the performance goals that car companies seek.
	We want to answer the following question: **how do we drive as
	fast as possible and avoid obstacles/collisions?** From this main question
	comes related subproblems such as:
	 - How do we know where to go? (A sensing and planning problem)
	 - How do we get from point $A$ to point $B$? (A sensing, planning, and actuation problem)

	For the purposes of our project, we drive around the virtual and physical environment
	and collect our vehicle's coordinates along the way. These waypoints give us
	the path we need to traverse. And in regard to the second question,
	we implement our variety of controllers and see which one yields the
	fastest lap without colliding into other objects.
	""")

	st.subheader("In what real-world robotics applications could the work from your project be useful?")
	st.write("""
	This was talked about in the previous paragraphs, but to reiterate, our
	project centers around autonomous vehicle research, which car companies
	have invested time and money in to develop production level systems. Our project
	work could be useful in figuring out which autonomous vehicle strategies to use in production,
	but utlimately, its up to others to figure out how they could use our work.
	For instance, our project could be useful in figuring out autonomous driving
	capabilities within personal cars, or it could be useful for deploying a
	feet of autonomous rideshare or delivery vehicles. In the end, it's all about imagination!
	""")
