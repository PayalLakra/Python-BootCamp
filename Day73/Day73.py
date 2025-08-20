'''
Topics to be Covered:
- How to visualise your data and create charts with Matplotlib
- How to pivot, group and manipulate your data with Pandas to get it into the format you want
- How to work with timestamps and time-series data
- How to style and customise a line chart to your liking
'''

# Learning Points ->

# used .groupby() to explore the number of posts and entries per programming language
# converted strings to Datetime objects with to_datetime() for easier plotting
# reshaped our DataFrame by converting categories to columns using .pivot()
# used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()
# created (multiple) line charts using .plot() with a for-loop
# styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.
# added a legend to tell apart which line is which by colour
# smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.