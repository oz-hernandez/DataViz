"""
Part II: Take the data we just parsed and visualize it using
popular Python math libraries.
"""

from collections import Counter

import matplotlib.pyplot as plt
import parse

def visualize_days():
	"""Visualize data by the day of week"""

# grab our parsed data that we parsed earlier
original_data = parse.MY_FILE
parsed_data = parse.parse(original_data, ",")
short_list = parsed_data[:15]

# make a new variable, 'counter', for iterating through
# each line of data in the parsed data, and count how many
# incidents happen on each day of the week
counter = Counter(item["DAY_WEEK"] for item in short_list)
