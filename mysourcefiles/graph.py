"""
Part II: Take the data we just parsed and visualize it using
popular Python math libraries.
"""

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import parse

original_data = parse.MY_FILE
parsed_data = parse.parse(original_data, ",")


def visualize_days():
	"""Visualize data by the day of week"""

	short_list = parsed_data[:20000]

	# make a new variable, 'counter', for iterating through
	# each line of data in the short_list, and count how many
	# incidents happen on each day of the week
	counter = Counter(item["DAY_WEEK"] for item in short_list)

	# seperate the x-axis data (the days of the week from the
	# 'counter' variable) from the y-axis data 
	# (the number of incidents for each day)
	data_list = [counter["Monday"],
				counter["Tuesday"],
				counter["Wednesday"],
				counter["Thursday"],
				counter["Friday"],
				counter["Saturday"],
				counter["Sunday"]
				]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	# with that y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)

	# Assign labels to the plot
	plt.xticks(range(len(day_tuple)), day_tuple)

	# Save the plot
	plt.savefig("Days.png")

	# Close figure
	#plt.clf()
	plt.show()

def visualize_type():
	"""Visualize data by category in a bar graph"""
	
	data_file = parsed_data[:20000]
   # same as before, this returns a dict where it sums the total
   # incidents per Category.

	counter = Counter(item["INCIDENT_TYPE_DESCRIPTION"] for item in data_file)
	
   # Set the labels which are based on the keys of our counter.
   # Since order doesn't matter, we can just use counter.keys()
	labels = tuple(counter.keys())

	# Set where the labels hit the x-axis
	xlocations = np.array(range(len(labels))) + 1
	

	width = 0.5

	plt.figure(figsize=(16,9))
	# Assign data to a bar plot
	plt.bar(xlocations, counter.values(), width=width)

	# Assign labels and tick location to x-axis
	plt.xticks(xlocations + width / 2, labels, rotation=90)

	# give some more room so the labels aren't cut off in the graph
	plt.subplots_adjust(bottom= 0.4, right=0.98, left=0.05)

	# Save the plot
	
	plt.savefig("Type.png")
	
	# Close figure
	#plt.clf()

	plt.show()

def main():
	visualize_type()
	visualize_days()
if __name__ == "__main__":
	main()