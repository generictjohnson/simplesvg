from base import SVGBase
from path import Path

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

    def path(self, meta=None, **kwargs):
        '''Create a path, add it to the DOM and return a reference to it.

        @param meta: optional, dict
            any metadata to pass to the newly created path
        @param kwargs: keyword parameters
            additional metadata'''

        path = Path(meta=meta, **kwargs)
        self.elements.append(path)
        return path

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

