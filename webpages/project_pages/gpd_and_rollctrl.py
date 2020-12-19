import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64

def page():
    assets_path = 'webpages/project_pages/gpd_and_rollctrl_assets'
    st.write("""
    ### Ground Plane Detection and the Roll Controller
    *By James Cheney and Christian Reyes*

    Below is (1) a demo run of the controller and (2) an in-depth explanation
    of the Roll controller. Feel free to watch the video or read the content,
    as they pretty much go over the same thing.
    """)
    st.video("https://www.youtube.com/watch?v=kTxV4qfiV6o")
    st.video("https://www.youtube.com/watch?v=SvllzcfLZ7g")

    st.write("""
    As the name may suggest, the roll controller uses roll instead of PID for
    controlling longitudinal movement, i.e. controlling the throttle. Latitudinal
    movement is controlled with a hand-tuned, slightly adaptive PID. For the K
    values of the latitudinal movement PID, look at the real life PID page, since
    we use their same configuration. Waypoints are generated from going around
    the track and collecting vehicle coordinates along the way.

    The easiest way to get the roll of the car is by querying Carla, but in
    the real world, we need to rely on sensors to establish the transformation
    attributes of the car. For our system, the sensors that we have are RGB and
    depth cameras. Using the depth camera input, we can segment the road upon
    which the car is traveling, and by converting the depth data of the road to
    a point cloud, we can calculate the road normal. Finally, with the road
    normal, we can find the angle between the road normal vector and the axis
    which divides the frame to find the roll. In the case of Carla, this axis
    would be the positive y-axis of the camera frame. The angle can be found by
    (1) normalizing the road normal vector, (2) taking the dot product of the
    normalized road normal and the positive y-axis [0, 1, 0], and (3) calculate
    the inverse cosine of this dot product. This calculation is based on the
    definition of the dot product, which when considering normalized vectors is
    simply just the cosine of the angle between the vectors.
	""")

    st.write("""
    ### Ground Plane Detection

    There are multiple ways to segment the ground from the boundaries and
    obstacles on the road. Complex systems may use convolutional neural networks
    on images to segment the road, but for our purposes, we usually resort to a
    flood fill strategy. First, we get the point cloud of our sensed environment
    from the depth camera. The point cloud is calculated via the inverse of the
    camera intrinsics matrix, which converts the depth data to 3D points in the
    camera frame. Then we estimate normals per point by (1) taking its neighbors,
    (2) calculating the difference vectors pointing from the left neighbor to
    the right neighbor and the back neighbor to the front neighbor, and (3) with
    these difference vectors, we compute the cross product and assign the
    resulting vector as the estimated normal. One fascinating observation is
    that our Numpy variation of estimating normals outperforms Open3D’s function.
    Once we have our normals per point, we construct a $d_1$x$d_2$x$3$ tensor where $d_1$
    and $d_2$ represent the height and width of our depth matrix, respectively. We
    now consider this tensor as an unconventional RGB image which we pass to OpenCV
    to execute their flood fill algorithm. Per convention of flood fill algorithms,
    we need to set a seed point to begin the flood, and we also need to set a
    termination criteria to stop flooding. For our system, we start our seed
    point at the bottom middle of the depth matrix tensor. The image below should
    clarify our description.
    """)
    image = Image.open(f'{assets_path}/flood_fill_figure.png')
    st.image(image, caption= 'Flood Fill Results', use_column_width=True)

    st.write("""
    Our termination criteria is that from a spot, we
    continue the flood to a neighbor if the neighbor’s normal vector components
    are within +/- 0.01 of the normal vector components associated with the
    given spot. The code snippet below should also clarify our flood fill
    algorithm parameters.
    """)
    image = Image.open(f'{assets_path}/flood_fill_code.png')
    st.image(image, caption= 'Flood Fill Configuration', use_column_width=True)

    st.write("""
    ### Editing the Ground Plane Detection Algorithm for Calculating Roll

    As you can see from the previous photo, our flood fill algorithm accurately
    segments the road from barriers and obstacles, but the downside is that this
    method is slow, especially on edge devices. This matters because the ROAR RC
    car must have efficient algorithms in order to race effectively. Some key
    observations is that we don’t need to compute all the normals that exist
    within our sensed data to get the road normal vector. Therefore, we employ
    some heuristics in order to speed up calculation of the road normal angle and
    thus our roll angle. First of all, we exclude points that belong on the
    horizon, since this is a wasted calculation. At the moment, we hard code the
    row index belonging to the end horizon based on observations of what works
    best. We pick a value of 200, meaning that points below the row index of 200
    in our depth matrix are what we pick during our first filtering phase. Our
    second filtering phase samples 5,000 points from the region we talked about
    previously.  However, this sparse sampling of points breaks the assumption of
    connected components, which is what our flood fill algorithm relies on for
    segmentation. We get around this issue by employing a k-nearest neighbor
    strategy amongst the estimated normals that are computed. Given that our KNN
    algorithm chooses closest neighbors based on the norm of the difference
    between two points, we get 200 normals that are similar to the normal
    associated with our seed point (this is the same seed point that we mentioned
    in the flood fill section). We rely on Open3D’s KDTree implementation to
    efficiently calculate the nearest normals. Finally, we mean the normals to
    get the road normal. With these optimizations, our client processes information
    at 30-40 FPS, instead of 4-8 FPS with the original ground plane detection system.
    """)
    image = Image.open(f'{assets_path}/heuristic_figure.png')
    st.image(image, caption= 'Horizon Limit + Sparse Sampling + KNN',
             use_column_width=True)

    st.write("""
    As a note about implementation details, we also do road normal calculations
    every 5 “time steps”. “Time steps” are defined as the completion of one
    sensing, planning, and actuation loop.
    """)
    image = Image.open(f'{assets_path}/timestep_code.png')
    st.image(image, caption= 'Time Step Code for Limiting Roll Calculations',
             use_column_width=True)

    st.write("""
    Additionally, we verify the computed
    roll by the roll given by the system. In order for our computed roll to
    match closely with the system-given roll in degrees, we need to subtract by
    90 degrees after we convert our angle from radians to degrees. Computation
    of estimated normals/consideration of the wrong camera frame axes could be
    to blame for this weird mathematics.
    """)
    image = Image.open(f'{assets_path}/roll_correction_code.png')
    st.image(image, caption= 'Roll Correction Code for Approximate True Roll',
             use_column_width=True)

    st.write("""
    The latitudinal controller is a hand-tuned, slightly adaptive PID controller.
    The keys represent speed boundaries.
    """)
    image = Image.open(f'{assets_path}/lat_kvals_code.png')
    st.image(image, caption= 'Adaptive K-Values for Latitudinal PID Controller')

    st.write("""
    ### Using the Roll Control and Results

    Now that we have the roll of the car from our depth data, we can use this
    value to output a throttle to our car. Carla expects a value between 0 and
    1, and our driving intuition tells us that we must slow down our car in the
    presence of roll. This is mainly to address proper breaking around curves
    while still maintaining a high enough speed. Based on our criteria for an
    output, we thought that the following function would be a good starting
    approximation:""")
    st.latex(r'''
        f(x) = e^{-w \cdot |\text{roll}|}
    ''')

    st.write("""
    Our results indicated that $w=0.048$ is the best for our waypoint
    and car configuration. Amazingly, though, this roll controller gives us the
    best lap time amongst our racing agents.
    """)
    st.write(pd.DataFrame({
        'weight': [0.048, 0.058, 0.068],
        'Lap Time (Seconds)': [103.274860382, 109.641319513, 116.743569851]
    }))

    st.write("""
    Here is a demo video of ground plane detection and the Roll Controller agent
    in action.
    """)
    st.video("https://www.youtube.com/watch?v=SNIbJFqhKFQ")

    st.write("""
    ### Future Work

    For future work, we would like to:
     - Fix the bugs with the current roll
     - Find more robust and generalizable optimizations for ground plane calculations
     - Use ground plane detection as a medium for placing the next waypoint
     - Explore using the road normal vector and/or roll angle as a feature for an RL agent

    Amongst our system, the roll controller gives us the fastest lap time, so we
    would like to experiment more with this idea of using roll as a factor in
    control.
    """)

    st.header("Design Questions")
    st.subheader(
    	"What design criteria must your project meet? What is the desired functionality?")
    st.write("""
    The design criteria is to smoothly, reliably, and quickly be able to autonomously
    maneuver a vehicle around a given road course. For now, we are concerned with
	simulated racing environments, so our ultimate goal is to achieve the fastest lap
    around the given Carla track while taking into account the previosly mentioned items.
    To this end, it was desired to test a variety of controllers and see which one
    performs best.
    """)

    st.subheader("Describe the design you chose.")
    st.write("""
    Unlike other controllers mentioned in this final project, the Roll controller
    is not one that has been tried and tested. It was an innovation of our group
    to use the roll control as a way to output the throttle. Intuitively, if our
    car has nonzero roll, we would like to slow down to prevent sliding and
    promote smooth motion, especially around curves.
    """)

    st.subheader(
		"What design choices did you make when you formulated your design?\
		What trade-offs did you have to make?")
    st.write("""
    This was discussed in the general description and implementation details
    above. Notable design choices were (1) the edtiting of the ground plane detection
    algorithm for calculating roll and (2) the throttle function for our controller.

    In particular, we edited the ground plane detection algorithm by
    (1) looking in a desired region, (2) sampling points from the region, and (3)
    taking the mean of the normals similar to the seed point normal. This mean
    gives us the road mean vector. In regard to our throttle function, it
    behaves in a way that aligns with our intution, i.e. the output is in the interval
    [0, 1] and throttle is penalized when roll is nonzero.

    In terms of trade-offs, we had to sacrifice the generalizability of the
    flood fill algorithm running at each time step for faster hacks. Technically,
    our system is designed to perform on the track given in Carla, so we might
    have to tune the hard-coded values if given another track.
    """)

    st.subheader(
    	"How do these design choices impact how well the project meets design\
    	criteria that would be encountered in a real engineering application,\
    	such as robustness, durability, and efficiency?")
    st.write("""
    Since the Roll controller is not a tried and tested system, it may not be as
    robust in real-world environments. However, skidding and sliding is a very
    real thing that race cars must deal with, and although our Carla environment
    does not simulate this behavior, we believe that this design choice will
    serve our racing agent well in reliably navigating curves at high speeds due
    to factoring in roll.

    In terms of generalizability amongst racing tracks, our current system is not
    robust, since we hard code timesteps for roll calculations and use KNN to
    gather similar normals instead of using a more strict termination criteria
    (the flood fill algorithm features this). However, we did not have the
    opportunity to try out other tracks to test out our generalizability, so
    we leave this as a future topic to explore.
    """)

    st.header("Implementation Questions")
    st.subheader("Describe any hardware you used or built. Illustrate with pictures and diagrams.")
    st.write("""
    Not applicable.
    """)

    st.subheader("What parts did you use to build your solution?")
    st.write("""
    Not applicable.
    """)

    st.subheader("Describe any software you wrote in detail. Illustrate with diagrams, flow charts, and/or other appropriate visuals. This includes launch files, URDFs, etc.")
    st.write("""
    See general description and implementation above. In general, for each controller,
    functions were written to take inputs and process needed information from
    them.  This information was converted to needed data and sent to the algorithm
    that determined the outputs of the controller.  Other system modifications
    were minor - such as copying an agent and modifying it to call the Roll
    Controller instead of the already existing PID controller, and changing the
    initiating file to call this agent instead of the original.
    """)

    st.subheader("How does your complete system work? Describe each step.")
    st.write("""
    See general description and implementation above.
    """)
