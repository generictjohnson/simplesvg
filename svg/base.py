

class SVGBase(object):
    '''A class holding common functionality for all SVG objects.'''

    def __init__(self, meta=None, **kwargs):
        '''Create the SVGBase object.

        @param meta: dict
            any metadata to store as attributes in the XML file
        @param kwargs: keyword parameters
            metadata as keyword parameters'''

        if meta is not None:
            meta.update(kwargs)
            kwargs = meta

        self._meta = kwargs

    def meta(self):
        '''Return the metadata, string formatted for insertion into an XML tag.'''
        
        return ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in self._meta.iteritems())
