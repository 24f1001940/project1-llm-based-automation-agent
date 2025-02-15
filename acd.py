from geopy.geocoders import Nominatim

# Activate the Nominatim geocoder
locator = Nominatim(user_agent="myGeocoder")

# Geocode the city Mexico City in Mexico
location = locator.geocode("Quanzhou, China")

# Check if the location was found
if location:
    # Retrieve the bounding box
    bounding_box = location.raw.get('boundingbox', [])

    # Check if the bounding box is available
    if len(bounding_box) > 1:
        # Extract the minimum latitude from the bounding box (the first value in the list)
        min_latitude = bounding_box[0]
        print(f"The minimum latitude of the bounding box for Mexico City is: {min_latitude}")
    else:
        print("Bounding box information not available.")
else:
    print("Location not found.")
