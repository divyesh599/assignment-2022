# assignment-2022
Interview purpose...

Task

Find points in polygon.

Given 5000 randomly placed points, find all the points which are within the polygon (India polygon in this case).

https://i.imgur.com/3uRV6Bp.png
Figure: The points only within the India region need to be selected using python.

Details:

Python Packages to be used: Shapely, json, csv

Attached dataset:
1. india_extent_points.csv - contains latitude, longitude of the points. Need to be read as [shapely](https://github.com/shapely/shapely) geometry (each line in the CSV should be considered a Point).
2. india_geojson.geojson - A geojson containing coordinates of India.

Output of the assignment should be a CSV with only the points within the India polygon.
