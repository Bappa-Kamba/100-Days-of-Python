import colorgram
import os

program_directory = os.path.dirname(__file__)

extracted_colors = colorgram.extract(program_directory+"/pic.jpg", 30)

colors = []
for color in extracted_colors:
    colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))

print(colors)
