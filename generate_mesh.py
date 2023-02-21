# Instructions:
# This script takes input from an input.json file and generates a mesh.inp file based on the data provided. 
# The mesh.inp file contains information about nodes and elements to be used in a finite element analysis.

# Usage:
# 1. Create an input.json file with the following keys:
#    - part_name: Name of the part being analyzed.
#    - width: Width of the part.
#    - height: Height of the part.
#    - nodes: Number of nodes to be used in the finite element analysis.
# 2. Replace the input.json filename in line 5 with your own input file name.
# 3. Replace the mesh.inp filename in line 26 with your desired output file name.
# 4. Run the script and a mesh.inp file will be generated in the same directory.
#    The mesh.inp file will contain information about the nodes and elements to be used in a finite element analysis.
#    Note that this script assumes a certain type of element (B21) is being used, which may need to be modified based on your specific needs.
#    Also note that the node and element information is being written to the mesh.inp file using comma-separated values.
#    If you need a different format, you may need to modify the script accordingly.

import csv
import json

with open("input.json", "r") as f:
    data = json.load(f)

part_name = data["part_name"]
width = data["width"]
height = data["height"]
nodes = data["nodes"]

# Define x_coord and y_coord lists
x_coord = [i * width / (nodes - 1) for i in range(nodes)]
y_coord = [0] * nodes

header = ["*HEADING", f"{part_name} Analysis"]
nodes_list = []
for i in range(nodes):
    nodes_list.append(["*NODE", str(i + 1), str(x_coord[i]), str(y_coord[i])])

elements = []

# Create elements
for i in range(nodes - 1):
    elements.append(["*ELEMENT, TYPE=B21", str(i + 1) + "," + str(i + 2)])

with open("mesh.inp", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(header)
    writer.writerows(nodes_list)
    writer.writerows(elements)
