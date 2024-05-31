import sys, numpy as np
import heapq

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

algorithm, image = input_.split("\n\n")
image_grid = [list([x_ for x_ in x]) for x in image.split("\n")]

def expand_grid(image_grid, y_expand, x_expand):
    yext = [['.']*len(image_grid[0])]*y_expand
    image_grid = yext + image_grid + yext.copy()
    image_grid[0].append('xx')
    return image_grid

def enhance_pixel(y, x, image_grid, algorithm):
    # image_grid = np.array(grid)
    binary = ''
    for row in image_grid[y-1:y+2]:
        for bit in row[x-1:x+2]:
            binary += '1' if bit == '#' else '0'
    decimal = int(binary, 2)
    return algorithm[decimal]

print(enhance_pixel(3, 3, image_grid, algorithm))
