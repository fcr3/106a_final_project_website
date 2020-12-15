import streamlit as st
import numpy as np
import pandas as pd

from webpages.home_page import page as home
from webpages.team_page import page as team
from webpages.project_page import page as project

from webpages.introduction_page import page as introduction
from webpages.design_page import page as design
from webpages.implementation_page import page as implementation
from webpages.results_page import page as results
from webpages.conclusion_page import page as conclusion
from webpages.team_page import page as team
from webpages.additionalmaterials_page import page as additionalmaterials

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
	if page_mode == 'Introduction':
		introduction()
	if page_mode == 'Design':
		design()
	if page_mode == 'implementation':
		implementation()
	if page_mode == 'Results':
		results()
	if page_mode == 'Conclusion':
		conclusion()
	if page_mode == 'Team':
		team()
	if page_mode == 'Additional Materials':
		additionalmaterials()
	if page_mode == 'temp':
		temppage()

if __name__ == '__main__':
	page_mode = sidebar()
	mainpage(page_mode)