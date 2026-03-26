distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}

def main():
    spacecraft = input("Enter spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"{spacecraft} does not exist.")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    
    m = covert(au)
    print(f"{m} m away")

def covert(au):
    return au * 149597870700

if __name__ == "__main__":
    main()