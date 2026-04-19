import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt


datos_tienda = {
    "ID_Producto": ["NX-01", "NX-02", "NX-03", "NX-04", "NX-05"],
    "Nombre": ["RTX 3060", "Ryzen 7 5700G", "RAM 16GB", "SSD 1TB", "Fuente 650W"],
    "Precio": [300.0, None, 45.0, None, 60.0],  
    "Stock": [10, 5, None, 20, None]    
}


df = pd.DataFrame(datos_tienda)

msno.matrix(df)


plt.show()