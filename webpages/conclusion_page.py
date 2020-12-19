import streamlit as st
import numpy as np
import pandas as pd

def page():
	st.header("Conclusion")
	st.subheader("Discuss your results.")
	st.write(pd.DataFrame({
		"Controller": ['PID', 'RL PID', 'Roll', 'Stanley'],
		"Lap Time (Seconds)": [121.816164255, 119.655861378, 103.274860382, None],
		"Lap Time (Min:Sec)": ['2:01', '1:59', '1:43', None]
	}))
	st.write("""
	By looking at the performance breakdown of our racing agents and their
	controllers, it is clear that the Roll controller produced the fastest
	lap time.

	Interestingly, our RL PID controller and traditionally tuned PID controller
	produced very similar results indicating that our RL PID agent was trained
	incredibly well as it produced a very similar outcome to that of a human
	setting the k values through traditional control methods.

	The Roll controller was the big winner of our racing agents, having an 18.54
	second faster lap time than the traditionally tuned PID controller.
	""")

	st.subheader("How well did your finished solution meet your design criteria?")
	st.write("""
	Out of 7 teams, our project ended up placing 3rd in the ROAR race. We also
	finished with the Reliability Award, being the only team with 0 collisions.
	This absolutely meets our design criteria since we achieved the fastest
	possible lap time without running into barriers or other cars.
	""")

	st.subheader("Did you encounter any particular difficulties?")
	st.write("""
	On the physical car, we are using Vive Tracker for our localization service.
	However, the calibration is a bit unintuitive. For example, the goggles had
	to be placed in a specific direction and the Vive Tracker had to be carefully
	placed on the vehicle or else the pitch of the car would be off. The Vive
	Tracker was also seen as “lost” a few times which caused unrecoverable
	runtime crashes from Steam/OpenVR that required a manual restart of the server.

	On the physical car, in terms of vehicle safety and throttle limits, we ended
	up setting the throttle boundary from (0,1) instead of the traditional (-1,1).
	This is because we ran into issues when the vehicle was going very fast and
	the PID controller instructed the vehicle to go in reverse to slow down
	immediately. Going in reverse is not optimal when trying to go as fast as
	possible. Since our car is only needed to move forward, this was found to be
	fine, however if our vehicle needed to ever move in reverse, this would not
	be a good thing to do.

	There were various times where our physical car hit a barrier during testing
	at a very high speed and damaged the car! To stop this from happening, we
	set a limit on the motor RPM and maximum speed of the vehicle. After testing,
	we slowly increased these values until the desired limit was reached for the
	car to go around the track quickly without flying off the track on the curves.
	""")

	st.subheader("Does your solution have any flaws or hacks?")
	st.write("""
	Although our solution performed very well in the ROAR race, there are some
	flaws with our solution that could be investigated/improved upon. Although
	our Roll controller was our fastest racing agent, with a 18.54 second faster
	lap time than the traditionally tuned PID controller, remarkably enough, the
	Roll controller is not a tried and tested system. It was an innovation of
	our group to use the roll control as a way to output the throttle. This means
	that, on a real track, with sliding and disturbances, the Roll controller could
	not perform as well as our simulation suggests. Additionally, there are some
	hacks for speeding up the roll calculation such as using the horizon,
	sparse sampling, KNN, and execution of calculation at certain time steps. We
	need a more robust algorithm to speed up the calcultions. 
	""")

	st.subheader("What improvements would you make if you had additional time?")
	st.write("""
	If we had more additional time, we would love to bring our simulation to life.
	At the Richmond Field Station, we had the opportunity to test our physical car
	on a flat track with three tight curves. However, if we could test our physical
	car on a new track with more disturbances (e.g. inclines, rain, etc.), we could
	better replicate driving in the real-world and continue fine-tuning our PID k
	values.

	The collection of waypoints that are fed into our physical car could also be
	improved. This is because our waypoints were collected by manually driving the
	car around our created track, introducing significant human error (e.g. we didn’t
	drive exactly straight on a straight path).

	When calculating the next desired position of the car, the lookahead value is very
	important. We set the lookahead value to be relatively small to reduce crashes on
	curves and create a smoother path overall. The lookahead value was also set to be
	constant throughout the car’s race. However, this can cause the car to do some
	unnecessary calculations when, for example driving fast on a straight path. So
	another improvement we could make to reduce lap time is to smartly adjust the
	lookahead based on different track scenarios and velocities.

	Next steps for the Stanley Controller are to implement the proposed solution
	and see if it fixes the problem with the waypoint not updating and causing
	the controller to “stall out”.  The proposed fix is to skip any waypoint that
	has “expired” - eg is behind the vehicle.  The next waypoint in the queue will
	be accessed and this cycle will continuously repeat until a waypoint in front
	of the vehicle is found.

	The RollControll has room for improvement.  A look ahead can be added to
	detect when a turn is coming.  This could be done by taking the rate of
	change of the heading error, and when it is increasing and greater than a
	given rate, the throttle will be lowered proportionally.  When the look-ahead
	heading error is zero or decreasing, acceleration can be resumed according to
	the RollControll algorithm.

	Finally, the various controllers can all be tuned in the gym to maximize
	performance.  They can also be tested in the physical car, to test cross
	platform viability.
	""")
