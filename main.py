import streamlit as st
import numpy as np
import pandas as pd

from webpages.home_page import page as home
from webpages.team_page import page as team
from webpages.project_page import page as project
from webpages.temp_page import page as temppage

st.title('ROAR: A 106A Final Project')

def sidebar():
	st.sidebar.title("Where do you want to go?")
	app_mode = st.sidebar.selectbox("",
	    ["Home", "Team", "Project", "temp"])
	return app_mode


def mainpage(page_mode):
	if page_mode == 'Home':
		home()
	if page_mode == 'Team':
		team()
	if page_mode == 'Project':
		project()
	if page_mode == 'temp':
		temppage()

if __name__ == '__main__':
	page_mode = sidebar()
	mainpage(page_mode)