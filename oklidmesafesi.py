import math
#Noktaları tanımlayalım.

points = [(0, 0),(4, 6),(-3,-5),(2,3), (-2,4), (9, 16)]

#Öklid Mesafesi için fonksiyon yazalım.

def euclideanDistance(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

#Mesafeleri hesaplayalım.Bunun için  distances adında bir list oluşturalım.

distances=[]
for i in range(len(points)):
     for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

#Minimum mesafeyi bulalım.

minimum_distance=min(distances)
print("Minimum mesafe:",minimum_distance)
