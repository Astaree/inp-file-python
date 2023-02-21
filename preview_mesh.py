# Instructions:
# This script takes input from an input.json file and generates a mesh.inp file based on the data provided. 
# The mesh.inp file contains information about nodes and elements to be used in a finite element analysis.

# Usage:
# 1. Create an input.json file with the following keys:
#    - part_name: Name of the part being analyzed.
#    - width: Width of the part.
#    - height: Height of the part.
#    - nodes_h, nodes_w: Number of nodes horisontaly and verticly to be used in the finite element analysis.
# 2. Replace the input.json filename in line 5 with your own input file name.
# 3. Replace the mesh.inp filename in line 26 with your desired output file name.
# 4. Run the script and a mesh.inp file will be generated in the same directory.
#    The mesh.inp file will contain information about the nodes and elements to be used in a finite element analysis.
#    Note that this script assumes a certain type of element (B21) is being used, which may need to be modified based on your specific needs.
#    Also note that the node and element information is being written to the mesh.inp file using comma-separated values.
#    If you need a different format, you may need to modify the script accordingly.

import json
import matplotlib.pyplot as plt

with open("./input.json", "r") as f:
    data = json.load(f)

part_name = data["part_name"]
nodes_w = data["nodes_w"]
nodes_h = data["nodes_h"]
width = data["width"]
height = data["height"]

x_coord = [i * width / (nodes_w - 1) for i in range(nodes_w)]
y_coord = [i * height / (nodes_h - 1) for i in range(nodes_h)]

fig, ax = plt.subplots()

#ax.scatter(x_coord, y_coord, s=5)

# Create connections between nodes
for i in range(nodes_w):
    for j in range(nodes_h):
        ax.scatter(x_coord[i-1], y_coord[j-1],s=10)
        ax.plot([x_coord[i-1], x_coord[i]], [y_coord[j-1], y_coord[j-1]], 'k-')
        ax.plot([x_coord[i], x_coord[i]], [y_coord[j-1], y_coord[j]], 'k-')
        if i==0 or j ==0:continue
        ax.plot([x_coord[i-1], x_coord[i]], [y_coord[j-1], y_coord[j]], 'k-')
    

plt.show()

header = ["*HEADING", f"{part_name} Analysis"]
nodes_list = []
elements = []

nodes_list.append(["*NODE"])
for i in range(nodes_w):
    for j in range(nodes_h):
        counter = 1
        nodes_list.append([str(counter), str(x_coord[i]), str(y_coord[j])])
        counter+=1

elements.append(["*ELEMENT, TYPE=B21"])
for i in range(nodes_w):
    for j in range(nodes_h):
        counter = 1
        elements.append([str(counter),str(counter)])

print(nodes_list)
print(elements)