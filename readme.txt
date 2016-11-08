//commands to run drunk_turtle:

cd catkin_ws
source devel/setup.bash

//to produce a random stumbling motion, enter:
roslaunch drunk_turtle stumble.launch

//OR

//to produce a swaying stumble, enter:
roslaunch drunk_turtle stumble.launch swag:=sway


//to monitor turtle's position, open a new terminal window and type:

cd catkin_ws
rostopic echo turtle1/pose
