import json
import csv
from shapely.geometry import Point, Polygon


with open('india_geojson.geojson', 'r') as json_file:
    data = json.load(json_file)

# india Polygones
polys=[]
for item in data['features'][0]["geometry"]['coordinates']:
    polys.append(item[0])

# Queries
csv_points=[]
file = open("india_extent_points.csv")
csvreader = csv.reader(file)
header = next(csvreader)

for row in csvreader:
    csv_points.append([ int(row[0]), float(row[1]), float(row[2]) ])

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


with open('answer.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(ans)):
        writer.writerow([i+1, ans[i][0], ans[i][1]])
