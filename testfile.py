from hw4 import *
#https://chatgpt.com/share/6adc67e6-ce70-83e8-8bf0-c9c7d7695bae
def test_build_graph(tmp_path):
    pop = tmp_path / "pop.txt"
    pop.write_text("A: 100\nB: 200\n")

    road = tmp_path / "road.txt"
    road.write_text("A: B\n")

    cities = build_graph(pop, road)
    city_map = {c.name: c for c in cities}

    assert len(cities) == 2
    assert city_map["A"].population == 100
    assert city_map["B"] in city_map["A"].neighbors
    assert city_map["A"] in city_map["B"].neighbors



def connect(a, b):
    a.add_neighbor(b)
    b.add_neighbor(a)


def test_disconnected_islands():
    a = City("A", 10)
    b = City("B", 20)
    c = City("C", 30)
    connect(a, b)

    assert count_num_islands([a, b, c]) == 2


def test_island_populations():
    a = City("A", 10)
    b = City("B", 20)
    c = City("C", 5)
    connect(a, b)

    assert count_island_population([a, b, c]) == [30, 5]


def test_shortest_path():
    a = City("A", 1)
    b = City("B", 1)
    c = City("C", 1)
    d = City("D", 1)
    e = City("E", 1)

    connect(a, b)
    connect(b, d)
    connect(d, e)
    connect(a, c)
    connect(c, e)

    assert min_distance(a, e) == 2


def test_unreachable_and_same_city():
    a = City("A", 10)
    b = City("B", 20)

    assert min_distance(a, b) == -1
    assert min_distance(a, a) == 0
