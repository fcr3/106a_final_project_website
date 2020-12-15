import streamlit as st
import numpy as np
import pandas as pd

from webpages.project_pages.real_pid import page as real_pid
from webpages.project_pages.gym_pid import page as gym_pid
from webpages.project_pages.stanley import page as stanley
from webpages.project_pages.calibration import page as calibration

def page():
	st.write("""
	## Project Page
	""")

	app_mode = st.sidebar.selectbox(
		"Which part of the project do you want to see?",
	    ["Real Life PID Controller", "Gym Tuned PID Controller", 
	     "Stanley Controller", "Calibration"])

	if app_mode == 'Real Life PID Controller':
		real_pid()
	if app_mode == 'Gym Tuned PID Controller':
		gym_pid()
	if app_mode == 'Stanley Controller':
		stanley()
	if app_mode == 'Calibration':
		calibration()