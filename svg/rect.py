from base import SVGBase

class Rect(SVGBase):
    '''An SVG rect.'''

    TEMPLATE = '''\
<rect x="{x}" y="{y}" width="{width}" height="{height}" {meta}></rect>'''

    def __init__(self, x, y, width, height, **kwargs):
        '''Create the rect object, with additional metadata.

        @param x: float
            the x coordinate of the corner closest to the origin
        @param y: float
            the y coordinate of the corner closest to the origin
        @param width: float
            the width of the rectangle
        @param height: float
            the height of the rectangle
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Rect, self).__init__(**kwargs)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self):
        '''Generate the XML for this element.'''

        return self.TEMPLATE.format(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            meta=self.meta())

