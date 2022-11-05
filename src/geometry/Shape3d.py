from src.geometry.Vector import Vector
from src.geometry.Shape import Shape

class Shape3d:

    def __init__(self, points):
        self.points = points

    def isometric(self):
        points = [Vector(x = point.x + point.z * .5, y = point.y + point.z * .5) for point in self.points]
        return Shape(points)
