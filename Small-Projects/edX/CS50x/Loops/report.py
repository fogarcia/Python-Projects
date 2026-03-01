def main():
    # spacecraft = {
    #     "name": "Voyager 1",
    #     "distance": "163"
    # }
    spacecraft = {
        "name": "James Webb Space Telescope"
    }
    spacecraft.update({"distance": "0.00001581", "orbit": "Sun"})
    # spacecraft["distance"] = "0.00001581"
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ============= Report =============
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    
    ==================================
    """
main()