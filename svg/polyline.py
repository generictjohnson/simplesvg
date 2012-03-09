from base import SVGBase

class Polyline(SVGBase):
    '''An SVG line.'''

    TEMPLATE = '''\
<polyline points="{points}" {meta}></polyline>'''

    def __init__(self, *args, **kwargs):
        '''Create the polyline object, with additional metadata.

        @param args: positional arguments
            the points of the polyline, as (x,y) float pairs
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Polyline, self).__init__(**kwargs)

        self.points = list(args)

    def render(self):
        '''Generate the XML for this element.'''

        points = ' '.join('{},{}'.format(*p) for p in self.points)

        return self.TEMPLATE.format(
            points=points,
            meta=self.meta())

