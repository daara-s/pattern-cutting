import drawSvg as draw
import numpy as np

from vec2 import vec2
from LineSegment import LineSegment
from Intersection import Intersection

class PolyLine:
    "As opposed to a monogamous line. This represents a shape made by many line segments joined end to end."
    points: list[vec2]

    # Constrction
    def __init__(self, points = []):
        self.points = points

    def append(self, p):
        self.points.append(vec2(p.x, p.y))


    def close(self):
        self.append(self.start())

    # Iteration
    def segments(self):
        "Iterate line segments"
        for start, end in zip(self.points, self.points[1:]):
            yield LineSegment(start, end)

    def segment(self, index):
        return LineSegment(
            start = self.points[index],
            end = self.points[index+1]
        )

    def intersections(self):
        for start,meeting,end in zip(self.points, self.points[1:], self.points[2:]):
            yield Intersection(start,meeting,end)

    def angles(self):
        "Iterate all the three point angles"
        return [intersection.angle for intersection in self.intersections()]

    @property
    def length(self):
        "Measure the total length of the poly line"
        sum = 0.0
        for segment in self.segments():
            sum += segment.length
        return sum


    # TODO: Probably doesnt make sense for this to be a subclass any more
    class MeasurementAlongPolyLine:
        def __init__(self, parent, lengthAlong: float, index, remainder):
            self.parent = parent
            self.index = index
            self.remainder = remainder
            self.lengthAlong = lengthAlong

        @property
        def segment(self) ->  LineSegment:
            return self.parent.segment( self.index )

        @property
        def point(self):
            return self.segment.pointAlong(self.remainder);

        def normal(self):
            "Unit vector line segment perpendicular to the parent at this point"
            return self.segment.normalAlong(self.remainder)

        def svg(self):
            marker = self.normal().withLength(-3)
            textPath = marker.withLength(100).translate(marker.vector.withLength(marker.length + 1))
            label = draw.Text("{:.0f}mm".format(self.lengthAlong), 5, stroke='none', fill="#000000", path = textPath.svg())
            group = draw.Group()
            group.append(marker.svg())
            group.append(label)
            return group

        # TODO: Use a boundingRect() method instead
        @property
        def top(self): 
            return self.point.y
        @property
        def bottom(self): 
            return self.point.y
        @property
        def left(self): 
            return self.point.x
        @property
        def right(self): 
            return self.point.x

    def measureAlong(self, w):
        sum = 0
        i = 0
        for segment in self.segments():
            if sum + segment.length < w:
                sum += segment.length
            else:
                return self.MeasurementAlongPolyLine(self, w, i, w - sum)
            i += 1
        # otherwise
        raise ValueError

    def pointAlong(self, w) -> vec2:
        "Find a point a certain distance along the polyline"
        return self.measureAlong(w).point

    def evenlySpacedMeasurements(self, step = 10):
        return [self.measureAlong(w) for w in np.arange(0, self.length, step)]

    def upsample(self):
        "Interpolate between the points to create a new poly line with greater resolution"
        # TODO

    def resample(self):
        "Increase the resolution of the line, but no gaurantee for keeping the original points"
        # TODO

    def proximity(self, p):
        "How close is point, p, from the poly line"
        # TODO

    def tangent(self, w):
        "Get the tangent to the poly line at w millimeters along."
        measurement = self.measureAlong(w)
        point = measurement.point
        direction = measurement.segment.unitVector()
        return LineSegment(point, point + direction)

    def findCorners(self, threshholdAngle):
        "Find sharp corners in the line"
        # TODO

    @property
    def top(self) -> float:
        "y coordinate of the topmost point"
        return max([point.y for point in self.points])

    @property
    def bottom(self) -> float:
        "y coordinate of the bottom-most point"
        return min([point.y for point in self.points])

    @property
    def left(self) -> float:
        "x coordinate of the left-most point"
        return min([point.x for point in self.points])

    @property
    def right(self) -> float:
        "x coordinate of the right-most point"
        return max([point.x for point in self.points])

    def start(self) -> vec2:
        return self.points[0]

    def end(self) -> vec2:
        return self.points[-1]


    # Exporting
    def interleavedCoordinates(self):
        for point in self.points:
            yield point.x
            yield point.y

    def svg(self):
        "drawSvg object representation"
        return draw.Lines(*self.interleavedCoordinates(), close=False);

    def __str__(self):
        points = ["{}".format(point) for point in self.points]
        return " -> ".join(points)

    def translate(self, t):
        return PolyLine([point + t for point in self.points])

    def slice(self, start, end):
        startMeasurement = self.measureAlong(start)
        endMeasurement = self.measureAlong(end)
        middlePoints = self.points[startMeasurement.index + 1 : endMeasurement.index + 1]
        return PolyLine([startMeasurement.point, *middlePoints, endMeasurement.point])




if __name__ == "__main__":
    square = PolyLine([vec2(1,1), vec2(1,100), vec2(100,100), vec2(100,1), vec2(0,0)])
    d = draw.Drawing(1000, 1000, origin='center',  stroke='black', fill='none')

    d.append(square.svg())
    d.saveSvg("example.svg")

    up = vec2(0, 1)
    print(up.angle)
    left = vec2(1,0)
    print(left.angle)
