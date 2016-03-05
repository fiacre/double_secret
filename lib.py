import random
import math
from simanneal import Annealer

def parse_cities(json_data):
    cities = {}
    for k in json_data.keys():
        (lat, lon) = json_data.get(k)
        print(k, lat, lon)
        cities[k] = (lat, lon)
    return cities

"""
everything below was freely stolen from  
https://github.com/perrygeo/simanneal
"""

def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 6371.0  # radius of Earth (km)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R

class TravellingSalesmanProblem(Annealer):

    """
    Run annealer with a travelling salesman problem.
    """
    
    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super().__init__(state)

    def move(self):
        """Swaps two cities in the route."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e


def run_anneal(cities):
    init_state = list(cities.keys())
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = {}
    for ka, va in cities.items():
        distance_matrix[ka] = {}
        for kb, vb in cities.items():
            if kb == ka:
                distance_matrix[ka][kb] = 0.0
            else:
                distance_matrix[ka][kb] = distance(va, vb)

    tsp = TravellingSalesmanProblem(init_state, distance_matrix)
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"  
    state, e = tsp.anneal()

    while state[0] != 'New York City':
        state = state[1:] + state[:1]  # rotate NYC to start
    print("%i mile route:" % e)
    print(state)
    for city in state:
        print("\t", city)
    return state

