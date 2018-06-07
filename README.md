# navigation_waypoints_scripts
A ROS script to create waypoints, and make the robot navigate between them


The python scripts are to be used as follows:
- Delete the file.csv, waypointNodes.csv files *This should be automated*
-  nodeSelection_1.py , it required TKinter for python. A file browser requires you to point to your .pgm map file
    - Select the points you want to navigate to
- waypointCreation_2.py, adjust the DENSITY variable, this file creates intermediate points in between the nodes you previously selected.
- navigateToGoals_3.py, this will actually tell the robot to navigate to the waypoints. You can also adjust how much to wait at each waypoint before moving on to the next one.


Make sure the move_base stack in configured properly. Before you are using this script, your robot should be able to accept, and properly navigate to the commanded location from RViz
