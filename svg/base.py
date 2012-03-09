

class SVGBase(object):
    '''A class holding common functionality for all SVG objects.'''

    def __init__(self, **kwargs):
        '''kwargs holds meta data'''

        self._meta = kwargs

    def meta(self):
        
        return ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in self._meta.iteritems())
