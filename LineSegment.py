
from vec2 import vec2

class LineSegment:
    "A line with a start and an end in 2d space"

    start: vec2
    end: vec2

    def __init__(self, start, end):
        if start == end:
            raise ValueError
        self.start = start
        self.end = end

    @property
    def vector(self):
        return self.end - self.start

    @vector.setter
    def vector(self, vector: vec2):
        self.end = self.start + vector

    def unitVector(self):
        return self.vector.unitVector()

    @property
    def direction(self):
        "Alias for unitVector"
        return self.unitVector()

    @property 
    def length(self):
        return self.vector.length

    @length.setter
    def length(self, length: float):
        self.vector.length = length

    @property
    def angle(self):
        return self.vector.angle

    @angle.setter
    def angle(self, angle):
        self.vector.angle = angle

    def pointAlong(self, lengthAlong) -> vec2:
        if lengthAlong < 0 or lengthAlong > self.length:
            raise ValueError
        else:
            progress = lengthAlong / self.length
            return self.start * (1.0 - progress) + self.end * progress

    def normalAlong(self, lengthAlong):
        start = self.pointAlong(lengthAlong)
        direction = self.direction.normal()
        return LineSegment(start=start, end=start + direction)
        



    # Bounding rectangle methods
    @property
    def top(self):
        return max([self.start.y, self.end.y])

    @property
    def bottom(self): 
        return min([self.start.y, self.end.y])
    
    @property
    def left(self): 
        return min([self.start.x, self.end.x])

    @property
    def right(self):
        return max([self.start.x, self.end.x])

    def __str__(self):
        return "{} -> {}".format(self.start, self.end)

