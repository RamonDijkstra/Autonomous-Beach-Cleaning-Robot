'''
Bachelor Project Information Sciences
This file contains the detection of objects with YOLO and a queried knowledge graph to infer actions that
are given to the mechanical side of an autonomous robot that detects and removes plastic on beaches.

Author: Ramon Dijkstra
'''

# Import the right libraries

import rdflib
import os
import json
import operator
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, RDF, RDFS, Namespace, Literal, URIRef
from collections import Counter, OrderedDict


# Load the graph

g = rdflib.Graph()
g.load("knowledgegraph.ttl", format="turtle")


#Perform YOLO object detection
#The image can be inserted on the "bottleishan.jpg" place

os.system('./darknet detect cfg/yolov3.cfg yolov3.weights.1 data/bottleishan.jpg > result.json')

data = open("result.json").read()
lines = data.split('\n')
elements = []
percentages = []
lines.remove(lines[0])
lines.remove(lines[-1])

for i in lines:
	element = i.split(':')[0]
	elements.append(element)

	percentage = int(i.split(':')[1].split('%')[0])
	percentages.append(percentage)

index, value = max(enumerate(percentages), key=operator.itemgetter(1))
target = elements[index]
target = "ex:%s" % target


#Perform SPARQL query to get infomation about the target and the robot itself

robot = "ex:robot"

qres = g.query('''
    SELECT ?s ?p ?o
    WHERE {
    ?s ?p ?o
    VALUES ?s {%s} .
    }
''' %(target)
               )

qres2 = g.query('''
    SELECT ?s ?p ?o
    WHERE {
    ?s ?p ?o
    VALUES ?s {%s} .
    }
''' %(robot)
               )


#Print actions that can be given to the mechanical side of the robot

for row in qres:
	s = row[0].split('/')[-1]
	p = row[1].split('/')[-1]
	o = row[2].split('/')[-1]
	print('%s, %s -> %s' %(s,p,o))

for row in qres2:
	s = row[0].split('/')[-1]
	p = row[1].split('/')[-1]
	o = row[2].split('/')[-1]
	print('%s, %s -> %s' %(s,p,o))
