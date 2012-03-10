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

    TAG = 'g'

    def __init__(self, **kwargs):
        '''Create the group.

        @param kwargs: keyword parameters
            additional metadata'''

        kwargs['load_defaults'] = False
        super(Group, self).__init__(**kwargs)

    def group(self, *args, **kwargs):
        '''Create a subgroup, add it to this group and return a reference to
        it. All arguments are passed to the group's constructor.

        @param args: positional arguments
            the positional arguments to pass to the group's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the group's constructor'''

        group = Group(*args, **kwargs)
        self.add_child(group)
        return group

    def path(self, *args, **kwargs):
        '''Create a path, add it to this group and return a reference to it. 
        All arguments are passed to the path's constructor.

        @param args: positional arguments
            the positional arguments to pass to the path's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the path's constructor'''

        path = Path(*args, **kwargs)
        self.add_child(path)
        return path

    def rect(self, *args, **kwargs):
        '''Create a rect, add it to this group and return a reference to it.
        All arguments are passed to the path's constructor.

        @param args: positional arguments
            the positional arguments to pass to the rect's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the rect's constructor'''

        rect = Rect(*args, **kwargs)
        self.add_child(rect)
        return rect

    def circle(self, *args, **kwargs):
        '''Create a circle, add it to this group and return a reference to it. 
        All arguments are passed to the circle's constructor.

        @param args: positional arguments
            the positional arguments to pass to the circle's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the circle's constructor'''

        circle = Circle(*args, **kwargs)
        self.add_child(circle)
        return circle

    def ellipse(self, *args, **kwargs):
        '''Create a ellipse, add it to this group and return a reference to it. 
        All arguments are passed to the circle's constructor.

        @param args: positional arguments
            the positional arguments to pass to the circle's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the circle's constructor'''

        ellipse = Ellipse(*args, **kwargs)
        self.add_child(ellipse)
        return ellipse

    def line(self, *args, **kwargs):
        '''Create a line, add it to this group and return a reference to it. 
        All arguments are passed to the line's constructor.

        @param args: positional arguments
            the positional arguments to pass to the line's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the line's constructor'''

        line = Line(*args, **kwargs)
        self.add_child(line)
        return line

    def polyline(self, *args, **kwargs):
        '''Create a polyline, add it to this group and return a reference to 
        it. All arguments are passed to the polyline's constructor.

        @param args: positional arguments
            the positional arguments to pass to the polyline's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the polyline's constructor'''

        polyline = Polyline(*args, **kwargs)
        self.add_child(polyline)
        return polyline

    def polygon(self, *args, **kwargs):
        '''Create a polygon, add it to this group and return a reference to it. 
        All arguments are passed to the polygon's constructor.

        @param args: positional arguments
            the positional arguments to pass to the polygon's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the polygon's constructor'''

        polygon = Polygon(*args, **kwargs)
        self.add_child(polygon)
        return polygon

