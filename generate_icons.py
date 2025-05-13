from PIL import Image
import os

# 1. Ruta a tu imagen original (1024×1024)
src = os.path.join("frontend", "images", "icons", "original.png")

# 2. Directorio de salida (mismo icons/)
out_dir = os.path.join("frontend", "images", "icons")

# Asegura que exista la carpeta
os.makedirs(out_dir, exist_ok=True)

# 3. Abre la imagen
img = Image.open(src).convert("RGBA")

# 4. Genera cada icono
for size in (192, 512):
    icon = img.resize((size, size), Image.Resampling.LANCZOS)
    dest = os.path.join(out_dir, f"icon-{size}.png")
    icon.save(dest)
    print(f"Guardado {dest} ({size}×{size})")
