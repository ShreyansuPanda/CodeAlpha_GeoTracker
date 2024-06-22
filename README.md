# CodeAlpha Task-3: GeoLocation Tracker

A geolocation tracking application built with Python, Tkinter for the GUI, and Folium for creating interactive maps. This application allows users to fetch geolocation data based on an IP address and visualize the location on a map.

##Video Showcase: https://www.linkedin.com/posts/shreyansu-panda-5a9854276_pythonprogramming-python-programming-activity-7210174493103730688-d5F9?utm_source=share&utm_medium=member_desktop

## Features

- Fetch geolocation data using the IPinfo API.
- Display location information including IP, city, region, country, and coordinates.
- Create an interactive map with the location marked.
- Open the generated map in a web browser.

## Tools Used

- **Python**
- **Tkinter**: For creating the graphical user interface.
- **Folium**: For generating interactive maps.
- **Requests**: For making API calls.
- **Webbrowser**: For opening the generated map in a web browser.

## Requirements

- Python 3.x
- Requests
- Folium
- Tkinter (usually included with Python)

## Installation

1. Clone the repository
    
2. Install required packages:
    ```sh
    pip install requests folium
    ```

## Usage

1. Run the application:
    ```sh
    python Tracker.py
    ```

2. The main window of the application will appear. Here are the available functionalities:

    - **Enter IP Address:** Enter an IP address to fetch its geolocation. Leave blank to use your own IP address.
    - **Fetch Geolocation:** Click the button to fetch and display the geolocation data.
    - **Open Map:** Click the button to open the generated map in your default web browser.

## Code Structure

- `Tracker.py`: Contains the entire application logic including fetching geolocation data, creating maps, and the Tkinter GUI implementation.

## Functions

### `Tracker.py`

- **`get_geolocation(ip_address='')`**: Fetches geolocation data from IPinfo API.
- **`create_map(location, location_info, geojson_file)`**: Creates a map with the specified location and saves it as an HTML file.
- **`fetch_geolocation()`**: Fetches the geolocation data, creates a map, and updates the GUI with location information.
- **`open_map()`**: Opens the generated map in the default web browser.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
