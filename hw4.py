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
#discovered is a set of visited cities
def dfs(source, discovered):
    for city in source.neighbors:
        if city not in discovered:
            discovered.add(city)
            dfs(city, discovered)

#task 3: Given the list of City objects, write a func to return the number of islands
def count_num_islands(cities):
    discovered = set()
    islands = 0
    for city in cities:
        if city not in discovered:
            islands += 1
            discovered.add(city)
            #add all the cities connected to the source city in the visited set
            dfs(city, discovered)
    return islands

#task 4: Given the list of City objects, write a function that would \n
# return the population of each island in the island archipelago. \n
# Note that this function would require you to find the population of each connected component in the graph. 



def dfs_population(source, discovered):
    total = source.population
    for city in source.neighbors:
        if city not in discovered:
            discovered.add(city)
            total += dfs_population(city, discovered) #add the population of neighbors
    return total

def count_island_population(cities):
    discovered = set()
    populations = []
    for city in cities:
        if city not in discovered:
            discovered.add(city)
            total = dfs_population(city, discovered)
            populations.append(total)#append the sum population of each island with one or more cities
    return populations

#task 5: Given two City objects, write a function that would return the minimum number of unique highways\n
# you can take to reach from one city to another.
# Note that this function requires you to find the distance, i.e., the number of unique highways between two cities.

def min_distance(start, end):
    if start == end:
        return 0
    discovered = set()
    discovered.add(start)
    cur = [start]

    distance = 0
    #when cur is not empty
    while cur:
        distance += 1
        nxt = []

        for city in cur:
            for neighbor in city.neighbors:
                if neighbor not in discovered:
                    if neighbor == end:
                        return distance #the first time we have distance returned is the shortest
                    discovered.add(neighbor)
                    nxt.append(neighbor)
        cur = nxt
    return -1

if __name__ == "__main__":
    cities = build_graph("city_population.txt", "road_network.txt")

    print("Task 2: graph adjacency list")
    for city in cities:
        names = []
        for neighbor in city.neighbors:
            names.append(neighbor.name)
        print(city.name, "population: ", city.population,"neighbors: ", names )

    print("Task 3: number of islands ->", count_num_islands(cities))

    print("Task 4: population of different isalnds")
    list_population = count_island_population(cities)
    for i in range(len(list_population)):
        print(list_population[i])

    print("Task 5: minimum distance")
    a = cities[0]
    for b in cities[1:]:
        print(a.name, "->", b.name, ":", min_distance(a, b))


