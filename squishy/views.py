from django.shortcuts import render

import random

def generate_tiles(n):
    types = ["vlarge", "large", "medium", "small", "vsmall"]
    weights = [0.1, 0.25, 0.3, 0.25, 0.1]
    tiles = random.choices(population=types, weights=weights, k=n)
    random.shuffle(tiles)
    return tiles

def yield_pixels(n):
    types = ["large", "medium", "small"]
    weights = [0.25, 0.5, 0.25]
    tiles = random.choices(population=types, weights=weights, k=n)
    random.shuffle(tiles)
    for _ in range(2):
        yield tiles

# def annotate_tiles(n):
#     tile_map = [i for i in range(n)]
#     random.shuffle(tile_map)

#     for i, val in enumerate(tile_map):
#         if (val % 2 == 0):
#             tile_map[i] = "vsmall"
#         elif (val % 3 == 0):
#             tile_map[i] = "small"
#         elif (val % 5 == 0):
#             tile_map[i] = "medium"
#         elif (val % 7 == 0):
#             tile_map[i] = "vlarge"
#         else:
#             tile_map[i] = "large"
#     return tile_map

# Create your views here.
def index(request):
    return render(request, "squishy/index.html", {
        "map" : generate_tiles(100)
    })
    
def pixels(request):
    return render(request, "squishy/pixels.html", {
        "map": generate_tiles(100000)
    })