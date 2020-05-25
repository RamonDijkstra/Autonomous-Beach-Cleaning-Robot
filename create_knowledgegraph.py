'''
Bachelor Project Information Sciences Knowledge Graph in RDFLib
This file contains the knowledge graph of an autonomous plastic identification and removal beach robot.
'''

# Import the right libraries

import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, RDF, RDFS, Namespace, Literal, URIRef
from collections import Counter, OrderedDict

# Create the graph and insert existing knowledge graphs

g = rdflib.Graph()

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
dbo = Namespace('http://dbpedia.org/ontology/')
geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
EX = Namespace('http://example.com/bachelor_project/')
xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

g.bind('geo', geo)
g.bind('ex', EX)
g.bind('xsd', xsd)

def shorten(uri):
    if type(uri) == Literal:
        return '"%s"' % (uri)

    components = g.namespace_manager.compute_qname(uri)
    return "%s" % (components[2])


def inference():
    for s, p, o in g:
        first_element = shorten(s)
        second_element = shorten(p)
        third_element = shorten(o)

        subject = s
        predicate = p
        objec = o

        for s, p, o in g:
            if (first_element == shorten(p) and second_element == "domain"):
                g.add((s, rdf.type, objec))
            if (first_element == shorten(p) and second_element == "range"):
                g.add((o, rdf.type, objec))
            if (third_element == shorten(s) and second_element == "subPropertyOf" and shorten(p) == "subPropertyOf"):
                g.add((subject, rdfs.subPropertyOf, o))
            if (first_element == shorten(p) and second_element == "subPropertyOf"):
                g.add((s, objec, o))
            if (first_element == shorten(o) and second_element == "subClassOf" and shorten(p) == "type"):
                g.add((s, rdf.type, objec))
            if (third_element == shorten(s) and second_element == "subClassOf" and shorten(p) == "subClassOf"):
                g.add((subject, rdfs.subClassOf, o))


# Add the main tuples for the knowledge graph

g.add((EX.dynamic_object, RDFS.subClassOf, EX.object))
g.add((EX.static_object, RDFS.subClassOf, EX.object))

g.add((EX.person, RDFS.subClassOf, EX.dynamic_object))
g.add((EX.animal, RDFS.subClassOf, EX.dynamic_object))
g.add((EX.car, RDFS.subClassOf, EX.dynamic_object))
g.add((EX.ball, RDFS.subClassOf, EX.dynamic_object))

g.add((EX.plastic_object, RDFS.subClassOf, EX.static_object))
g.add((EX.pole, RDFS.subClassOf, EX.static_object))
g.add((EX.towel, RDFS.subClassOf, EX.static_object))
g.add((EX.windscreen, RDFS.subClassOf, EX.static_object))
g.add((EX.chair, RDFS.subClassOf, EX.static_object))
g.add((EX.sunbed, RDFS.subClassOf, EX.static_object))
g.add((EX.tree, RDFS.subClassOf, EX.static_object))
g.add((EX.boat, RDFS.subClassOf, EX.static_object))
g.add((EX.inflatables, RDFS.subClassOf, EX.static_object))
g.add((EX.umbrella, RDFS.subClassOf, EX.static_object))

# Add the general properties of the main tuples

# Person
g.add((EX.person, EX.has_property, EX.dynamic))
g.add((EX.person, EX.has_property, EX.can_walk))
g.add((EX.person, EX.has_property, EX.can_move))

# Animal
g.add((EX.animal, EX.has_property, EX.dynamic))
g.add((EX.animal, EX.has_property, EX.can_walk))
g.add((EX.animal, EX.has_property, EX.can_move))

# Car
g.add((EX.car, EX.has_property, EX.dynamic))
g.add((EX.car, EX.has_property, EX.can_move))

# Ball
g.add((EX.ball, EX.has_property, EX.dynamic))
g.add((EX.ball, EX.has_property, EX.can_move))
g.add((EX.ball, RDFS.subClassOf, EX.plastic_object))

# Plastic
g.add((EX.bottle, RDFS.subClassOf, EX.plastic_object))
g.add((EX.bottle, EX.has_weight, EX.low))
g.add((EX.plastic_sack, RDFS.subClassOf, EX.plastic_object))
g.add((EX.plastic_bag, RDFS.subClassOf, EX.plastic_object))

# Towel
g.add((EX.towel, EX.has_position, EX.on_the_ground))

# Windscreen
g.add((EX.windscreen, EX.has_position, EX.on_the_ground))

# Chair
g.add((EX.chair, EX.has_position, EX.on_the_ground))

# Sunbed
g.add((EX.windscreen, EX.has_position, EX.on_the_ground))

# Tree
g.add((EX.tree, EX.has_property, EX.leaves))

# Boat
g.add((EX.boat, EX.has_position, EX.on_the_ground))

# Inflatables
g.add((EX.inflatables, RDFS.subClassOf, EX.plastic_object))
g.add((EX.inflatables, EX.contains, EX.air))

# Umbrella
g.add((EX.umbrella, EX.has_position, EX.on_the_ground))

# Add properties about pick up


# Person
g.add((EX.person, EX.action_required, EX.move_around))

# Animal
g.add((EX.animal, EX.action_required, EX.move_around))

# Car
g.add((EX.car, EX.action_required, EX.move_around))

# Ball
g.add((EX.ball, EX.action_required, EX.move_around))

# Plastic
g.add((EX.bottle, EX.action_required, EX.pick_up))
g.add((EX.plastic_sack, EX.action_required, EX.pick_up))
g.add((EX.plastic_bag, EX.action_required, EX.pick_up))

# Towel
g.add((EX.towel, EX.action_required, EX.move_around))

# Windscreen
g.add((EX.windscreen, EX.action_required, EX.move_around))

# Chair
g.add((EX.chair, EX.action_required, EX.move_around))

# Sunbed
g.add((EX.windscreen, EX.action_required, EX.move_around))

# Tree
g.add((EX.tree, EX.action_required, EX.move_around))

# Boat
g.add((EX.boat, EX.action_required, EX.move_around))

# Inflatables
g.add((EX.inflatables, EX.action_required, EX.move_around))

# Umbrella
g.add((EX.umbrella, EX.action_required, EX.move_around))

# How can it be picked up?

# Plastic
g.add((EX.bottle, EX.pick_up_ability, EX.one_arm))
g.add((EX.plastic_sack, EX.pick_up_ability, EX.two_arms))
g.add((EX.plastic_bag, EX.pick_up_ability, EX.one_arm))


# Information about the robot itself
g.add((EX.robot, RDFS.subClassOf, EX.object))
g.add((EX.robot, geo.lat, Literal("-8.659589")))
g.add((EX.robot, geo.long, Literal("115.130358")))
g.add((EX.robot, EX.bin_location, Literal("-8.659522, 115.130313")))
g.add((EX.robot, EX.saved_location, Literal("-8.659655, 115.130383")))


inference()
g.serialize(destination='knowledgegraph.ttl', format='turtle')