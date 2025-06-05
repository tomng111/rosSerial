# ROS2 Humble
This is a fork of the original code from <ins>docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html</ins>, with some changes.<br />
The main idea starting from the famous rosserial-ROS1 (<ins>wiki.ros.org/rosserial</ins>), which I love and the subscriber part of the Humble tutorial.<br />
An Arduino Mega board is used as the hardware where the blinking LED is actually happening.<br /><br />
ROS2 Humble - Arduino Mega 2560.<br />
## Essential commands<br />
### Project
- `ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub`<br />
- `source install/setup.bash`<br />
- `ros2 run py_pubsub seriel`<br />
### Arduino
- `sudo chmod a+rw /dev/<your_port>`<br />
## Notes from the Tutorial<br /> 
### package.xml
After the lines above, add the following dependencies corresponding to your node’s import statements:<br />
- `<exec_depend>rclpy</exec_depend>`<br />
- `<exec_depend>std_msgs</exec_depend>`<br />
### setup.cfg
The contents of the setup.cfg file should be correctly populated automatically, like so:<br />
- `[develop]`<br />
- `script_dir=$base/lib/py_pubsub`<br />
- `[install]`<br />
- `install_scripts=$base/lib/py_pubsub`<br />
