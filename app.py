import folium
from streamlit_folium import st_folium
import streamlit as st

# Function to categorize the attraction type based on name and description
def categorize_attraction_type(name, description):
    name = name.lower()  # Convert name to lowercase for easier matching
    description = description.lower()  # Convert description to lowercase for easier matching

    # Historical sites
    if any(keyword in name or keyword in description for keyword in ["temple", "fort", "palace", "historical", "monument", "museum", "ruins", "castle"]):
        return "Historical"

    # Natural wonders
    elif any(keyword in name or keyword in description for keyword in ["rainforest", "beach", "mountain", "island", "park", "cave"]):
        return "Natural"

    # Amusement parks
    elif any(keyword in name or keyword in description for keyword in ["amusement", "theme park", "ride", "bridge", "towers", "lagoon"]):
        return "Amusement"

    # Default to Unknown
    else:
        return "Unknown"

# Streamlit app title
st.title("Tourist Map of Malaysia")

# Predefined dataset of tourist attractions
predefined_data = [
    {"Name": "A Famosa", "Description": "Historical fortress in Melaka", "Latitude": 2.1936, "Longitude": 102.2491},
    {"Name": "Kek Lok Si Temple", "Description": "Buddhist temple in Penang", "Latitude": 5.3566, "Longitude": 100.2736},
    {"Name": "Langkawi Sky Bridge", "Description": "Scenic bridge with mountain views", "Latitude": 6.3721, "Longitude": 99.6656},
    {"Name": "Taman Negara", "Description": "Rainforest national park", "Latitude": 4.3833, "Longitude": 102.4167},
    {"Name": "Sunway Lagoon", "Description": "Popular theme park in Selangor", "Latitude": 3.0738, "Longitude": 101.6078},
    # Additional attractions
    {"Name": "Gunung Mulu National Park", "Description": "UNESCO World Heritage Site with caves and karst formations", "Latitude": 4.0545, "Longitude": 114.8125},
    {"Name": "Perhentian Islands", "Description": "Beautiful islands with crystal-clear waters", "Latitude": 5.9167, "Longitude": 102.7333},
    {"Name": "Sipadan Island", "Description": "World-class diving site in Sabah", "Latitude": 4.1141, "Longitude": 118.6280},
    {"Name": "Batu Caves", "Description": "Limestone caves and Hindu temple", "Latitude": 3.2379, "Longitude": 101.6831},
    {"Name": "Mount Kinabalu", "Description": "Highest peak in Southeast Asia", "Latitude": 6.0759, "Longitude": 116.5580},
    {"Name": "Penang Hill", "Description": "Hill with natural beauty and a funicular railway", "Latitude": 5.4333, "Longitude": 100.2731},
    {"Name": "Putrajaya Mosque", "Description": "Modern mosque with unique architecture", "Latitude": 2.9408, "Longitude": 101.6929},
    {"Name": "Desaru Coast", "Description": "Beautiful beach destination in Johor", "Latitude": 1.5667, "Longitude": 104.2500},
    {"Name": "Malacca River Cruise", "Description": "Scenic boat ride along the Malacca River", "Latitude": 2.1971, "Longitude": 102.2521},
    {"Name": "Cameron Highlands", "Description": "Cool hill station known for tea plantations", "Latitude": 4.4700, "Longitude": 101.3800}
]

# Categorize each attraction
for row in predefined_data:
    row['Type'] = categorize_attraction_type(row['Name'], row['Description'])

# Initialize the map
map_center = [4.2105, 101.9758]  # Center of Malaysia
tourist_map = folium.Map(location=map_center, zoom_start=6)

# Create feature groups for different types of attractions
layers = {
    "Historical": folium.FeatureGroup(name="Historical Sites"),
    "Natural": folium.FeatureGroup(name="Natural Wonders"),
    "Amusement": folium.FeatureGroup(name="Amusement Parks"),
    "Unknown": folium.FeatureGroup(name="Unknown Attractions")  # Added Unknown layer
}

# Marker colors for each type
marker_colors = {
    "Historical": "blue",
    "Natural": "green",
    "Amusement": "red",
    "Unknown": "gray"
}

# Add markers for each attraction
for attraction in predefined_data:
    attraction_type = attraction["Type"]
    popup_content = f"<b>{attraction['Name']}</b><br>{attraction['Description']}"

    folium.Marker(
        location=[attraction["Latitude"], attraction["Longitude"]],
        popup=folium.Popup(popup_content, max_width=300),
        tooltip=attraction["Name"],
        icon=folium.Icon(color=marker_colors.get(attraction_type, "gray"))
    ).add_to(layers[attraction_type])  # Ensure all types are accounted for

# Add layers to map
for layer_name, layer_group in layers.items():
    layer_group.add_to(tourist_map)

# Add layer control
folium.LayerControl().add_to(tourist_map)

# Add total attractions label on the map
total_attractions = len(predefined_data)
folium.Marker(
    location=[6.5, 105.5],  # Coordinates where you want the label
    icon=folium.DivIcon(html=f'<div style="font-size: 16px; color: black;">Total Attractions: {total_attractions}</div>')
).add_to(tourist_map)

# Display the map
st_map = st_folium(tourist_map, width=700, height=500)

# Show total attractions count
st.write(f"**Total Attractions:** {total_attractions}")
