# SAMUEL MARTINEZ NC 0096
# EJEMPLO 1: IMAGEN ORIGINAL Y ESPECTRO DE FRECUENCIA
# ARCHIVO: ejemplo1-espectro-0096.py
# =====================================================
import os
import importlib.util
import matplotlib.pyplot as plt

# Importar funciones-frecuencia-0096.py (soporta guiones medios en el nombre)
ruta_mod = os.path.join(os.path.dirname(os.path.abspath(__file__)), "funciones-frecuencia-0096.py")
spec = importlib.util.spec_from_file_location("funciones_frecuencia_0096", ruta_mod)
ff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ff)

cargar_imagen = ff.cargar_imagen
obtener_espectro = ff.obtener_espectro
guardar_grafica = ff.guardar_grafica

# 1. Cargar la imagen
imagen = cargar_imagen("guitarra1.png")

# 2. Calcular el espectro de frecuencia
espectro = obtener_espectro(imagen)

# 3. Mostrar dimensiones en consola
print("--- EJEMPLO 1 ---")
print("Imagen guitarra1.png cargada.")
print(f"Dimensiones: Alto={imagen.shape[0]}, Ancho={imagen.shape[1]}")

# 4. Crear la figura con 2 subgráficas (1 fila, 2 columnas)
figura, ejes = plt.subplots(1, 2, figsize=(12, 6))

# 5. Mostrar imagen original
ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original (Dominio Espacial)")
ejes[0].axis("off")

# 6. Mostrar espectro de frecuencia
ejes[1].imshow(espectro, cmap="gray")
ejes[1].set_title("Espectro de Frecuencia (Dominio de Frecuencia)")
ejes[1].axis("off")

plt.tight_layout()

# 7. Guardar y mostrar
guardar_grafica(figura, "01_imagen_y_espectro.png")
plt.show()
print("SAMUEL MARTINEZ NC 0096")