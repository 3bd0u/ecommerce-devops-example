def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenue" in response.data

def test_list_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert "products" in data

def test_order(client):
    response = client.post('/order', json={"item": "Produit A"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["status"] == "Commande reçue"
