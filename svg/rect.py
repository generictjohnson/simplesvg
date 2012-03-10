from base import SVGBase

class Rect(SVGBase):
    '''An SVG rect.'''

    TAG = 'rect'

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

        super(Rect, self).__init__(x=x, y=y, width=width, height=height, **kwargs)

