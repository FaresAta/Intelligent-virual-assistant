import webbrowser

def open_google_maps(destination):
    """
    Opens Google Maps with directions to the specified destination.
    
    Args:
        destination (str): The destination for Google Maps.
    """
    if not destination.strip():
        return "Please specify a destination."
    
    google_maps_url = f"https://www.google.com/maps/dir/?api=1&destination={destination.replace(' ', '+')}"
    webbrowser.open(google_maps_url)
    return f"Opening Google Maps for directions to: {destination}"
