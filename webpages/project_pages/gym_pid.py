import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64
import streamlit.components.v1 as st_comps

def page():
	assets_path = 'webpages/project_pages/gym_pid_assets'

	st.write("""
	### Gym-Tuned PID Controller
	*By Michael Wu and Christian Reyes*
	""")
	st.video("https://www.youtube.com/watch?v=w2g0dKvVW-c")

	st.write("""
	We decided to use Gym and stable-baseline to facilitate reinforcement
	learning tasks by reducing the amount of infrastructural code we have to
	write.

	Gym is a toolkit for developing and comparing reinforcement learning
	algorithms, it provides the basic architectures for functions such as **step,
	reset, render**. Furthermore, it supports built in callback functions that
	help with debugging.

	Stable-baseline is a set of improved implementations of reinforcement
	learning algorithms based on the OpenAI Baseline package.

	Specifically, we decided to adopt the Deep Deterministic Policy Gradient
	(DDPG) because it features a model-free off-policy algorithm for learning
	continuous actions. Learning a continuous action space is specifically
	important to us because we are trying to learn the target speed,
	Longitudinal K values, and the lateral K values of our controller. Those
	values are all in a continuous space. DDPG has two networks: the actor and
	the critic network. The Actor network proposes the next action given the
	current state; while the critic network predicts if the action is good or
	bad given a state and an action.

	Our proposed pipeline is as in the picture below, where our environment will
	output some observations to the actor module and critic module. Actor module
	will use that observation to produce the next action, while the critic
	network will evaluate the actor’s policy.
	""")
	ac_image = Image.open(f'{assets_path}/actor_critic.png')
	st.image(ac_image, caption= 'Actor Critic Diagram of our RL System',
			 use_column_width=True)

	st.write("""
	Our first proposal was to make our observation state be the concatenation
	of current speed, current throttle, current steering, current transform,
	and target transform. However, we quickly find that there might be too much
	input, since it is of shape (15, 1). Therefore, we reduced the observation
	state to just (3,1) by making our observation state be only current speed,
	current throttle, and current steering.

	Now that we have the observation space out of the way, we need to define
	our reward function such that the DDPG algorithm will converge according to
	our desired policy.

	We want to incentivize finishing a lap, go to the next waypoint, and go
	faster. We also want to decentivize collisions, stay in the same place, and
	by expert knowledge, we know that the track can handle speed greater than
	80, so we want to disincentivize speed less than 80.
	""")
	rew_image = Image.open(f'{assets_path}/reward_code.png')
	st.image(rew_image, caption= 'Image of our Reward/Penalty Function',
			 use_column_width=True)

	st.header("Design Questions")
	st.subheader(
		"What design criteria must your project meet? What is the desired functionality?")
	st.write("""
	Specifically for the ROAR Gym project, we decided to utilize the sensing
	data of GPS, vehicle throttle, steering, and put it into our simple waypoint
	following planning module, and into a PID controller.
	""")

	st.subheader("Describe the design you chose.")
	st.write("""
	Specifically for the ROAR Gym project, we decided to go with the gym
	environment because it is open source, easy to start with, and have a variety
	of supported examples, and future adaptations. And we chose to use a stable
	baseline as our algorithm specific implementation above this gym environment.
	""")

	st.subheader(
		"What design choices did you make when you formulated your design?\
		What trade-offs did you have to make?")
	st.write("""
	Specifically for the ROAR Gym environment, we streamed the entire concept of
	Agent into the Gym, and then formulated our customized function that extract
	and reformulate the needed data to feed into the gym observation, and action
	space. An agent knows about the camera data, current vehicle state, planning
	module state, and everything that is streamed into the vehicle. Now, since we
	have streamed this agent into the Gym, the gym environment also knows about
	that information.

	Unfortunately, the tradeoff we have to make is efficiency -- it is not
	efficient to copy all data into another module. However training a
	Reinforcement agent takes time and the time it took to copy the data turns
	out to be trivial.
	""")

	st.subheader(
		"How do these design choices impact how well the project meets design\
		criteria that would be encountered in a real engineering application,\
		such as robustness, durability, and efficiency?")
	st.write("""
	Specifically for the ROAR Gym project, I think we met the criteria pretty good.
	The RL trained PID controller turned out to be really robust in the sense
	that it will not collide, but at the same time drive decently fast. In fact,
	we won the award for not crashing a single time in this semester’s ROAR
	competition. In terms of efficiency, it is able to run at about 50 FPS.
	Putting this data in comparison with a traditional PID controller -- which
	is also about 55 FPS, i think that this simple neural net is performing
	really well.
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

	st.subheader(
		"Describe any software you wrote in detail. Illustrate with diagrams,\
		flow charts, and/or other appropriate visuals. This includes launch\
		files, URDFs, etc.")
	st.write("""
	See our description above for the implementation details and associated figures.
	""")

	st.subheader("How does your complete system work? Describe each step.")
	st.write("""
	Specifically for RL based PID controller, it is a infinite while loop with
	each loop doing...
	""")
	st_comps.html("""
	In Loop:
	<ol>
		<li>Get the vehicle state (Current transform, camera data)</li>
		<li>Planning module produces the next waypoint</li>
		<li>Feed the next waypoint and vehicle state into the RL based PID Controller</li>
		<li>RL based PID Controller will output the next throttle and steering</li>
		<li>Stream the throttle and steering into the environment that we are attached to currently (either simulation or real hardware)</li>
	</ol>
	""")
