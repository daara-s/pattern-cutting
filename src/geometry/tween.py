from layout import side_by_side
from src.geometry.Group import Group
from src.geometry.Shape import Shape
import numpy as np

def tween(a: Shape, b: Shape, phase: float, resolution = 1.0) -> Shape:
    larger_length = max(a.length, b.length)

    shape = Shape()
    for w in np.arange(0, 1, resolution / larger_length):
        p = a.pointAlong(w * a.length)
        q = b.pointAlong(w * b.length)
        r = p + (q-p) * phase
        shape.line_to(r)
    return shape

def tween_demo(a: Shape, b:Shape):
    step = .2
    shapes = []
    shapes.append(a.with_label("A").with_style("arrow"))
    for phase in np.arange(step, 1.0-step, step):
       shapes.append(tween(a, b, phase).with_label("phase = {}".format(phase)).with_style("arrow"))

    shapes.append(b.with_label("B").with_style("arrow"))

    return Group(*side_by_side(*shapes))

