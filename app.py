import csv
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

# File uploader for the CSV file
uploaded_file = st.file_uploader("Upload a CSV file with tourist attractions", type=["csv"])

if uploaded_file:
    # Read the CSV file
    data = []
    csv_reader = csv.DictReader(uploaded_file.read().decode('utf-8').splitlines())

    for row in csv_reader:
        # Convert Latitude and Longitude to float
        row['Latitude'] = float(row['Latitude'])
        row['Longitude'] = float(row['Longitude'])

        # Categorize the attraction
        row['Type'] = categorize_attraction_type(row['Name'], row['Description'])

        data.append(row)

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
    for attraction in data:
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
    total_attractions = len(data)
    folium.Marker(
        location=[6.5, 105.5],  # Coordinates where you want the label
        icon=folium.DivIcon(html=f'<div style="font-size: 16px; color: black;">Total Attractions: {total_attractions}</div>')
    ).add_to(tourist_map)

    # Display the map
    st_map = st_folium(tourist_map, width=700, height=500)

    # Show total attractions count
    st.write(f"**Total Attractions:** {total_attractions}")
%%writefile app.py
import csv
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

# File uploader for the CSV file
uploaded_file = st.file_uploader("Upload a CSV file with tourist attractions", type=["csv"])

if uploaded_file:
    # Read the CSV file
    data = []
    csv_reader = csv.DictReader(uploaded_file.read().decode('utf-8').splitlines())

    for row in csv_reader:
        # Convert Latitude and Longitude to float
        row['Latitude'] = float(row['Latitude'])
        row['Longitude'] = float(row['Longitude'])

        # Categorize the attraction
        row['Type'] = categorize_attraction_type(row['Name'], row['Description'])

        data.append(row)

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
    for attraction in data:
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
    total_attractions = len(data)
    folium.Marker(
        location=[6.5, 105.5],  # Coordinates where you want the label
        icon=folium.DivIcon(html=f'<div style="font-size: 16px; color: black;">Total Attractions: {total_attractions}</div>')
    ).add_to(tourist_map)

    # Display the map
    st_map = st_folium(tourist_map, width=700, height=500)

    # Show total attractions count
    st.write(f"**Total Attractions:** {total_attractions}")

