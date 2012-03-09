from base import SVGBase

class Ellipse(SVGBase):
    '''An SVG ellipse.'''

    TEMPLATE = '''\
<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" {meta}></ellipse>'''

    def __init__(self, cx, cy, rx, ry, **kwargs):
        '''Create the ellipse object, with additional metadata.

        @param cx: float
            the x coordinate of the center of the ellipse
        @param cy: float
            the y coordinate of the center of the ellipse
        @param rx: float
            the x-radius of the ellipse
        @param ry: float
            the y-radius of the ellipse
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Ellipse, self).__init__(**kwargs)

        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry

    def render(self):
        '''Generate the XML for this element.'''

        return self.TEMPLATE.format(
            cx=self.cx,
            cy=self.cy,
            rx=self.rx,
            ry=self.ry,
            meta=self.meta())

