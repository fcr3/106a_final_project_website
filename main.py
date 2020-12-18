import streamlit as st
import numpy as np
import pandas as pd

from webpages.home_page import page as home
from webpages.team_page import page as team
from webpages.introduction_page import page as introduction
from webpages.projects_page import page as projects
from webpages.results_page import page as results
from webpages.conclusion_page import page as conclusion
from webpages.additionalmaterials_page import page as additionalmaterials

st.title('ROAR: A 106A Final Project')

def sidebar():
	st.sidebar.title("Where do you want to go?")
	app_mode = st.sidebar.selectbox("",
	    ["Home", "Introduction", "Design and Implementation", "Results",
		"Conclusion", "Team", "Additional Materials"])
	return app_mode


def mainpage(page_mode):
	if page_mode == 'Home':
		home()
	if page_mode == 'Introduction':
		introduction()
	if page_mode == 'Design and Implementation':
		projects()
	if page_mode == 'Results':
		results()
	if page_mode == 'Conclusion':
		conclusion()
	if page_mode == 'Team':
		team()
	if page_mode == 'Additional Materials':
		additionalmaterials()

if __name__ == '__main__':
	page_mode = sidebar()
	mainpage(page_mode)
