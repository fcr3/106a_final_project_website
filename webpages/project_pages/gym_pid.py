import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64

def page():
	assets_path = 'webpages/project_pages/gym_pid_assets'

	st.write("""
	### Gym-Tuned PID Controller
	*By Michael Wu and Christian Reyes*
	""")
	st.video("https://www.youtube.com/watch?v=xJemmKPnML4")

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
