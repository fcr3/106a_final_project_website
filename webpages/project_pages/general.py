import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64

def page():
    assets_path = 'webpages/project_pages/general_assets'
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
    Our project must meet the course requirements of Sensing, Planning, and
    actuation. We split our group into 5 different sub projects that tackle each
    part. We are interested in creating different controllers and comparing their
    results in simulation -- to see which one would go faster. And then we would
    also like to experiment the same algorithm in real life to see if they extend.

    Therefore, we decide to pursue the real life PID controller project which
    involves GPS Localizations (Sensing), waypoint following planner (Planning),
    and a basic PID controller (actuation).

    We also created a Roll based controller and a Gym tuned PID controller
    because we are interested in comparing their empirical result against each
    other and the PID controller. Additionally, the Roll based controller uses
    an additional sensing module using the depth camera to calculate the roll.

    Lastly, we found that hardwares are not perfect. Therefore, we have a subproject
    that works on wheel encoder to make sure that the wheels are correctly aligned
    in real life for better performance.
    """)

    st.subheader("Describe the design you chose.")
    st.write("""
    On a high level, the ROAR project decided to initially not go with ROS
    because it is easier to get everyone’s hands on. Therefore, aligning with
    that decision, we are purely using the ROAR pipeline.

    The idea of the ROAR design is that an Agent, which metaphorically is
    the driver, will control the car using the modules that it implements.
    For example, the `PIDAgent` uses a SimpleWaypointFollower, a waypoint
    follower with look ahead waypoint point parsing capability, and PID
    Controller. We also have a variety of other Agents that do other things
    such as a RollControllerAgent that uses DepthToPointCloudDetector and a
    RollController.

    Lastly, on the hardware side, we have implemented multithreaded mode for
    all hardware components to make sure that polling data does not slow down
    the main process. Such as polling for arduino reading or waiting for socket
    data will not stall the main program.
    """)

    st.subheader(
    	"What design choices did you make when you formulated your design?\
    	What trade-offs did you have to make?")
    st.write("""
    The design choice we made forced us to code our own server and client for the
    Vive Tracker, while these might be provided in ROS. Furthermore, the
    multi-threaded mode has to be manually enabled because we are not following
    ROS’s publisher and subscriber model. But it is not a big deal since we have
    enough abstraction such that enabling multi-threading for a particular module
    is just a matter of adding 2 lines of code above the existing serial version.
    """)

    st.subheader(
    	"How do these design choices impact how well the project meets design\
    	criteria that would be encountered in a real engineering application,\
    	such as robustness, durability, and efficiency?")
    st.write("""
    Answer each of the mentioned criteria
    ##### Robustness
    We think that in a sense it is less robust, since
    introducing custom code nearly always introduce new bugs, not saying
    implementing our own framework. However, at the same time, it reduces our
    headache in trying to figure out why some ROS node stops working and some
    data are not being sent in a publisher subscriber mode. Or in other words,
    it makes debugging easier

    ##### Durability
    We think that our code is durable because it has to
    experience both hardware and software scrutiny, and small bugs might be
    easily discovered through different system malfunction and crashes. However,
    in terms of hardware durability, we implemented safety features, such as
    limiting how fast the motor can turn, to limit the speed and protect the
    vehicle.

    ##### Efficiency
    The program is not that efficient since it is written
    in python. However, disregarding language wise inefficiency, it is worth
    noting that we have multi-threaded mode so that we are taking full advantage
    of the Python language and the CPU.
    """)

    st.header("Implementation Questions")
    st.subheader("Describe any hardware you used or built. Illustrate with pictures and diagrams.")
    st.write("""
    We built the Vive Tracker and the ROAR Car.
    """)
    image = Image.open(f'{assets_path}/roar_car_vive_tracker.jpg')
    st.image(image, caption='ROAR RC Car with VIVE Tracker',
    		 use_column_width=True)
    image = Image.open(f'{assets_path}/homeimg.png')
    st.image(image, caption='Squadron of ROAR RC Cars',
    		 use_column_width=True)

    st.write("""
    We also used a wheel encoder installed Yuri Murakami.
    """)

    st.subheader("What parts did you use to build your solution?")
    st.write("""
    The wheel encoder and the Vive Tracker, with some super glue and blue tape :)
    """)

    st.subheader(
    	"Describe any software you wrote in detail. Illustrate with diagrams,\
    	flow charts, and/or other appropriate visuals. This includes launch\
    	files, URDFs, etc.")
    st.write("""
    Please see each section for details.
    """)

    st.subheader("How does your complete system work? Describe each step.")
    st.write("""
    Please see each section for details.
    """)
