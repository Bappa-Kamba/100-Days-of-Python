import os
import pandas

filename = os.path.abspath("DAY-25/squirrel_data.csv")

data = pandas.read_csv(filename)
fur_colors = data['Primary Fur Color']

color_data = pandas.DataFrame(fur_colors.value_counts())

color_data.to_csv('fur_color_count.csv')