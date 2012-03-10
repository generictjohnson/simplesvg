import collections

from base import SVGBase
from circle import Circle
from ellipse import Ellipse
from line import Line
from path import Path
from polygon import Polygon
from polyline import Polyline
from rect import Rect

class Group(SVGBase):
    '''A group of SVG elements.'''

    TEMPLATE = '''\
<g {meta}>
{children}
</g>'''

    def __init__(self, **kwargs):
        '''Create the group.

        @param kwargs: keyword parameters
            additional metadata'''

        super(Group, self).__init__(**kwargs)

        self.children = list()

    def transform(self, *args):
        '''Create an empty transform group according to the transformations in
        args. Add the group to the DOM and return a reference to it.

        @param args: positional arguments
            the transformations to apply, specified as (type, values) pairs, 
            where type is one of "matrix" "translate" "scale" "rotate" "skewX"
            or "skeyY"'''

        transform = list()
        for transform_type, value in args:
            if isinstance(value, collections.Sequence):
                value = ','.join(str(v) for v in value)

            transform.append('{}({})'.format(transform_type, value))
        transform = ', '.join(transform)

        group = Group(transform=transform)
        self.children.append(group)
        return group

    def path(self, *args, **kwargs):
        '''Create a path, add it to this group and return a reference to it. 
        All arguments are passed to the path's constructor.

        @param args: positional arguments
            the positional arguments to pass to the path's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the path's constructor'''

        path = Path(*args, **kwargs)
        self.children.append(path)
        return path

    def rect(self, *args, **kwargs):
        '''Create a rect, add it to this group and return a reference to it.
        All arguments are passed to the path's constructor.

        @param args: positional arguments
            the positional arguments to pass to the rect's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the rect's constructor'''

        rect = Rect(*args, **kwargs)
        self.children.append(rect)
        return rect

    def circle(self, *args, **kwargs):
        '''Create a circle, add it to this group and return a reference to it. 
        All arguments are passed to the circle's constructor.

        @param args: positional arguments
            the positional arguments to pass to the circle's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the circle's constructor'''

        circle = Circle(*args, **kwargs)
        self.children.append(circle)
        return circle

    def ellipse(self, *args, **kwargs):
        '''Create a ellipse, add it to this group and return a reference to it. 
        All arguments are passed to the circle's constructor.

        @param args: positional arguments
            the positional arguments to pass to the circle's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the circle's constructor'''

        ellipse = Ellipse(*args, **kwargs)
        self.children.append(ellipse)
        return ellipse

    def line(self, *args, **kwargs):
        '''Create a line, add it to this group and return a reference to it. 
        All arguments are passed to the line's constructor.

        @param args: positional arguments
            the positional arguments to pass to the line's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the line's constructor'''

        line = Line(*args, **kwargs)
        self.children.append(line)
        return line

    def polyline(self, *args, **kwargs):
        '''Create a polyline, add it to this group and return a reference to 
        it. All arguments are passed to the polyline's constructor.

        @param args: positional arguments
            the positional arguments to pass to the polyline's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the polyline's constructor'''

        polyline = Polyline(*args, **kwargs)
        self.children.append(polyline)
        return polyline

    def polygon(self, *args, **kwargs):
        '''Create a polygon, add it to this group and return a reference to it. 
        All arguments are passed to the polygon's constructor.

        @param args: positional arguments
            the positional arguments to pass to the polygon's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the polygon's constructor'''

        polygon = Polygon(*args, **kwargs)
        self.children.append(polygon)
        return polygon

    def render(self):
        '''Generate the XML for this canvas and all of its elements.'''

        children = '\n'.join(e.render() for e in self.children)

        return self.TEMPLATE.format(children=children,
                                    meta=self.meta())

