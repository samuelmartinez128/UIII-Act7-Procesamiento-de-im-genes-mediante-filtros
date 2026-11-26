# SAMUEL MARTINEZ NC 0096
# EJEMPLO 3: SOBEL Y EN EL DOMINIO DE LA FRECUENCIA
# ARCHIVO: ejemplo3-sobel-y-0096.py
# =====================================================
import os
import importlib.util
import numpy as np
import matplotlib.pyplot as plt

# Importar funciones-frecuencia-0096.py (soporta guiones medios en el nombre)
ruta_mod = os.path.join(os.path.dirname(os.path.abspath(__file__)), "funciones-frecuencia-0096.py")
spec = importlib.util.spec_from_file_location("funciones_frecuencia_0096", ruta_mod)
ff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ff)

cargar_imagen = ff.cargar_imagen
obtener_espectro = ff.obtener_espectro
aplicar_filtro_frecuencia = ff.aplicar_filtro_frecuencia
normalizar_visualizacion = ff.normalizar_visualizacion
guardar_grafica = ff.guardar_grafica

# 1. Cargar imagen original
imagen = cargar_imagen("guitarra1.png")

# 2. Crear kernel Sobel Y (Detecta cambios verticales -> resalta bordes horizontales)
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# 3. Aplicar Sobel Y en el dominio de la frecuencia
resultado_y = aplicar_filtro_frecuencia(imagen, sobel_y)

# 4. Calcular el espectro de la respuesta filtrada
espectro_y = obtener_espectro(resultado_y)

# 5. Normalizar la respuesta para visualizarla
imagen_y_normalizada = normalizar_visualizacion(resultado_y)

# 6. Mostrar resultados
figura, ejes = plt.subplots(1, 3, figsize=(15, 5))

ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original")
ejes[0].axis("off")

ejes[1].imshow(espectro_y, cmap="gray")
ejes[1].set_title("Espectro después de Sobel Y")
ejes[1].axis("off")

ejes[2].imshow(imagen_y_normalizada, cmap="gray")
ejes[2].set_title("Respuesta Sobel Y (Bordes Horizontales)")
ejes[2].axis("off")

plt.tight_layout()
guardar_grafica(figura, "03_sobel_y.png")
plt.show()
print("SAMUEL MARTINEZ NC 0096")
