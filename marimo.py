# Email: 23f1002802@ds.study.iitm.ac.in

# Cell 1: Interactive slider widget using Marimo UI
slider = mo.ui.slider(1, 20, value=10, label="Number of points")

# Cell 2: Generate data points based on slider value
data_points = list(range(1, slider.value + 1))

# Cell 3: Compute squares of data points (dependent on data_points)
squared_points = [x**2 for x in data_points]

# Cell 4: Dynamic markdown output reflecting slider state
mo.md(f"### Data Analysis Output\nYou selected **{slider.value}** data points. Their squares are:\n{', '.join(map(str, squared_points))}")

# Comments:
# The slider widget provides interactive control to select the number of points.
# Subsequent cells depend reactively on the slider’s current value.
# Markdown cell dynamically updates to display analysis results.
