import os
import tempfile
import sys
import json

import pytest

from app import app


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
    s = client.get('/')
    assert b'Hello, World!' in s.data


def test_get_all_park_names(client):
    js = client.get('/api/v1/parks')
    data = json.loads(js.data)
    assert 'CUMBBASO' == data[0]['id']


def test_client_get_park(client):
    js = client.get('/api/v1/parks/VICTPA')
    data = json.loads(js.data)
    assert 'Victoria Park' == data[0]['siteName']


def test_client_get_nearest_parks(client):
    js = client.get('/api/v1/parks/lat=51.44&lng=-2.587&radius=500')
    data = json.loads(js.data)
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
    js = client.get('/api/v1/trees/lat=51.44&lng=-2.587&radius=500')
    data = json.loads(js.data)
    assert len(data) == 10


def test_client_get_benches(client):
    js = client.get('/api/v1/benches/lat=51.44&lng=-2.587&radius=500')
    data = json.loads(js.data)
    assert data[0]['id'] == 7347
