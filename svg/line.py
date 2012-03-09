from base import SVGBase

class Line(SVGBase):
    '''An SVG line.'''

    TEMPLATE = '''\
<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {meta}></line>'''

    def __init__(self, x1, y1, x2, y2, **kwargs):
        '''Create the line object, with additional metadata.

        @param x1: float
            the x coordinate of the first point of the line
        @param y1: float
            the y coordinate of the first point of the line
        @param x2: float
            the x coordinate of the second point of the line
        @param y2: float
            the y coordinate of the second point of the line
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Line, self).__init__(**kwargs)

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def render(self):
        '''Generate the XML for this element.'''

        return self.TEMPLATE.format(
            x1=self.x1,
            y1=self.y1,
            x2=self.x2,
            y2=self.y2,
            meta=self.meta())

