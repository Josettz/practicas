def jugar_ronda(arma):
    print("=== Comprando armamento ===")
    
    # Esta es nuestra función "de bolsillo". 
    # Solo existe y funciona MIENTRAS estemos dentro de jugar_ronda.
    def recargar_arma():
        print(f"Sonido de recarga: ¡Clack, clack! La {arma} está lista.")
        
    # Aquí la función principal decide USAR su herramienta de bolsillo
    recargar_arma()
    
    print("¡Muros caídos, a pelear!")

# -----------------------------------------
# Ahora intentamos ejecutar el código en la vida real:

jugar_ronda("Vandal")