from functools import wraps
import math

from base import SVGBase

def requires_initalization(fn):
    '''A decorator for functions that require an initialized path. This will
    not throw an error, but rather silently initialize the pen to the origin.

    @param fn: function
        the function to decorate'''

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        if not self.d:
            self.move_to(0, 0)

        return fn(self, *args, **kwargs)
    return wrapper

def requires_open(fn):
    '''A decorator that will throw an error if the decorated function is called
    after the path has been closed.

    @param fn: function
        the function to decorate'''

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        closed = object.__getattribute__(self, 'closed')
        if closed:
            raise ValueError('cannot call {} on a closed path'.format(fn.__name__))

        return fn(self, *args, **kwargs)
    return wrapper

class Path(SVGBase):
    '''An SVG path element.
    
    The arc logic was taken from the libcairo library'''

    TAG = 'path'

    RENDERERS = {
        'd': ' '.join
    }

    def __init__(self, **kwargs):
        '''Create the path object, with additional metadata.

        @param kwargs: keyword parameters
            additional metadata as key/value pairs'''

        super(Path, self).__init__(d=list(), **kwargs)

        object.__setattr__(self, 'pen', None)
        object.__setattr__(self, 'closed', False)

    def _pen(self, x, y):
        '''Set the position of the pen.

        @param x: float
            the x-coordinate of the pen
        @param y: float
            the y-coordinate of the pen'''

        object.__setattr__(self, 'pen', (x, y))

    @requires_open
    def move_to(self, x, y):
        '''Move the pen to the location.

        @param x: float
            the x-coordinate of the new location of the pen
        @param y: float
            the y-coordinate of the new location of the pen'''

        self.d.append('M {:f} {:f}'.format(x, y))
        self._pen(x, y)

    @requires_initalization
    @requires_open
    def line_to(self, x, y):
        '''Draw a line from the current position to the new one.

        @param x: float
            the x-coordinate of where to draw the line
        @param y: float
            the y-coordinate of where to draw the line'''

        if (x, y) == self._pen:
            return

        self.d.append('L {:f} {:f}'.format(x, y))
        self._pen(x, y)

    @requires_open
    def close(self):
        '''Close the path. This prevents any further modifications.'''

        self.d.append('Z')
        object.__setattr__(self, 'closed', True)

    @requires_initalization
    @requires_open
    def curve_to(self, x1, y1, x2, y2, x, y):
        '''Draw a cubic Bezier curve from the current position to (x,y), using
        (x1,y1) as the control point for the current position and (x2,y2) as 
        the control point for (x,y).

        @param x1: float  
            the x-coordinate for the control point for leaving the current 
            position
        @param y1: float  
            the y-coordinate for the control point for leaving the current 
            position
        @param x2: float  
            the x-coordinate for the control point for entering the destination 
            position
        @param y2: float  
            the y-coordinate for the control point for entering the destination 
            position
        @param x: float  
            the x-coordinate for the destination position
        @param y: float  
            the y-coordinate for the destination position'''
        
        self.d.append('C {:f} {:f} {:f} {:f} {:f} {:f}'.format(x1, y1, x2, y2, x, y))
        self._pen(x, y)

    @requires_initalization
    @requires_open
    def _arc_segment(self, cx, cy, radius, theta1, theta2):
        '''Draw a circular arc (a portion of the circumference of a circle. 
        Angles are specified in radians, where 0 is at three o'clock and the
        positive direction is clockwise.

        @param cx: float
            the x-coordinate of the center of the circle
        @param cy: float
            the y-coordinate of the center of the circle
        @param radius: float
            the radius of the circle
        @param theta1: float
            the starting angle of the arc
        @param theta2: float
            the finishing angle of the arc'''
        
        r_sin_1 = radius * math.sin(theta1)
        r_cos_1 = radius * math.cos(theta1)
        r_sin_2 = radius * math.sin(theta2)
        r_cos_2 = radius * math.cos(theta2)

        h = 4.0/3.0 * math.tan((theta2 - theta1) / 4.0)

        self.curve_to(cx + r_cos_1 - h * r_sin_1,
                      cy + r_sin_1 + h * r_cos_1,
                      cx + r_cos_2 + h * r_sin_2,
                      cy + r_sin_2 - h * r_cos_2,
                      cx + r_cos_2,
                      cy + r_sin_2)

    @requires_initalization
    @requires_open
    def arc(self, cx, cy, radius, theta1, theta2, radians=False, max_segment_theta=math.pi/2):
        '''Draw a circular arc (a portion of the circumference of a circle. 
        Angles are specified in degrees, unless the keyword argument 'radians'
        is set to true. The angle with value 0 is at three o'clock and the
        positive direction is counter-clockwise, if positive x is to the right
        and positive y is up. This function will split up excessively large 
        angles into multiple paths, to preserve accuracy.

        @param cx: float
            the x-coordinate of the center of the circle
        @param cy: float
            the y-coordinate of the center of the circle
        @param radius: float
            the radius of the circle
        @param theta1: float
            the starting angle of the arc
        @param theta2: float
            the finishing angle of the arc
        @param max_segment_theta: float
            the maximum angle a curve can subtend - any requests that span more
            than this value will be broken up into multiple curves'''

        if not radians:
            theta1 = math.radians(theta1)
            theta2 = math.radians(theta2)

        self.line_to(cx + radius * math.cos(theta1),
                     cy + radius * math.sin(theta1))

        d_theta = theta2 - theta1
        if d_theta != 0.0:

            n_segments = int(math.ceil(abs(d_theta) / max_segment_theta))

            theta = theta1
            theta_step = d_theta / n_segments

            for i in xrange(n_segments):
                self._arc_segment(cx, cy, radius, theta, theta + theta_step)
                theta += theta_step

