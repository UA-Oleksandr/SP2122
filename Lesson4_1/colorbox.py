from color import Color
from box import Box
class ColorBox(Box, Color):

    def __init__(self, heights:float, width:float, colorValue:str):
        super().__init__(heights, width)
        Color.__init__(colorValue)

    def __str__(self):
        return (f"Width: {self.Width}"
                f"Height: {self.Heights}"
                f"Color: {self.ColorValue}")
