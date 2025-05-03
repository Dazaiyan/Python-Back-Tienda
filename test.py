import pytest
import requests
import json
from app import app  # Importa tu aplicación Flask

# Configuración para pruebas
BASE_URL = "http://localhost:5000/graphql"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_obtener_productos(client):
    """Prueba que la consulta de productos devuelva datos válidos"""
    query = """
    query {
        productos {
            id
            nombre
            precio
        }
    }
    """
    response = client.post("/graphql", json={"query": query})
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert "productos" in data["data"]
    assert len(data["data"]["productos"]) > 0
    assert all("nombre" in p for p in data["data"]["productos"])

   

def test_modificar_stock(client):
    """Prueba la mutación para modificar stock"""
    mutation = """
    mutation {
        modificarStock(id: 1, cantidad: -2) {
            nombre
            stock
            disponible
        }
    }
    """
    response = client.post("/graphql", json={"query": mutation})
    data = json.loads(response.data)
    producto = data["data"]["modificarStock"]
    
    assert response.status_code == 200
    assert producto["nombre"] == "Camiseta Blanca Esencial"
    assert producto["stock"] == 8  # Asumiendo stock inicial de 10
    
    # Prueba que disponible se actualice correctamente
    mutation_agotar = """
    mutation {
        modificarStock(id: 1, cantidad: -8) {
            stock
            disponible
        }
    }
    """
    response = client.post("/graphql", json={"query": mutation_agotar})
    data = json.loads(response.data)
    assert data["data"]["modificarStock"]["disponible"] == False

def test_stock_no_negativo(client):
    """Prueba que el stock no pueda ser negativo"""
    mutation = """
    mutation {
        modificarStock(id: 2, cantidad: -999) {
            stock
            disponible
        }
    }
    """
    response = client.post("/graphql", json={"query": mutation})
    data = json.loads(response.data)
    
    assert data["data"]["modificarStock"]["stock"] == 0
    assert data["data"]["modificarStock"]["disponible"] == False

