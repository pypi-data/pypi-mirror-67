# Importing libraries
# import pytest library for testing
import pytest

# import pandas for data handling
import pandas as pd

# import numpy for math
import numpy as np

# import simpy for simulation environment
import simpy

# import networkx for graphs
import networkx as nx

# import spatial libraries
import pyproj
import shapely.geometry

# import date and time handling
import datetime

# import random for random selection
import random

# tranport network analysis package
import opentnsim.core as core
import opentnsim.model as model


"""
Testing the VesselGenerator class and Simulation class of model.py
"""


@pytest.fixture()
def vessel_database():
    return pd.read_csv("tests/vessels/vessels.csv")


@pytest.fixture()
def vessel_type():
    vessel = type(
        "Vessel",
        (
            core.Identifiable,
            core.Movable,
            core.HasContainer,
            core.VesselProperties,
            core.HasResource,
            core.Routeable,
        ),
        {},
    )

    return vessel


@pytest.fixture()
def graph():
    FG = nx.Graph()

    node_1 = {"Name": "Node 1", "Geometry": shapely.geometry.Point(4.49540, 51.905505)}
    node_2 = {"Name": "Node 2", "Geometry": shapely.geometry.Point(4.48935, 51.907995)}
    node_3 = {"Name": "Node 3", "Geometry": shapely.geometry.Point(4.48330, 51.910485)}
    nodes = [node_1, node_2, node_3]

    for node in nodes:
        FG.add_node(
            node["Name"],
            geometry=node["Geometry"],
            Position=(node["Geometry"].x, node["Geometry"].y),
        )

    edges = [[node_1, node_2], [node_2, node_3]]
    for edge in edges:
        FG.add_edge(edge[0]["Name"], edge[1]["Name"], weight=1)

    return FG


"""
Actual testing starts below
"""


def test_make_vessel(vessel_database, vessel_type, graph):

    # Generate a path
    path = nx.dijkstra_path(graph, list(graph)[0], list(graph)[-1])
    env = simpy.Environment()
    env.FG = graph

    # Generate a vessel
    generator = model.VesselGenerator(vessel_type, vessel_database)
    generated_vessel = generator.generate(env, "Test vessel")

    # Make the test vessel
    random.seed(4)
    vessel_info = vessel_database.sample(n=1, random_state=int(1000 * random.random()))
    vessel_data = {}

    vessel_data["env"] = env
    vessel_data["name"] = "Test vessel"
    vessel_data["route"] = None
    vessel_data["geometry"] = None

    for key in vessel_info:
        if key == "vessel_id":
            vessel_data["id"] = vessel_info[key].values[0]
        else:
            vessel_data[key] = vessel_info[key].values[0]

    test_vessel = vessel_type(**vessel_data)

    for key in generated_vessel.__dict__:
        if key != "container" or key != "resource":
            generated_vessel.__dict__[key] == test_vessel.__dict__[key]


def test_inter_arrival_times_markovian(vessel_database, vessel_type, graph):

    # Create a vessel generator
    generator = model.VesselGenerator(vessel_type, vessel_database)

    # Create a simulation object
    simulation_start = datetime.datetime(2019, 1, 1)
    sim = model.Simulation(simulation_start, graph)
    sim.add_vessels(
        origin=list(graph)[0], destination=list(graph)[-1], vessel_generator=generator
    )

    # Run the simulation
    sim.run(duration=100 * 24 * 60 * 60)

    # The default arrival times of vessels is 1 per hour
    inter_arrivals = []

    for i, _ in enumerate(sim.environment.vessels):
        if i > 0:
            inter_arrivals.append(
                sim.environment.vessels[i].log["Timestamp"][0]
                - sim.environment.vessels[i - 1].log["Timestamp"][0]
            )

    # Test if average inter_arrival time is indeed approximately 3600 seconds
    assert np.isclose(3600, np.mean(inter_arrivals).total_seconds(), rtol=0.01, atol=60)


def test_inter_arrival_times_uniform(vessel_database, vessel_type, graph):

    # Create a vessel generator
    generator = model.VesselGenerator(vessel_type, vessel_database)

    # Create a simulation object
    simulation_start = datetime.datetime(2019, 1, 1)
    sim = model.Simulation(simulation_start, graph)
    sim.add_vessels(
        origin=list(graph)[0],
        destination=list(graph)[-1],
        vessel_generator=generator,
        arrival_process="Uniform",
    )

    # Run the simulation
    sim.run(duration=100 * 24 * 60 * 60)

    # The default arrival times of vessels is 1 per hour
    inter_arrivals = []

    for i, _ in enumerate(sim.environment.vessels):
        if i > 0:
            inter_arrivals.append(
                sim.environment.vessels[i].log["Timestamp"][0]
                - sim.environment.vessels[i - 1].log["Timestamp"][0]
            )

    # Test if average inter_arrival time is indeed approximately 3600 seconds
    assert np.isclose(3600, np.mean(inter_arrivals).total_seconds(), rtol=0.01, atol=60)
