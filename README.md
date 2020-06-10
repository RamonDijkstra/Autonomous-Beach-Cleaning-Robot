# The development of an autonomous robot that detects and removes plastic on beaches.

This github repository contains the files and the results of a bachelor's thesis. The thesis examines the extent to which Artificial Intelligence supports the development of an autonomous robot that detects and removes plastic on beaches.

The AI techniques that are used are path planning, object detection and a knowledge graph.

## The abstract of the research
The abstract of the bachelor thesis is added below. This abstract is added so that the goal of the project is getting more clear.

This paper examines the extent to which Artificial Intelligence supports the development of an autonomous robot that detects and removes plastic on beaches. We initiated this research because plastic pollution is a worldwide problem. Next to oceans and rivers, beaches are polluted with an extensive amount of plastic debris. There is currently no general method to remove all the plastic on beaches. Besides that, humans are not able to manually remove all this plastic. Our idea is to develop an autonomous robot that can detect and remove the plastic on beaches. This research does not focus on the mechanical side of the robot. It examines the extent to which path planning, object detection and a knowledge graph are suitable technologies for the development of an autonomous beach cleaning robot. A simple area coverage path planning algorithm provides the robot with the initial movement. The capabilities of an object detection program called YOLO are explored and it is found that it can detect objects with high precision and in real-time. A knowledge graph is used to represent the beach environment and the actions that need to be taken after an event occurs. The paper concludes that path planning, object detection and a knowledge graph are suitable technologies for the development of an autonomous robot that can detect and remove the plastic on beaches.

## How it works

### Path Planning
The path planning algorithm is not coded. Is is found that a simple area coverage path planning algorithm will do the job. Therefore, we have not implemented it. The visualisation_simple_path_planning.png can be used as a reference of how the Path Planning should look like.

### Object Detection
YOLO object detection from Pjreddie is used.
- https://pjreddie.com/darknet/yolo/ (How to install the files)
- https://github.com/pjreddie/darknet (The files)

To get YOLO working, follow the above links and install the files.

### Knowledge Graph
The create_knowledgegraph.py file in this repository contains the knowledge graph of the autonomous robot.
It saves the Knowledge Graph in the knowledgegraph.ttl file. A visualisation of this knowledge graph can be found in the visualisation_knowledge_graph.png file.

### Get everything together
The detect_and_query_KG.py file in this repository contains the object detection combined with the knowledge graph to infer the actions that need to be taken by the robot.

How to get it working:
- Install YOLO
- Run the create_knowledgegraph.py file
- Choose an image to detect
- Run the detect_and_query_KG.py file

The output contains the actions that need to be taken by the robot.

The visualisation_scenario_full_system.png file contains a visualisation of the whole system.
