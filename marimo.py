# Email: 23f1002802@ds.study.iitm.ac.in

# Cell 1: Data input and processing cell
# This cell creates a list of numbers depending on the slider value.
slider_value = slider(label="Number of points", min=1, max=20, value=10)

# Generating data dependent on the slider value
data_points = list(range(1, slider_value + 1))

# Cell 2: Analysis cell dependent on Cell 1's output
# This cell computes the square of each data point.
squared_points = [x**2 for x in data_points]

# Dynamic markdown output based on slider state
md(f"### Data Analysis Output\nYou selected **{slider_value}** data points. Their squares are:\n{', '.join(map(str, squared_points))}")

# Comments:
# The slider_value controls the number of data points generated in Cell 1.
# The squared_points list in Cell 2 is dynamically updated based on data_points from Cell 1.
# The markdown output dynamically displays the current state of the analysis.
