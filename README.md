# ROS2 Humble
ROS2 Humble - Arduino Mega 2560.<br />
## Essential commands<br />
### Project
- `ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub`<br />
- `source install/setup.bash`<br />
- `ros2 run py_pubsub seriel`<br />
### Arduino
- `sudo chmod a+rw /dev/<your_port>`<br />
## Structure<br /> 
- py_pubsub<br />
  - __init__.py
  - subscriber_member_function.py
- resource<br />
  - py_subhub
- test<br />
  - test_copyright.py
  - test_flake8.py
  - test_pep257.py
- LICENSE<br />
- package.xml<br />
- setup.cfg<br />
- setup.py<br />
