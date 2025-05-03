from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
from ariadne import QueryType, MutationType, make_executable_schema, graphql_sync, gql

app = Flask(__name__)
CORS(app)  


productos = [
    {
        "id": 1,
        "nombre": "Camiseta Blanca Esencial",
        "precio": 29.99,
        "stock": 10,
        "disponible": True
    },
    {
        "id": 2,
        "nombre": "Jeans Corte Clásico",
        "precio": 89.99,
        "stock": 5,
        "disponible": True
    },
    {
        "id": 3,
        "nombre": "Vestido Minimalista",
        "precio": 59.99,
        "stock": 0,
        "disponible": False
    },
    {
        "id": 4,
        "nombre": "Chaqueta Urbana",
        "precio": 129.99,
        "stock": 2,
        "disponible": True
    },
    {
        "id": 5,
        "nombre": "Zapatillas Urbanas",
        "precio": 79.99,
        "stock": 8,
        "disponible": True
    }
]


# Esquema GraphQL
type_defs = gql("""
    type Producto {
        id: ID!
        nombre: String!
        precio: Float!
        stock: Int!
        disponible: Boolean!
    }

    type Query {
        productos: [Producto!]!
    }

    type Mutation {
        modificarStock(id: ID!, cantidad: Int!): Producto
    }
""")

query = QueryType()
mutation = MutationType()

@query.field("productos")
def get_productos(*_):
    return productos

@mutation.field("modificarStock")
def modificar_stock(_, info, id, cantidad):
    for p in productos:
        if p["id"] == int(id):
            p["stock"] += cantidad
            if p["stock"] <= 0:
                p["stock"] = 0
                p["disponible"] = False
            else:
                p["disponible"] = True
            return p
    return None

schema = make_executable_schema(type_defs, query, mutation)

@app.route("/graphql", methods=["GET", "POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result)

# Interfaz de Apollo Sandbox
@app.route("/")
def apollo_sandbox():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Apollo Sandbox</title>
        <script src="https://embeddable-sandbox.cdn.apollographql.com/_latest/embeddable-sandbox.umd.production.min.js"></script>
        <link rel="stylesheet" href="https://embeddable-sandbox.cdn.apollographql.com/_latest/embeddable-sandbox.css">
    </head>
    <body>
        <div id="sandbox" style="position: absolute; top: 0; right: 0; bottom: 0; left: 0;"></div>
        <script>
            new window.EmbeddedSandbox({
                target: '#sandbox',
                initialEndpoint: window.location.origin + '/graphql',
            });
        </script>
    </body>
    </html>
    """)


if __name__ == "__main__":
    app.run(debug=True)