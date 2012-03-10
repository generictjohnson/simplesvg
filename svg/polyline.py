from base import SVGBase

class Polyline(SVGBase):
    '''An SVG line.'''

    TAG = 'polyline'

    def __init__(self, *args, **kwargs):
        '''Create the polyline object, with additional metadata.

        @param args: positional arguments
            the points of the polyline, as (x,y) float pairs
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        points = ' '.join('{},{}'.format(*a) for a in args)
        super(Polyline, self).__init__(points=points, **kwargs)

