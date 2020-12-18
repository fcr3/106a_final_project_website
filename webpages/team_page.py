import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64

def page():
	st.header("Team")
	assets_path = 'webpages/profile_assets'

	st.subheader("Marleah Puckett")
	proof_image = Image.open(f'{assets_path}/Marleah.jpg')
	st.image(proof_image,
			 caption= 'Marleah, a foodie in Chinatown SF.',
			 width=300)
	st.write("""
	Marleah Puckett is a 4th year Mechanical Engineering student with a minor in
	EECS. Her interests include mechatronics, controls, and heat transfer.
	Pre-corona she enjoyed spending time with family and friends, travelling,
	and working out. Now, she spends most of her time playing Animal Crossing.

	Major contributions include working on the traditionally tuned PID controller
	for the physical car.
	 """)

	st.subheader("Michael Wu")
	proof_image = Image.open(f'{assets_path}/Michael.jpeg')
	st.image(proof_image,
			 caption= 'Michael Wu at Strawberry Peak.',
			 width=300)
	st.write("""
	Michael Wu is a senior studying computer science. He has taken courses in ML,
	artificial intelligence, algorithm, data structures, data science, databases
	and et cetera. He is also the lead software developer in the ROAR project
	and the head facilitator for the ROAR DeCal. At the same time, he also work
	at LBNL in the Computational Material Science department with the Materials
	Project developing automated pipelines.

	Michael's contributions include:
	 - Implemented the PID Controller
	 - Created and implemented the the ROAR software architecture
	 - Empirically found working PID K values in real life with Marleah.
	 - Integrated the Vive Tracking system in ROAR
	 - DIY hardware integration with the Vive Tracker
	 - Architected and implemented custom Gym environment
	 - Developed and trained the DDPG Reinforcement Learning PID Agent.
	 - Assisted teammates in their projects from understanding the ROAR platform to peer programming.
	""")

	st.subheader("Jonathan Wong")
	proof_image = Image.open(f'{assets_path}/Jonathan.jpg')
	st.image(proof_image,
			 caption= 'Jonathan enjoying a brisk Sunday morning walk.',
			 width=300)
	st.write("""
	Jonathan Wong is a 4th year Mechanical Engineering Major with a minor in EECS.
	His main interests are in design, audio tech, and music.  In his free time,
	he likes making music and playing badminton.

	Jonathan worked on calibrating the physical ROAR car, making sure the car
	actually ran as expected when we commanded it to go straight and turn.
	""")

	st.subheader("Flaviano Christian Reyes")
	proof_image = Image.open(f'{assets_path}/Christian.jpg')
	st.image(proof_image,
			 caption= 'Christian posing with the VIVE setup.',
			 width=300)
	st.write("""
	Christian is a 4th year EECS major and Data Science minor. His interests is
	in anything computer vision. His current projects deal with the intersection
	between AR/VR and machine learning, specially around the topic of scene
	synthesis. In his free time, he hangs out with his dog Butterbean, plays
	basketball, practices his dancing to be a Jabbawockee, and sleeps.

	Christian worked on the ground plane detection applications within ROAR,
	including the flood fill algorithm and the sparse sampling + KNN algorithm
	for roll calculation. He also helped Michael with the gym-tuned PID controller
	and helped implement the roll controller. His contributions to the gym-tuned
	PID controller include deciding the learning algorithm and conceptualizing the
	reward/penalty system. Michael and Christian consulted Professor Allen Yang,
	Professor Sastry, Michael Estrada, and Tyler Westenbroek for RL best practices
	and how to best create our learning environment. He also helped design the project
	website.
	""")

	st.subheader("James Cheney")
	proof_image = Image.open(f'{assets_path}/James2.jpg')
	st.image(proof_image,
			 caption= 'James in front of the Hermitage.',
			 width=300)
	st.write("""
	James is a MEng student in Control of Autonomous and Robotic systems. He is a
	Veteran of the US Navy’s Nuclear Power program, and currently, he is in a
	career transition from Nuclear Chemistry to Mechanical Engineering. He is experienced
	in operations, troubleshooting, and repair of a wide variety of mechanical,
	chemical, electrical, and fluid systems related to military and commercial
	power production, as well as automotive manufacturing. His interests include
	health and fitness, veganism, traveling. His hobbies include beach volleyball,
	surfing/bodysurfing, swing and blues dancing, and hiking.

	For this project, he wrote Stanley controller and innovated Roll controller,
	with help from Michael Wu and Christian Reyes. He also made the overview video.
	""")
