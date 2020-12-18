import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def page():
	st.header("Home")
	st.subheader("Team: Marleah Puckett, Michael Wu,  Jonathan Wong, Christian Reyes, James Cheney")
	st.write("""
	University of California, Berkeley
	""")
	home_image = Image.open('homeimg.png')
	st.image(home_image, caption= '"Float like a Cadillac, sting like a Beemer." - Lightning McQueen', use_column_width=True)
