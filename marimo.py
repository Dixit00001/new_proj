# Email: 23f1002802@ds.study.iitm.ac.in

# Cell 1: Interactive slider widget for selecting number of points
slider_value = slider(label="Number of points", min=1, max=20, value=10)

# Generating data dependent on slider value
data_points = list(range(1, slider_value + 1))

# Cell 2: Compute squares of data points (dependent on data_points)
squared_points = [x**2 for x in data_points]

# Dynamic markdown output based on current slider state
md(f"### Data Analysis Output\nYou selected **{slider_value}** data points. Their squares are:\n{', '.join(map(str, squared_points))}")

# Comments:
# The slider_value widget controls the number of data points generated in Cell 1.
# squared_points in Cell 2 depends on data_points from Cell 1.
# The markdown output dynamically updates reflecting current slider selection.

