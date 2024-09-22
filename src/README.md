**BUCK- AUTONOMOUS MOBILE ROBOT FOR DEPTH-CAM AND 2D LIDAR MAPPING ,NAVIGATION**

OS: UBUNTU 22.04

ROS DISTRO: HUMBLE

Humble installation link::https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html


            
Packages needed:
        
        sudo apt install ros-humble-xacro
        sudo apt install python3-colcon-common-extensions
        sudo apt install ros-humble-joint-state-publisher-gui
        sudo apt install ros-humble-gazebo-ros-pkgs
        sudo apt install ros-humble-rtabmap-*

Clone this repo in your ros2 work directory using,

            git clone https://github.com/Nikhilesh-003/buck_ws.git
Then build the package in your workspace ,

            colcon build --symlink-install

ROBOT with 2 depth camera LAUNCHING COMMAND:

In terminal 1:

    ros2 launch model_py launch_sim.launch.py                        



RTABMAP:

  .**RTAB-Map (Real-Time Appearance-Based Mapping)** is a powerful ROS package designed for real-time _3D environment mapping and localization_. Specifically tailored for depth cameras and 2D lidar mapping, RTAB-Map integrates sensory data to create detailed, dynamic maps
  .It utilizes visual features for loop closure detection, improving map consistency over time. This package is crucial for autonomous systems, providing a comprehensive solution for mapping, navigation, and localization in various environments.



In one terminal 2:
            
            ros2 launch model_py twodepth.launch.py

In terminal 3 :

Teleoperation: Teleoperation allows users to remotely control the Buck autonomous mobile robot equipped with 2 depth cameras, enabling seamless navigation and interaction within its environment using the teleop_twist_keyboard package in ROS2.

            ros2 run teleop_twist_keyboard teleop_twist_keyboard 




            
