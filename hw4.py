class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)


def build_graph(population_file, road_file):
    cities = {}

    with open(population_file) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(":")
            name = parts[0].strip()
            population = int(parts[1].strip())
            #create a city object and store it into cities dictionary
            cities[name] = City(name, population)
    with open(road_file) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(":")
            city_1 = cities[parts[0].strip()]
            city_2 = cities[parts[1].strip()]
            #since highway goes both way, it's an undirected graph
            city_1.add_neighbor(city_2)
            city_2.add_neighbor(city_1)
    return list(cities.values())


