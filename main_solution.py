import json
import csv
from shapely.geometry import Point, MultiPolygon, Polygon

import geopandas as gpd
import matplotlib.pyplot as plt


with open('india_geojson.geojson', 'r') as json_file:
    data = json.load(json_file)

polys=[]
for item in data['features'][0]["geometry"]['coordinates']:
    polys.append(item[0])


#multipoly=MultiPolygon([[ polys[0], polys[1:] ]])
#del polys

#csv_points=dict()
csv_points=[]

file = open("india_extent_points.csv")
csvreader = csv.reader(file)

header = next(csvreader)

for row in csvreader:
    csv_points.append([ int(row[0]), float(row[1]), float(row[2]) ])
    #csv_points[int(row[0])]=[float(row[1]), float(row[2])]

file.close()
del csvreader



ans=[]
n=len(polys)
for i in range(5000):
    p1=Point(csv_points[i][2], csv_points[i][1])
    for j in range(n):
        if p1.within(Polygon(polys[j])):
            ans.append([csv_points[i][1], csv_points[i][2]])
            break


with open('answer.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
    writer.writerow(header)
    for i in range(len(ans)):
        writer.writerow(ans[i])
