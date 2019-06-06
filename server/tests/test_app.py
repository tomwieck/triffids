import os
import tempfile
import sys
import json

import pytest

from triffidsapi.app import create_app
app = create_app()

# def setup(self):
#     self.app_context = app.app_context()
#     self.app_context.push()


# def tearDown(self):
#     self.app_context.pop()


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_client_exists(client):
    s = client.get('/api/v1/')
    assert b'Hello, World!' in s.data


def test_get_all_park_names(client):
    js = client.get('/api/v1/parks')
    data = json.loads(js.data)
    assert 'ADELPL' == data[0]['id']


def test_client_get_park(client):
    js = client.get('/api/v1/parks/VICTPA')
    data = json.loads(js.data)
    assert 'Victoria Park' == data['siteName']


def test_client_get_nearest_parks(client):
    js = client.get('/api/v1/parks/loc?lat=51.44&lng=-2.587&radius=600')
    data = json.loads(js.data)
    print(data)
    assert 'Victoria Park' == data[0]['siteName']


def test_client_get_trees(client):
    js = client.get('/api/v1/trees/VICTPA')
    data = json.loads(js.data)
    assert len(data) == 581


def test_client_get_trees_by_species(client):
    js = client.get('/api/v1/trees/VICTPA?latinCode=QURO')
    data = json.loads(js.data)
    assert len(data) == 44


def test_client_get_trees_by_location(client):
    js = client.get('/api/v1/trees/loc?lat=51.44&lng=-2.587&radius=500')
    data = json.loads(js.data)
    assert len(data) == 836


def test_client_get_tree_by_id(client):
    js = client.get('/api/v1/trees?id=ec86bf43c7da17c479f9252e6bbcc8d6ef544a00')
    data = json.loads(js.data)
    assert data == {'error': 'Not found'}


def test_client_get_benches(client):
    js = client.get('/api/v1/benches/loc?lat=51.44&lng=-2.587&radius=500')

    data = json.loads(js.data)
    assert data[0]['id'] == 7347

