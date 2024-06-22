import requests
import folium
import json
import tkinter as tk
from tkinter import messagebox
import webbrowser

def get_geolocation(ip_address=''):
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    data = response.json()
    return data

def create_map(location, location_info, geojson_file):
    lat, lon = location.split(',')
    geolocation_map = folium.Map(location=[float(lat), float(lon)], zoom_start=12)
    folium.Marker(
        [float(lat), float(lon)],
        popup=folium.Popup(location_info, parse_html=True)
    ).add_to(geolocation_map)
    
    with open(geojson_file, encoding='utf-8') as f:
        geojson_data = json.load(f)
    folium.GeoJson(geojson_data).add_to(geolocation_map)
    
    geolocation_map.save('geolocation_map.html')

def fetch_geolocation():
    ip_address = ip_entry.get()
    location_data = get_geolocation(ip_address)
    loc_parts = location_data['loc'].split(',')
    lat = loc_parts[0]
    lon = loc_parts[1]
    
    location_info = (
        f"IP: {location_data['ip']}\n"
        f"City: {location_data['city']}\n"
        f"Region: {location_data['region']}\n"
        f"Country: {location_data['country']}\n"
        f"Location: {lat}, {lon}"
    )
    
    result_text.set(location_info)
    
    geojson_file = r'D:\PROJECTS\GeoTracker\custom.geo.json'  # Replace with your GeoJSON file path
    create_map(f"{lat},{lon}", location_info.replace('\n', '<br>'), geojson_file)
    messagebox.showinfo("Success", "Map has been created and saved as 'geolocation_map.html'.")

def open_map():
    webbrowser.open('geolocation_map.html')

# Create the main window
root = tk.Tk()
root.title("Geolocation Tracker")

# Create and place the widgets
tk.Label(root, text="Enter IP Address (leave blank for your own IP):").pack(pady=10)
ip_entry = tk.Entry(root, width=40)
ip_entry.pack(pady=5)

tk.Button(root, text="Fetch Geolocation", command=fetch_geolocation).pack(pady=10)
tk.Button(root, text="Open Map", command=open_map).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack(pady=10)

# Start the GUI event loop
root.mainloop()