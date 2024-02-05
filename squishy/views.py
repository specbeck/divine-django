from django.shortcuts import render

import random

def annotate_tiles(n):
    tile_map = [i for i in range(n)]
    random.shuffle(tile_map)

    for i, val in enumerate(tile_map):
        if (val % 2 == 0) or (val % 7 == 0):
            tile_map[i] = "small"
        elif (val % 5 == 0) or (val % 3 == 0):
            tile_map[i] = "medium"
        else:
            tile_map[i] = "large"
    return tile_map
# Create your views here.
def index(request):
    return render(request, "squishy/index.html", {
        "map" : annotate_tiles(100)
    })