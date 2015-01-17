import geojson
import parse as p

def create_map(data_file):
	# Define type of GeoJSON we're creating
	geo_map = {"type: FeatureCollection"}

	# Define empty list to collect each point to graph
	item_list = []

	# Iterate over out data to create GeoJSON document.
	# We're using enumerate() so we get the line, as well
	# the index, which is the line number.
	for index, line in enumerate(data_file):

		# Skip any zero coordinates as this will throw off
		# out map.
		if line['X'] == "0" or line['Y'] == "0":
			continue

		# Setup a new dictionary for each iteration.
		data = {}

		# Assign line items to appropriate GeoJSON fields.
		data ['type'] = 'Feature'
		data ['id'] = index
		data['properties'] = {'title': line['Categor'],
							  'description': line['Descript'],
							  'date': line['Date']}
		data['geometry'] = {'type': 'Point',
							'coordinates': (line['X'], line['Y'])}

		# Add data dictionary to our item_list
		item_list.append(data)