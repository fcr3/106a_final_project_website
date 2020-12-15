import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def page():
	st.header("Introduction")
	intro_image = Image.open('introimg.png')
	st.image(intro_image, caption= 'Project Diagram', use_column_width=True)
	st.subheader("Describe the end goal of your project.")
	st.write("""
	Answer
	""")
	st.subheader("Why is this an interesting project?")
	st.write("""
	Answer
	""")
	st.subheader("What interesting problems do you need to solve to make your solution work?")
	st.write("""
	Answer
	""")
	st.subheader("In what real-world robotics applications could the work from your project be useful?")
	st.write("""
	Answer
	""")