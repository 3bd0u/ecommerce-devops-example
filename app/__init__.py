from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Bienvenue sur PIO E-commerce"}

@app.route('/products')
def list_products():
    return {"products": ["Produit A", "Produit B", "Produit C"]}

@app.route('/order', methods=['POST'])
def order():
    return {"status": "Commande reçue"}, 201
