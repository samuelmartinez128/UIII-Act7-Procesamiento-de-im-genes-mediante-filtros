# SAMUEL MARTINEZ NC 0096
# EJEMPLO 4: MAGNITUD DEL GRADIENTE (SOBEL X + SOBEL Y)
# ARCHIVO: ejemplo4-magnitud-gradiente-0096.py
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

# 2. Definir kernels
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

# 3. Aplicar ambos filtros en frecuencia
resultado_x = aplicar_filtro_frecuencia(imagen, sobel_x)
resultado_y = aplicar_filtro_frecuencia(imagen, sobel_y)

# 4. Calcular la magnitud del gradiente: G = sqrt(Gx^2 + Gy^2)
# Nota: Usamos los resultados crudos (antes de normalizar) para la operación matemática correcta
magnitud_gradiente = np.sqrt(resultado_x**2 + resultado_y**2)

# 5. Normalizar todas las respuestas para visualización
img_x_norm = normalizar_visualizacion(resultado_x)
img_y_norm = normalizar_visualizacion(resultado_y)
img_mag_norm = normalizar_visualizacion(magnitud_gradiente)

# 6. Calcular espectros para visualización comparativa
espectro_x = obtener_espectro(resultado_x)
espectro_y = obtener_espectro(resultado_y)

# 7. Mostrar los 6 resultados en una cuadrícula de 2x3
figura, ejes = plt.subplots(2, 3, figsize=(18, 10))

# Fila 1: Imagen original y Espectros
ejes[0, 0].imshow(imagen, cmap="gray")
ejes[0, 0].set_title("1. Imagen Original")
ejes[0, 0].axis("off")

ejes[0, 1].imshow(espectro_x, cmap="gray")
ejes[0, 1].set_title("2. Espectro Sobel X")
ejes[0, 1].axis("off")

ejes[0, 2].imshow(espectro_y, cmap="gray")
ejes[0, 2].set_title("3. Espectro Sobel Y")
ejes[0, 2].axis("off")

# Fila 2: Respuestas espaciales y Magnitud
ejes[1, 0].imshow(img_x_norm, cmap="gray")
ejes[1, 0].set_title("4. Respuesta Sobel X (Verticales)")
ejes[1, 0].axis("off")

ejes[1, 1].imshow(img_y_norm, cmap="gray")
ejes[1, 1].set_title("5. Respuesta Sobel Y (Horizontales)")
ejes[1, 1].axis("off")

ejes[1, 2].imshow(img_mag_norm, cmap="gray")
ejes[1, 2].set_title("6. Magnitud del Gradiente (Todos los bordes)")
ejes[1, 2].axis("off")

plt.tight_layout()
guardar_grafica(figura, "04_comparacion_magnitud_gradiente.png")
plt.show()
print("SAMUEL MARTINEZ NC 0096")