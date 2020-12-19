import streamlit as st
import numpy as np
import pandas as pd

def page():
	st.header("Additional Materials")
	st.subheader("Github Code:")
	st.write("""
	### [Traditional PID and RL PID Code in Michael's ROAR Branch](https://github.com/wuxiaohua1011/ROAR/tree/roll_additions)
	 - [Traditional PID Agent](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/agent_module/pid_agent.py)
	 - [RL PID Agent](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/agent_module/rl_testing_pid_agent.py)

	### [Stanley and Roll Code in Michael's ROAR Branch](https://github.com/wuxiaohua1011/ROAR/tree/roll_additions)
	 - [Roll Agent](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/agent_module/jAM1Agent.py)
	 - [Roll Calculation Script](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/perception_module/ground_plane_detector.py)
	 - [Roll Controller](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/control_module/pid_roll_controller.py)
	 - [Stanley Agent](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/agent_module/jAM3Agent.py)
	 - [Stanley Controller](https://github.com/wuxiaohua1011/ROAR/blob/roll_additions/ROAR/control_module/bstanley_controller.py)
	""")
