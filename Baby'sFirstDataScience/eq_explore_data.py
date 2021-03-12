import json 

# Explore the structure of the data.
filename = 'data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    # The json.load() function converts the data into a format Python can work 
    # with: in this case, a giant dictionary.

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:10])
print(lats[:10])

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    # Here we create a file to write this same data into a more readable format.
    json.dump(all_eq_data, f, indent=4)
