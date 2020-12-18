import streamlit as st
import numpy as np
import pandas as pd

from webpages.project_pages.calibration import page as calib_page
from webpages.project_pages.gym_pid import page as gym_pid_page
from webpages.project_pages.real_pid import page as real_pid_page
from webpages.project_pages.stanley import page as stanley_page

def page():
	st.header("Implementation")
	app_mode = st.sidebar.selectbox("Choose a subproject implementation:",
	    ["PID", "RL PID", "Stanley", "Calibration"])

	if app_mode == "PID":
		real_pid_page()
	if app_mode == "RL PID":
		gym_pid_page()
	if app_mode == "Stanley":
		stanley_page()
	if app_mode == "Calibration":
		calib_page()
