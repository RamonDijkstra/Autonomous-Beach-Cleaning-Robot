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

The abstract of the bachelor thesis is added below. This abstract is added so that the goal of the project is getting more clear.

This paper examines the extent to which Artificial Intelligence supports the development of an autonomous robot that can detect and remove the plastic on beaches. We initiated this research because plastic pollution is a worldwide problem. Next to oceans and rivers, beaches are polluted with an extensive amount of plastic debris. There is currently no general method to remove all the plastic on beaches. Besides that, humans are not able to manually remove all this plastic. Our idea is to develop an autonomous robot that can detect and remove the plastic on beaches. This research does not focus on the mechanical side of the robot. It examines the extent to which object detection, a knowledge graph, and path planning are suitable technologies for the development of an autonomous beach cleaning robot. The capabilities of an object detection program called YOLO are explored and it is found that it can detect objects with high precision and in real-time. A knowledge graph is used to represent the beach environment and the actions that need to be taken after an event occurs. A simple area coverage path planning algorithm provides the robot with the initial movement. The paper concludes that object detection, a knowledge graph, and path planning are suitable technologies for the development of an autonomous robot that can detect and remove the plastic on beaches.
