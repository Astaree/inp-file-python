"""
This script generates an input file for finite element analysis using the data from an input JSON file.
To use this script, provide a valid input JSON file in the same directory as the script, and run it using the following command:
    python script_name.py
The input file should have the following format:
{
    "part_name": "string",
    "nodes_w": "int",
    "nodes_h": "int",
    "width": "float",
    "height": "float"
}
where "part_name" is the name of the part being analyzed, "nodes_w" and "nodes_h" are the number of nodes in the width and height dimensions respectively,
and "width" and "height" are the dimensions of the part being analyzed. The output file will be saved in the same directory as the input JSON file.
"""

import json
from matplotlib.widgets import Button
import numpy as np
from scipy.spatial import Delaunay
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

points = np.array(np.meshgrid(y_coord,x_coord)).T.reshape(-1,2)

tri=Delaunay(points)
plt.triplot(points[:,0], points[:,1],tri.simplices) #krawędzie
plt.plot(points[:,0], points[:,1],'o',color='red')  #pkt

print(tri.simplices)

header = ["*HEADING", f"** {part_name} Analysis\n*Part, name=part-1"]
nodes_list = []
elements = []

nodes_list.append(["*Node"])
for i in range(len(points)):
    nodes_list.append([str(i+1), str(points[i][0]),str(points[i][1])])

elements.append(["*Element, type=S3"])
for i in range(len(tri.simplices)):
    elements.append([str(i+1),str(tri.simplices[i][0]),str(tri.simplices[i][1]),str(tri.simplices[i][2])])

with open(f"{part_name}.inp", "w") as f:
    f.writelines(str(head) + '\n' for head in header)
    f.writelines(str(node).replace('[','').replace(']','').replace('\'','') + '\n' for node in nodes_list)
    f.writelines(str(element).replace('[','').replace(']','').replace('\'','') + '\n' for element in elements)
    
#plt.show()