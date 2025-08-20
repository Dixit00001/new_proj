# Email: 23f1002802@ds.study.iitm.ac.in

# Cell 1: Create an interactive slider widget using Marimo UI
slider = mo.ui.slider(1, 20, value=10, label="Number of points")

# Cell 2: Generate data points dependent on slider value
data_points = list(range(1, slider.value + 1))

# Cell 3: Calculate squares of data points (dependent on data_points)
squared_points = [x**2 for x in data_points]

# Cell 4: Dynamic markdown output based on slider state
mo.md(f"### Data Analysis Output\nYou selected **{slider.value}** data points. Their squares are:\n{', '.join(map(str, squared_points))}")

# Comments:
# The slider widget in Cell 1 lets the user select the number of data points.
# Cell 2 generates a list of data points based on the slider's current value.
# Cell 3 computes the squares of these data points.
# Cell 4 outputs dynamic markdown reflecting the current slider selection and computed values.


