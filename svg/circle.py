from base import SVGBase

class Circle(SVGBase):
    '''An SVG circle.'''

    TAG = 'circle'

    def __init__(self, cx, cy, r, **kwargs):
        '''Create the circle object, with additional metadata.

        @param cx: float
            the x coordinate of the center of the circle
        @param cy: float
            the cy coordinate of the center of the circle
        @param r: float
            the radius of the circle
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Circle, self).__init__(cx=cx, cy=cy, r=r, **kwargs)

