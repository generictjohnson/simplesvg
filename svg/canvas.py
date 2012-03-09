from base import SVGBase
from path import Path

class Canvas(SVGBase):

    TEMPLATE = '''\
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:link="http://www.w3.org/1999"
     width="{width:d}pt"
     height="{height:d}pt"
     viewbox="0 0 {width:d} {height:d}"
     version="1.1" {meta}>
    {content}
 </svg>'''

    def __init__(self, width, height, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        self.width = width
        self.height = height

        self.elements = list()

    def path(self, **kwargs):
        path = Path(**kwargs)
        self.elements.append(path)
        return path

    def render(self):

        content = '\n'.join(e.render() for e in self.elements)

        return self.TEMPLATE.format(width=self.width, 
                                    height=self.height,
                                    content=content,
                                    meta=self.meta())

    def save(self, path):
        
        with open(path, 'w') as outfile:
            outfile.write(self.render())

