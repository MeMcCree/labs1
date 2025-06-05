from math import cos, radians


def latitude(phi):
    r_earth = 6370
    phi_rad = radians(phi)
    R = r_earth * cos(phi_rad)
    print(round(R))