from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo de clientes y productos
clientes = [
    {"id": 1, "nombre_cliente": "Cliente 1", "productos": [
        {"id_producto": 101, "nombre": "Producto A", "precio": 19.990, "talla": "M", "enlace": "/productos/101", "cantidad_disponible": 10},
        {"id_producto": 102, "nombre": "Producto B", "precio": 29.000, "talla": "L", "enlace": "/productos/102", "cantidad_disponible": 5}
    ]},
    {"id": 2, "nombre_cliente": "Cliente 2", "productos": [
        {"id_producto": 103, "nombre": "Producto C", "precio": 39.900, "talla": "S", "enlace": "/productos/103", "cantidad_disponible": 20}
    ]},
    {"id": 3, "nombre_cliente": "Cliente 3", "productos": [
        {"id_producto": 104, "nombre": "Producto D", "precio": 49.000, "talla": "XL", "enlace": "/productos/104", "cantidad_disponible": 15},
        {"id_producto": 105, "nombre": "Producto E", "precio": 59.000, "talla": "M", "enlace": "/productos/105", "cantidad_disponible": 8}
    ]},
    {"id": 4, "nombre_cliente": "Cliente 4", "productos": [
        {"id_producto": 106, "nombre": "Producto F", "precio": 69.000, "talla": "L", "enlace": "/productos/106", "cantidad_disponible": 12}
    ]},
    {"id": 5, "nombre_cliente": "Cliente 5", "productos": [
        {"id_producto": 107, "nombre": "Producto G", "precio": 79.500, "talla": "S", "enlace": "/productos/107", "cantidad_disponible": 30},
        {"id_producto": 108, "nombre": "Producto H", "precio": 89.000, "talla": "XL", "enlace": "/productos/108", "cantidad_disponible": 25}
    ]},
    {"id": 6, "nombre_cliente": "Cliente 6", "productos": [
        {"id_producto": 109, "nombre": "Producto I", "precio": 99.500, "talla": "M", "enlace": "/productos/109", "cantidad_disponible": 18}
    ]},
    {"id": 7, "nombre_cliente": "Cliente 7", "productos": [
        {"id_producto": 110, "nombre": "Producto J", "precio": 19.000, "talla": "L", "enlace": "/productos/110", "cantidad_disponible": 10},
        {"id_producto": 111, "nombre": "Producto K", "precio": 119.200, "talla": "S", "enlace": "/productos/111", "cantidad_disponible": 15}
    ]},
    {"id": 8, "nombre_cliente": "Cliente 8", "productos": [
        {"id_producto": 112, "nombre": "Producto L", "precio": 100.000, "talla": "M", "enlace": "/productos/112", "cantidad_disponible": 22}
    ]},
    {"id": 9, "nombre_cliente": "Cliente 9", "productos": [
        {"id_producto": 113, "nombre": "Producto M", "precio": 139.500, "talla": "XL", "enlace": "/productos/113", "cantidad_disponible": 28},
        {"id_producto": 114, "nombre": "Producto N", "precio": 149.000, "talla": "S", "enlace": "/productos/114", "cantidad_disponible": 10}
    ]},
    {"id": 10, "nombre_cliente": "Cliente 10", "productos": [
        {"id_producto": 115, "nombre": "Producto O", "precio": 59.500, "talla": "L", "enlace": "/productos/115", "cantidad_disponible": 17}
    ]},
    {"id": 11, "nombre_cliente": "Cliente 11", "productos": [
        {"id_producto": 116, "nombre": "Producto P", "precio": 169.000, "talla": "M", "enlace": "/productos/116", "cantidad_disponible": 20},
        {"id_producto": 117, "nombre": "Producto Q", "precio": 79.000, "talla": "XL", "enlace": "/productos/117", "cantidad_disponible": 12}
    ]},
    {"id": 12, "nombre_cliente": "Cliente 12", "productos": [
        {"id_producto": 118, "nombre": "Producto R", "precio": 189.000, "talla": "S", "enlace": "/productos/118", "cantidad_disponible": 8}
    ]},
    {"id": 13, "nombre_cliente": "Cliente 13", "productos": [
        {"id_producto": 119, "nombre": "Producto S", "precio": 199.000, "talla": "L", "enlace": "/productos/119", "cantidad_disponible": 25},
        {"id_producto": 120, "nombre": "Producto T", "precio": 49.000, "talla": "M", "enlace": "/productos/120", "cantidad_disponible": 14}
    ]},
    {"id": 14, "nombre_cliente": "Cliente 14", "productos": [
        {"id_producto": 121, "nombre": "Producto U", "precio": 49.000, "talla": "XL", "enlace": "/productos/121", "cantidad_disponible": 18}
    ]},
    {"id": 15, "nombre_cliente": "Cliente 15", "productos": [
        {"id_producto": 122, "nombre": "Producto V", "precio": 120.000, "talla": "S", "enlace": "/productos/122", "cantidad_disponible": 30}
    ]}
]

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    return jsonify(clientes)

@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

@app.route('/clientes/<int:id_cliente>/productos/<int:id_producto>', methods=['GET'])
def obtener_producto_cliente(id_cliente, id_producto):
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if cliente:
        producto = next((p for p in cliente["productos"] if p["id_producto"] == id_producto), None)
        if producto:
            return jsonify(producto)
        else:
            return jsonify({"mensaje": "Producto no encontrado"}), 404
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True,port=8000)
