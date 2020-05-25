'''
Bachelor Project Information Sciences Knowledge Graph in RDFLib
This file contains the object detection programme YOLO connected to the Knowledge Graph of the autonomous robot to infer the actions
that need to be taken.
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


#Perform query
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
