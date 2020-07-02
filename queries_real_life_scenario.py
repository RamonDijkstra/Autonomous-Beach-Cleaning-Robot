'''
Bachelor Project Information Sciences
This file contains the SPARQL queries of the real-life scenario and the instructions for actions are
given to the mechanical side of an autonomous robot that detects and removes plastic on beaches.
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

#Perform SPARQL query to get infomation about the detected bottle
print("Information detected bottle:")

qres = g.query('''
    SELECT ?o
    WHERE {
    		{ex:bottle ex:action_required ?o .}
    		UNION
    		{ex:bottle ex:has_weight ?o .}
    		UNION
    		{ex:bottle ex:pick_up_ability ?o .}
    	  }
'''
              )

#Print actions that can be given to the mechanical side of the robot

for row in qres:
	o = row[0].split('/')[-1]
	print(o)






#Perform SPARQL query to get infomation about the detected person
print("\n")
print("Information detected person:")

qres2 = g.query('''
    SELECT ?o
    WHERE {
    		{ex:person ex:action_required ?o .}
    		UNION
    		{ex:person ex:has_property ?o .}
    	  }
'''
               )

#Print actions that can be given to the mechanical side of the robot

for row in qres2:
	o = row[0].split('/')[-1]
	print(o)





#Perform SPARQL query to get infomation about the detected full temporary bin
print("\n")
print("Information detected full temporary bin:")

qres3 = g.query('''
    SELECT ?o
    WHERE {
    		{ex:robot ex:temporary_bin_full ?o .}
    		UNION
    		{ex:robot ex:bin_location ?o .}
   		  }
'''
               )

#Print actions that can be given to the mechanical side of the robot

for row in qres3:
	o = row[0].split('/')[-1]
	print(o)





#Perform SPARQL query to get infomation about the detected animal
print("\n")
print("Information detected animal:")

qres4 = g.query('''
    SELECT ?o
    WHERE {
    		{ex:animal ex:action_required ?o .}
    		UNION
    		{ex:animal ex:has_property ?o .}
    	  }
'''
               )

#Print actions that can be given to the mechanical side of the robot

for row in qres4:
	o = row[0].split('/')[-1]
	print(o)