# Autonomous-Beach-Cleaning-Robot

This github repository contains the files and results for a bachelor thesis. The thesis examines the extent to which several Artificial Intelligence techniques contribute to the development of an autonomous robot that detects and removes plastic on beaches.

YOLO object detection from Pjreddie is used. 
- https://github.com/pjreddie/darknet
- https://pjreddie.com/darknet/yolo/

To get YOLO working, follow the above links.

The create_knowledgegraph.py file in this repository contains the Knowledge Graph of the autonomous robot.
It saves the knowledge graph in the knowledgegraph.ttl file.

The detect_and_query_KG.py file in this repository contains the object detection combined with the knowledge graph to infer action.

How to get it working:
- Install YOLO
- Run the create_knowledgegraph.py file
- Choose a image to detect
- Run the detect_and_query_KG.py file

The output contains the actions that need to be taken by the robot.
