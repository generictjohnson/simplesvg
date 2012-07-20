from base import SVGBase

class Text(SVGBase):
    '''SVG text.'''

    TAG = 'text'

    def __init__(self, x, y, text, **kwargs):
        '''Create the text object, with additional metadata.

        @param x: float
            the x coordinate of first character
        @param y: float
            the y coordinate of first character
        @param text: str
            the text to display
        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Text, self).__init__(x=x, y=y, content=text, **kwargs)
