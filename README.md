# 🚀 API GraphQL para Tienda - Backend

## 📋 Descripción

API GraphQL construida con Flask y Ariadne para gestionar productos de una tienda online. Incluye:

- Consulta de productos
- Modificación de stock
- Actualización automática de disponibilidad
- Interfaz GraphiQL integrada

## 🛠 Tecnologías

- **Python 3.8+**
- **Flask** (Servidor web)
- **Ariadne** (Implementación GraphQL)
- **GraphiQL** (Interfaz de consultas integrada)

## ⚙️ Configuración

### Requisitos previos

- Python 3.8 o superior instalado
- Pip (Gestor de paquetes Python)

### Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/backend-tienda.git
   cd backend-tienda
   ```

2. Crear y activar entorno virtual (recomendado):

   **Linux/Mac**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   **Windows**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Ejecución

Iniciar el servidor:

```bash
python app.py
```

El servidor estará disponible en:

[http://localhost:5000](http://localhost:5000)

## 📚 Esquema GraphQL

### Tipos

```graphql
type Producto {
  id: ID!
  nombre: String!
  precio: Float!
  stock: Int!
  disponible: Boolean!
}
```

### Consultas (Queries)

```graphql
type Query {
  productos: [Producto]!
  producto(id: ID!): Producto
}
```

### Mutaciones

```graphql
type Mutation {
  modificarStock(id: ID!, cantidad: Int!): Producto
}
```

## 🔍 Uso de la API

### Interfaz GraphiQL

Accede a la interfaz interactiva en:

[http://localhost:5000](http://localhost:5000)

### Ejemplos de consultas

**Obtener todos los productos:**

```graphql
query {
  productos {
    id
    nombre
    precio
    stock
    disponible
  }
}
```

**Obtener un producto específico:**

```graphql
query {
  producto(id: 2) {
    nombre
    precio
    disponible
  }
}
```

### Ejemplos de mutaciones

**Reducir stock:**

```graphql
mutation {
  modificarStock(id: 1, cantidad: -3) {
    nombre
    stock
    disponible
  }
}
```

**Aumentar stock:**

```graphql
mutation {
  modificarStock(id: 3, cantidad: 5) {
    nombre
    stock
    disponible
  }
}
```
