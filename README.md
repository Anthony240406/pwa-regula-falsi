# PWA Regula Falsi

Aplicación Web Progresiva (PWA) que implementa el método numérico **Regula Falsi modificado (Método de Illinois)** para calcular raíces cuadradas. La aplicación permite calcular la raíz cuadrada de cualquier número mediante un método iterativo, mostrando una tabla detallada con todas las iteraciones del algoritmo.

## Características

- **Progressive Web App (PWA)**: Instalable en dispositivos móviles y escritorio
- **Funcionamiento offline**: Service Worker para cachear recursos
- **Método Regula Falsi modificado (Illinois)**: Optimización del método clásico para evitar estancamiento
- **Interfaz intuitiva**: Diseño responsive y moderno
- **Tabla de iteraciones**: Visualización detallada de cada paso del algoritmo
- **Backend API REST**: Servidor Flask con endpoint para cálculos
- **Configuración de precisión**: Control del error mediante exponente (ε = 10⁻ˣ)

## Tecnologías

### Backend
- **Python 3.10**
- **Flask**: Framework web para la API
- **Flask-CORS**: Manejo de CORS para comunicación frontend-backend
- **Gunicorn**: Servidor WSGI para producción

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Diseño responsive y moderno
- **JavaScript (ES6+)**: Lógica de la aplicación
- **Service Worker**: Funcionalidad offline y cacheo
- **Web App Manifest**: Configuración PWA

## Estructura del Proyecto

```
pwa-regula-falsi/
├── Backend/
│   ├── app.py              # Aplicación Flask y endpoints API
│   ├── utils.py            # Implementación del algoritmo Regula Falsi
│   ├── requirements.txt    # Dependencias de Python
│   └── Procfile           # Configuración para despliegue (Render/Heroku)
│
├── frontend/
│   ├── index.html         # Página principal
│   ├── manifest.json      # Configuración PWA
│   ├── service-worker.js  # Service Worker para funcionalidad offline
│   ├── css/
│   │   └── styles.css     # Estilos de la aplicación
│   ├── js/
│   │   ├── app.js         # Lógica principal de la aplicación
│   │   └── api.js         # Comunicación con la API backend
│   └── images/
│       └── icons/         # Iconos para la PWA
│
└── generate_icons.py      # Script para generar iconos de diferentes tamaños
```

## Instalación y Configuración

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno con soporte para Service Workers

### Backend
1. **Navegar al directorio del backend:**
   ```bash
   cd Backend
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv

   # En Windows
   venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor:**
   ```bash
   python app.py
   ```
   
   El servidor estará disponible en `http://localhost:5000`

### Frontend
El frontend es una aplicación estática que puede servirse con cualquier servidor web. Opciones:

#### Opción 1: Python Simple HTTP Server
```bash
cd frontend
python -m http.server 8000
```

#### Opción 2: Node.js http-server
```bash
cd frontend
npx http-server -p 8000
```

#### Opción 3: Servidor web de tu elección
Cualquier servidor web (Apache, Nginx, etc.) puede servir los archivos estáticos del directorio `frontend/`.

**⚠️ Nota:** Si ejecutas el frontend en un puerto diferente al backend (5000), asegúrate de actualizar la URL del API en `frontend/js/api.js`.

## Uso

1. **Abrir la aplicación** en el navegador
2. **Ingresar el número N** del cual se desea calcular la raíz cuadrada
3. **Ingresar el exponente** para definir la precisión (ε = 10⁻ˣ)
   - Ejemplo: exponente = 6 → ε = 10⁻⁶ = 0.000001
4. **Hacer clic en "Calcular"**
5. **Visualizar los resultados:**
   - Raíz aproximada en la parte superior
   - Tabla detallada con todas las iteraciones mostrando:
     - Número de iteración (n)
     - Extremos del intervalo (a, b)
     - Aproximación actual (xₙ)
     - Valor de la función f(xₙ)
     - Salto entre iteraciones |xₙ - xₙ₋₁|

### Ejemplo

Calcular √25 con precisión de 10⁻⁶:
- N: `25`
- Exponente: `6`
- Resultado esperado: `≈ 5.000000`

## Algoritmo: Regula Falsi Modificado (Método de Illinois)

El método implementado es una variante mejorada del método Regula Falsi clásico que soluciona el problema de convergencia lenta cuando uno de los extremos se mantiene fijo durante varias iteraciones.

### Características del algoritmo:

1. **Intervalo inicial**: Se calcula automáticamente basándose en `[floor(√N), ceil(√N)]` o `[0, max(1, N)]`

2. **Modificación de Illinois**: 
   - Si un extremo (a o b) queda fijo dos veces consecutivas, se divide su peso por 2
   - Esto "inclina" la recta y acelera la convergencia

3. **Criterio de parada**: 
   - El algoritmo termina cuando |xₙ - xₙ₋₁| < ε
   - Máximo de 100 iteraciones

4. **Función objetivo**: f(x) = x² - N

## Despliegue

### Backend en Render.com

### Frontend

El frontend puede desplegarse en cualquier servicio de hosting estático:
- **Netlify**
- **Vercel**
- **GitHub Pages**
- **Firebase Hosting**

**Importante**: Actualizar la URL del API en `frontend/js/api.js` con la URL de tu backend desplegado.

## Instalación como PWA

La aplicación puede instalarse como una PWA en dispositivos móviles y de escritorio:

1. Abrir la aplicación en el navegador
2. Buscar el botón "Instalar" o "Add to Home Screen" en el navegador
3. Confirmar la instalación
4. La aplicación estará disponible como una app independiente

## Configuración Avanzada

### Generar Iconos

Para generar iconos de diferentes tamaños a partir de una imagen original:

```bash
pip install Pillow
python generate_icons.py
```

La imagen original debe estar en `frontend/images/icons/original.png` (recomendado: 1024×1024px).

### Modificar la Precisión

Editar el valor de `max_iter` en `Backend/utils.py` para cambiar el número máximo de iteraciones permitidas.

### Cambiar la Función Objetivo

Modificar la función `f(x, N)` en `Backend/utils.py` para cambiar la función cuya raíz se desea calcular.

