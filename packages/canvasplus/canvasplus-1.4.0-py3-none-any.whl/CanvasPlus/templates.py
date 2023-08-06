"""Definition of the Template class."""
"""Luke-zhang-04
CanvasPlus (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
Licensed under the MIT License
"""


class Template:
    """Make templates for repeated display."""

    def __init__(self, *args, type_="", onRender=None, **kwargs):
        """Make templates for repeated display
        
        \nargs:
            x and y coordinates for the placement on render; if not given, the coordinates should be given when rendering the template
        \nkwargs: properties of the shape to be drawn
        """
        self.coords, self.onRender, self.properties, self.type = (
            args,
            onRender,
            kwargs,
            type_,
        )

    def copy(self):
        """returns a copy of the template."""
        return Template(
            *self.coords, shapeType=self.type, onRender=self.onRender, **self.properties
        )
