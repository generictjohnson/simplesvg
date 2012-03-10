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

    TAG = 'svg'

    def __init__(self, width, height, **kwargs):
        '''Create the canvas.

        @param width: int
            the width of the canvas in units of "pt"
        @param height: int
            the height of the canvas in units of "pt"
        @param meta: optional, dict
            the dictionary of metadata for the canvas
        @param kwargs: keyword parameters
            additional metadata'''

        super(Canvas, self).__init__(
            xmlns='http://www.w3.org/2000/svg',
            width=width, 
            height=height,
            viewbox='0 0 {} {}'.format(width, height),
            version='1.1',
            **kwargs)

    def flip_y(self):
        
        return self.transform(('matrix', (1, 0, 0, -1, 0, self.height)))

    def save(self, path, pretty=False):
        '''Save this canvas to a file.

        @param path: str
            the path to the output file
        @param pretty: optional, bool
            a flag controlling pretty printing - pretty printing will perform
            indentations based on nesting level'''
        
        with open(path, 'w') as outfile:
            outfile.write(self.render(pretty=pretty))

