# KNOWLEDGE GRAPH IMPLEMENTATION IN PYTHON
# -----------------------------------------
# This program demonstrates a simple Knowledge Graph (KG)
# using Python and NetworkX library.
#
# Concepts:
# - Nodes  -> Entities (Place, Food, Person, etc.)
# - Edges  -> Relationships between entities
#
# Example Domain:
# Travel Recommendation System

import networkx as nx
import matplotlib.pyplot as plt

# Create Directed Graph
KG = nx.DiGraph()

# -----------------------------------------
# ADD ENTITIES (NODES)
# -----------------------------------------

KG.add_node("Goa", type="Tourist Place")
KG.add_node("Beach", type="Attraction")
KG.add_node("Seafood", type="Food")
KG.add_node("Water Sports", type="Activity")
KG.add_node("Tourist", type="Person")

# -----------------------------------------
# ADD RELATIONSHIPS (EDGES)
# -----------------------------------------

KG.add_edge("Goa", "Beach", relation="has")
KG.add_edge("Goa", "Seafood", relation="famous_for")
KG.add_edge("Goa", "Water Sports", relation="offers")
KG.add_edge("Tourist", "Goa", relation="visits")

# -----------------------------------------
# DISPLAY KNOWLEDGE GRAPH DETAILS
# -----------------------------------------

print("===== KNOWLEDGE GRAPH =====\n")

print("Nodes in KG:")
for node, data in KG.nodes(data=True):
    print(node, "->", data)

print("\nRelationships in KG:")
for source, target, data in KG.edges(data=True):
    print(source, "--", data["relation"], "-->", target)

# -----------------------------------------
# VISUALIZE KNOWLEDGE GRAPH
# -----------------------------------------

pos = nx.spring_layout(KG)

nx.draw(
    KG,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True
)

edge_labels = nx.get_edge_attributes(KG, 'relation')

nx.draw_networkx_edge_labels(
    KG,
    pos,
    edge_labels=edge_labels
)

plt.title("Knowledge Graph Example")
plt.show()
