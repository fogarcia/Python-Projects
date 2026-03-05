import sys

def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.155]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")
    # coordinates = (42.376, -71.115)
    # latitude, longiude = coordinates
    # print(f"Latitude: {latitude}")
    # print(f"Longitude: {longiude}")

    # coordinates[0] = -42.376 - will give an error due to tuples being immutable.

main()