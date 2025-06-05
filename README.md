# ROS2 Humble
ROS2 Humble - Arduino Mega 2560.<br />
## Installation<br /> 
- `mkdir -p ~/test_ws/src`<br />
- `cd test_ws`<br />
- `colcon build --symlink-install`<br />
- `cd src`<br />
- `ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub`<br />
- `source install/setup.bash`<br />
- `sudo chmod a+rw /dev/ttyACM0`<br />
- `ros2 run py_pubsub talker`<br />
## Structure<br /> 
- beschreibung<br />
- include<br />
- konfig<br />
- launch<br />
- src<br />
- welten<br />
- CMakeLists.txt<br />
- package.xml<br />
