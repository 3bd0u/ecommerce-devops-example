import sys
import os
import pytest

# Ajoute la racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # <== importe l’objet Flask depuis __init__.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
