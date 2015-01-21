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
		# our map.
		if line['X'] == "0" or line['Y'] == "0":
			continue

		# Setup a new dictionary for each iteration.
		data = {}

		# Assign line items to appropriate GeoJSON fields.
		data['type'] = 'Feature'
		data['id'] = index
		data['properties'] = {'description': line['INCIDENT_TYPE_DESCRIPTION'],
							  'date': line['DAY_WEEK']}
		data['geometry'] = {'type': 'Point',
							'coordinates': (line['X'], line['Y'])}

		# Add data dictionary to our item_list
		item_list.append(data)

		# For each point in our item_list, we add the point to our
		# dictionary. Setdefault creates a key called 'features' that
		# has a value type of an empty list. With each iteration, we
		# are appending our point to that list.
		for point in item_list:
			geo_map.setdefault('features', []).append(point)

		# Now that all data is parsed in GeoJSON, write to a file so we
		# can upload it to gist.github.com
		with open('file_Bos.geojson', 'w') as f:
			f.write(geojson.dumps(geo_map))

def main():
	data_items = p.MY_FILE
	parsed_data = p.parse(data_items, ",")
	short_list = parsed_data[:20000]

	return create_map(short_list)

if __name__ == "__main__":
	main()