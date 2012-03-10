from attrs import Attrs

class SVGBase(object):
    '''A class holding common functionality for all SVG objects.'''

    def __init__(self, *args, **kwargs):
        '''Create the SVGBase object.

        @param args: positional parameters
            a tuple of (key,value) attributes
        @param kwargs: keyword parameters
            a dictionary of attributes'''

        load_defaults = kwargs.pop('load_defaults', True)

        attributes = Attrs(*args, **kwargs)

        object.__setattr__(self, 'attributes', attributes)
        object.__setattr__(self, 'meta', Attrs())
        object.__setattr__(self, 'transform', list())
        object.__setattr__(self, 'children', list())
        object.__setattr__(self, 'load_defaults', load_defaults)

    def __getitem__(self, name):
        '''Return the attribute with the given name.

        @param name: str
            the name of the attribute to get'''

        return object.__getattribute__(self, 'attributes')[name]

    def __setitem__(self, name, value):
        '''Forward the item assignment to the attributes mapping.

        @param name: str
            the name of the attribute to set
        @param value: object
            the new value of the attribute'''

        object.__getattribute__(self, 'attributes')[name] = value

    def __getattribute__(self, name):
        '''Return the metadata if requested, otherwise look the attribute in
        this SVG elements attributes structure.

        @param name: str
            the name of the attribute to fetch'''

        try:
            return getattr(object.__getattribute__(self, 'attributes'), name)
        except AttributeError:
            pass

        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        '''Set the value of attribute 'name'. 
        
        @param name: str
            the name of the attribute to set
        @param value: object
            the new value of the attribute'''

        setattr(object.__getattribute__(self, 'attributes'), name, value)

    def add_child(self, child):
        '''Add an SVG element to this one as a child element.

        @param child: SVGBase
            the SVG element to add as a child'''

        object.__getattribute__(self, 'children').append(child)

    def matrix(self, a, b, c, d, e, f):
        '''Create a group with a matrix transformation, add it to the DOM and
        return a reference to it. The matrix takes the form:

            [ [a  c  e] 
              [b  d  f] 
              [0  0  1] ]

        @param a: float
            the x-scaling factor
        @param b: float
            the y-scaling factor
        @param c: float
            the x-skewing factor
        @param d: float
            the y-skewing factor
        @param e: float
            the x-translation factor
        @param f: float
            the y-translation factor'''

        transform = object.__getattribute__(self, 'transform')
        transform.append('matrix({}, {}, {}, {}, {}, {})'.format(a, b, c, d, e, f))
        return self

    def translate(self, tx, ty):
        '''Create a group with a translation tranformation, add it to the DOM
        and return a reference to it.

        @param tx: float
            the x translation
        @param ty: float
            the y translation'''

        transform = object.__getattribute__(self, 'transform')
        transform.append('translate({} {})'.format(tx, ty))
        return self

    def scale(self, sx, sy):
        '''Create a group with a scaling tranformation, add it to the DOM and 
        return a reference to it.

        @param sx: float
            the x scaling factor
        @param sy: float
            the y scaling factor'''

        transform = object.__getattribute__(self, 'transform')
        transform.append('scale({} {})'.format(sx, sy))
        return self

    def rotate(self, theta, cx=0.0, cy=0.0):
        '''Create a group with a rotation transformation, add it to the DOM and
        return a reference to it.

        @param theta: float
            the angle, in degrees, of rotation
        @param cx: optional, float
            the x-center of rotation, defaults to 0
        @param cy: optional, float
            the y-center of rotation, defaults to 0'''

        transform = object.__getattribute__(self, 'transform')
        transform.append('rotate({}, {}, {})'.format(theta, cx, cy))
        return self

    def skew_x(self, theta):
        '''Skew in the x direction.

        @param theta: float
            the angle, in degrees, of the skew'''

        transform = object.__getattribute__(self, 'transform')
        transform.append('skewX({})'.format(theta))
        return self

    def skew_y(self, theta):
        '''Skew in the y direction.

        @param theta: float
            the angle, in degrees, of the skew'''

        transform = object.__getattribute__(self, 'transform')
        transform.append('skewY({})'.format(theta))
        return self

    def defaults(self):
        '''Return default values for this SVG element.'''

        load_defaults = object.__getattribute__(self, 'load_defaults')

        if load_defaults:
            yield 'fill', 'none'
            yield 'stroke', '#000'


    def render_attributes(self):
        '''Return the attributes and meta-attributes for this SVG element, 
        string-formatted for insertion into an XML tag.'''

        # set the attributes to the meta
        attributes = dict(self.meta)

        # apply default values if they have not been supplied
        for key, value in self.defaults():
            attributes[key] = value

        # create a dict of the base attributes
        base_attributes = dict(object.__getattribute__(self, 'attributes'))

        # perform any subclass-defined transformations on the attribute data
        try:
            renderers = object.__getattribute__(self, 'RENDERERS')
            for name in base_attributes:
                if name in renderers:
                    value = base_attributes[name]
                    base_attributes[name] = renderers[name](value)
        except AttributeError:
            pass

        # update the attributes so far with the base attributes, allowing any 
        # meta attributes with the same keys as base attributes to be clobbered
        attributes.update(base_attributes)

        # incorporate the transform into the attributes
        transform = object.__getattribute__(self, 'transform')
        if transform:
            attributes['transform'] = ' '.join(transform)

        return ' '.join('{}="{}"'.format(*kv) for kv in attributes.iteritems())

    def render(self, pretty=False, level=0):
        '''Render the XML for this SVG object.
        
        @param pretty: optional, bool
            a flag controlling pretty printing - pretty printing will perform
            indentations based on nesting level
        @param level: int
            the level of nesting this element is at'''

        padding = '' if not pretty else ' ' * (2 * level)

        tag = self.TAG
        attributes = self.render_attributes()

        children = object.__getattribute__(self, 'children')
        if children:
            children = '\n'.join(c.render(pretty=pretty, level=level+1) for c in children)

            xml = '<{tag} {attributes}>\n{children}\n{padding}</{tag}>'.format(
                tag=tag, 
                attributes=attributes, 
                children=children, 
                padding=padding)

        else:
            xml = '<{tag} {attributes} />'.format(tag=tag, attributes=attributes)

        return padding + xml
        

