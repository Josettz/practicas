import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# 1. Simulamos una tabla de tu inventario donde faltan datos (None)
datos_tienda = {
    "ID_Producto": ["NX-01", "NX-02", "NX-03", "NX-04", "NX-05"],
    "Nombre": ["RTX 3060", "Ryzen 7 5700G", "RAM 16GB", "SSD 1TB", "Fuente 650W"],
    "Precio": [300.0, None, 45.0, None, 60.0],  # Faltan 2 precios
    "Stock": [10, 5, None, 20, None]            # Faltan 2 datos de stock
}

# 2. Convertimos el diccionario en un "DataFrame" (una tabla de Pandas)
df = pd.DataFrame(datos_tienda)

# 3. ¡Magia! Generamos el gráfico de matriz de Missingno
msno.matrix(df)

# Mostramos el gráfico
plt.show()