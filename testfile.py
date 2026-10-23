from hw4 import build_graph, City

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