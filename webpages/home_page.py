import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def page():
	st.header("Home")
	st.subheader("Team: Jonathan Wong, Michael Wu, Marleah Puckett, Christian Reyes, James Cheney")
	home_image = Image.open('homeimg.png')
	st.image(home_image, caption= '"Float like a Cadillac, sting like a Beemer." - Lightning McQueen', use_column_width=True)
	ucb_image = Image.open('UCB.png')
	st.image(ucb_image)