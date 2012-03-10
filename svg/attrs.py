import collections

class Attrs(dict):
    '''A subclass of dict that allows access to keys through dot notation as
       well.'''

    def __init__(self, *args, **kwargs):
        '''Create the Attrs object. The constructor parameters are simply
           forwarded to the dict constructor, so the same exact same types are
           accepted.

           @param args : positional parameters
               a series of either dicts or (key,value) pairs
           @param kwargs : keyword arguments
               additional key=value pairs, these take precedence over the
               positional parameters'''

        super(Attrs, self).__init__(*args, **kwargs)

        for k in self:
            v = self[k]
            if isinstance(v, collections.Mapping):
                self[k] = Attrs(v)

    def __getattribute__(self, name):
        '''Get the attribute from this object. Look for a key with the same
           name and return it if it exists.

           @param name: str
               the name of the attribute'''

        if name in self:
            return self[name]

        return super(Attrs, self).__getattribute__(name)

    def __setattr__(self, name, value):
        '''Set the attribute with name to value.

           @param name: str
               the name of the attribute
           @param value: object
               the value to set it to'''

        self[name] = value


