#%%

## White belt

from math import pi

def volume_cylinder(radius, height):
    return pi * radius ** 2 * height

def volume_sphere(radius):
    return (4/3) * pi * radius ** 3

#%%
    
## Blue belt
    

import matplotlib.pyplot as plt

def whatever(number = 10):
    pass

def histogram():
    students = range(0, 100)
    bins = [0, 15, 50, 85, 100]

    plt.hist(students, bins, histtype="step", rwidth=0.9)

#%%
    
# blackbelt
    
from utils import functions
import data.triangles as tri


def calculate_triangles():
    for triangle in tri.triangle_definitions:
        area = functions.area_triangle(
                triangle["base"],
                triangle["height"])
        print(area)














