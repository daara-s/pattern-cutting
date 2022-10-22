import drawSvg as svg
from geometry.Shape import Shape
from render import render

demo = svg.Drawing(100, 100)

# Rendering a point with a Shape instance
p = Shape([[50, 50, 0]])
print(p.points.size)
demo.append(p.svg())

# Rendering a single line segment
segment = Shape([50, 75, 0, 25,25,0])
demo.append(segment.svg())

# Rendering a path with interim points
path = Shape([10, 10, 0, 10, 20, 0, 90, 20, 0], close=True)
demo.append(path.svg())

demo.saveSvg("DEMO.svg")


