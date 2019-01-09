import os
import tempfile
import sys

import pytest

import app


@pytest.fixture
def client():
    yield app


def test_client_exists(client):
    s = client.index()
    assert 'Hello, World!' in s


def test_client_get_park(client):
    js = client.parks.getPark('VICTPA')
    assert js[0]['id'] == 'VICTPA'
