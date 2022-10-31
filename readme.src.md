# Pattern cutting

This is a python library for pattern cutting.

This readme can be converted into a Jupyter notebook and ran using the `run.sh` script.


## `vec2` class

A class for 2d cartesian coordinates. Its used for point coordinates and also for 2d vectors

```code
from geometry.vec2 import vec2

origin = vec2(0,0)
origin.label = "Origin"

```

You can use the render function to generate an SVG representation of the geometry

```code
from render import render
render(origin)
```

## PolyLine

A `PolyLine` object is defined by multiple points which are joined by line segemnts to create a complicated line or shape.

```code
from geometry.PolyLine import PolyLine

square = PolyLine([vec2(0, 0), vec2(100, 0), vec2(100, 100), vec2(0, 100), vec2(0, 0)])

render(square)
```

Using the `style` property, a polyline can be rendered as many different kinds of shapes.

```code
from layout import topToBottom

shape = PolyLine([vec2(0, 0), vec2(100, 50), vec2(200, -50), vec2(300, 0)])

render(
  *topToBottom(
    shape.with_style("line").with_label("line"),
    shape.with_style("dashed").with_label("dashed"),
    shape.with_style("pointset").with_label("pointset"),
    shape.with_style("tape").with_label("tape")
  )
)
```

You can draw measurement markers along a polyline:

```code
render(
  square, 
  *square.evenlySpacedMeasurements()
)
```

Or automatically detect corners:
```code
corners = square.corners()
for corner in corners:
  corner.label = "Here is a corner!"

render(
  square,
  *corners
)
```

You can slice out a certain portion of a line:
```code

render(
  square.slice(25, 175)
)
```

The circle class can be used to generate regular polygons with so many sides they look like a circle:

```code
from geometry.Circle import Circle

circle = Circle(vec2(0, 0), 100)
triangle = circle.polyline(3)
hexagon = circle.polyline(6)
almostCircle = circle.polyline(50)

from layout import sideBySide
render(*sideBySide(triangle, hexagon, almostCircle))
```

We can put this together to get good approximations of measurements along a curve:
```code
arc = circle.polyline(100).slice(0, 150)
render(
  arc,
  *arc.evenlySpacedMeasurements()
  )
```

## Finding the closest point on a polyline
We can find the closest point on a polyline to any given coordinate:
```code
shape = arc
X = vec2(90, 100)
X.label = "X"
Y = shape.closestPoint(X)
Y.label = "Y"
render(
  shape,
  X,
  Y
)
```

You can use closest points in other methods too, such as `slice`

```code
shape = arc
P = vec2(90, 100)
P.label = "P"
Q = vec2(100, 0)
Q.label = "Q"
sliced = shape.slice(P, Q).moveRight(150)
sliced.label = "sliced"
render(P, Q, shape, sliced, *sliced.points)
```


## Die Lemma dress block

One of the main applications of this library is to create outfits for East London drag queen [Die Lemma](https://www.instagram.com/die.lemma/).

A dress block for Die was created and digitised into this library:

```code
from DieLemmaDressBlock import DieLemmaDressBlock

render(DieLemmaDressBlock)
```

Drawing parallels to a complex polyline:

```code
render(
  DieLemmaDressBlock,
  DieLemmaDressBlock.parallel(50)
)
```

or drawing inside the shape instead of outside,

```code
render(
  DieLemmaDressBlock,
  DieLemmaDressBlock.parallel(-25)
)
```

## Winnifred Owen pattern blocks

### Trouser block

```code
from TheClassicTailoredTrouserBlock import TheClassicTailoredTrouserBlock

render(TheClassicTailoredTrouserBlock())
```
