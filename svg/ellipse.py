from base import SVGBase

class Ellipse(SVGBase):
    '''An SVG ellipse.'''

    TAG = 'ellipse'

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

        super(Ellipse, self).__init__(cx=cx, cy=cy, rx=rx, ry=ry, **kwargs)

