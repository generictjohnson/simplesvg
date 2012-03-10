from circle import Circle
from ellipse import Ellipse
from group import Group
from line import Line
from path import Path
from polygon import Polygon
from polyline import Polyline
from rect import Rect

class Canvas(Group):
    '''The container for all SVG elements.'''

    TEMPLATE = '''\
<svg xmlns="http://www.w3.org/2000/svg" 
     width="{width:d}pt"
     height="{height:d}pt"
     viewbox="0 0 {width:d} {height:d}"
     version="1.1" {meta}>
    {children}
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

        super(Canvas, self).__init__(**kwargs)
        self.width = width
        self.height = height

    def render(self):
        '''Generate the XML for this canvas and all of its elements.'''

        children = '\n'.join(e.render() for e in self.children)

        return self.TEMPLATE.format(width=self.width,
                                    height=self.height,
                                    children=children,
                                    meta=self.meta())

    def save(self, path):
        '''Save this canvas to a file.

        @param path: str
            the path to the output file'''
        
        with open(path, 'w') as outfile:
            outfile.write(self.render())

