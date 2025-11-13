from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur l’API E-commerce PIO 🚀",
        "status": "running"
    })

@app.route('/products')
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Smartphone", "price": 800},
        {"id": 3, "name": "Casque Bluetooth", "price": 150}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
