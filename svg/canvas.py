from base import SVGBase
from circle import Circle
from ellipse import Ellipse
from line import Line
from path import Path
from polygon import Polygon
from polyline import Polyline
from rect import Rect

class Canvas(SVGBase):
    '''The container for all SVG elements.'''

    TEMPLATE = '''\
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:link="http://www.w3.org/1999"
     width="{width:d}pt"
     height="{height:d}pt"
     viewbox="0 0 {width:d} {height:d}"
     version="1.1" {meta}>
    {content}
 </svg>'''

    def __init__(self, width, height, meta=None, **kwargs):
        '''Create the canvas.

        @param width: int
            the width of the canvas in units of "pt"
        @param height: int
            the height of the canvas in units of "pt"
        @param meta: optional, dict
            the dictionary of metadata for the canvas
        @param kwargs: keyword parameters
            additional metadata'''

        super(Canvas, self).__init__(meta=meta, **kwargs)
        self.width = width
        self.height = height

        self.elements = list()

    def path(self, *args, **kwargs):
        '''Create a path, add it to the DOM and return a reference to it. All
        arguments are passed to the path's constructor.

        @param args: positional arguments
            the positional arguments to pass to the path's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the path's constructor'''

        path = Path(*args, **kwargs)
        self.elements.append(path)
        return path

    def rect(self, *args, **kwargs):
        '''Create a rect, add it to the DOM and return a reference to it.

        @param args: positional arguments
            the positional arguments to pass to the rect's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the rect's constructor'''

        rect = Rect(*args, **kwargs)
        self.elements.append(rect)
        return rect

    def circle(self, *args, **kwargs):
        '''Create a circle, add it to the DOM and return a reference to it. All
        arguments are passed to the circle's constructor.

        @param args: positional arguments
            the positional arguments to pass to the circle's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the circle's constructor'''

        circle = Circle(*args, **kwargs)
        self.elements.append(circle)
        return circle

    def ellipse(self, *args, **kwargs):
        '''Create a ellipse, add it to the DOM and return a reference to it. 
        All arguments are passed to the circle's constructor.

        @param args: positional arguments
            the positional arguments to pass to the circle's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the circle's constructor'''

        ellipse = Ellipse(*args, **kwargs)
        self.elements.append(ellipse)
        return ellipse

    def line(self, *args, **kwargs):
        '''Create a line, add it to the DOM and return a reference to it. All 
        arguments are passed to the line's constructor.

        @param args: positional arguments
            the positional arguments to pass to the line's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the line's constructor'''

        line = Line(*args, **kwargs)
        self.elements.append(line)
        return line

    def polyline(self, *args, **kwargs):
        '''Create a polyline, add it to the DOM and return a reference to it. 
        All arguments are passed to the polyline's constructor.

        @param args: positional arguments
            the positional arguments to pass to the polyline's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the polyline's constructor'''

        polyline = Polyline(*args, **kwargs)
        self.elements.append(polyline)
        return polyline

    def polygon(self, *args, **kwargs):
        '''Create a polygon, add it to the DOM and return a reference to it. 
        All arguments are passed to the polygon's constructor.

        @param args: positional arguments
            the positional arguments to pass to the polygon's constructor
        @param kwargs: keyword arguments
            the keyword arguments to pass to the polygon's constructor'''

        polygon = Polygon(*args, **kwargs)
        self.elements.append(polygon)
        return polygon

    def render(self):
        '''Generate the XML for this canvas and all of its elements.'''

        content = '\n'.join(e.render() for e in self.elements)

        return self.TEMPLATE.format(width=self.width, 
                                    height=self.height,
                                    content=content,
                                    meta=self.meta())

    def save(self, path):
        '''Save this canvas to a file.

        @param path: str
            the path to the output file'''
        
        with open(path, 'w') as outfile:
            outfile.write(self.render())

