from rdflib import Graph
g = Graph()
g.parse("iso639-1.skos.rdf")
qres = "SELECT ?lang WHERE { <http://id.loc.gov/vocabulary/iso639-1> <http://www.w3.org/2004/02/skos/core#hasTopConcept> ?lang . }"
lans = g.query(qres)
for lan in lans:
	gtemp = Graph()
	tlan = lan["lang"]
	print tlan
	filename = tlan+".skos.rdf"
	gtemp.parse(filename)
	g = g + gtemp

content = g.serialize(format="turtle")

graph = open("graph.ttl","w")
graph.write(content)
graph.close()
