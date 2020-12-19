import streamlit as st
import numpy as np
import pandas as pd

def page():
    st.write("""
    ### General Information

    At this point in our report, we take some time to describe the individual
    sub-projects that were incorporated in our main final project. Select from
    the side bar menu to watch videos and read out the design and implementation
    of these sub-projects.

    We include this general information section in our report website because
    even on a macro scale, our final project is organized with a design and
    implementation in mind.
    """)

    st.header("Design Questions")
    st.subheader(
    	"What design criteria must your project meet? What is the desired functionality?")
    st.write("""

    """)

    st.subheader("Describe the design you chose.")
    st.write("""

    """)

    st.subheader(
    	"What design choices did you make when you formulated your design?\
    	What trade-offs did you have to make?")
    st.write("""

    """)

    st.subheader(
    	"How do these design choices impact how well the project meets design\
    	criteria that would be encountered in a real engineering application,\
    	such as robustness, durability, and efficiency?")
    st.write("""

    """)

    st.header("Implementation Questions")
    st.subheader("Describe any hardware you used or built. Illustrate with pictures and diagrams.")
    st.write("""

    """)

    st.subheader("What parts did you use to build your solution?")
    st.write("""

    """)

    st.subheader(
    	"Describe any software you wrote in detail. Illustrate with diagrams,\
    	flow charts, and/or other appropriate visuals. This includes launch\
    	files, URDFs, etc.")
    st.write("""
    Not applicable.
    """)

    st.subheader("How does your complete system work? Describe each step.")
    st.write("""

    """)
