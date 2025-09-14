# Calzado Bless Puerto López 👟

Una página web moderna y funcional para la empresa **Calzado Bless Puerto López**, desarrollada con Flask (Python) y diseñada para mostrar información de la empresa, productos, proveedores y brindar una experiencia de usuario completa con formulario de contacto y chatbot interactivo.

## 🌟 Características

- **Página principal** con información completa de la empresa
- **Misión y visión** empresarial claramente presentadas
- **Catálogo de productos** organizados por categorías
- **Lista de proveedores** con información detallada
- **Formulario de contacto** funcional
- **Chatbot inteligente** que responde preguntas sobre la empresa
- **Diseño responsivo** que se adapta a dispositivos móviles
- **Promociones destacadas** (20% de descuento en segunda compra)

## 🚀 Tecnologías utilizadas

- **Backend**: Python 3.8+ con Flask
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Estilos**: CSS Grid y Flexbox para diseño responsivo
- **Iconos**: Font Awesome 6.0
- **Servidor de producción**: Gunicorn

## 📁 Estructura del proyecto

```
calzado-bless/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias Python
├── README.md          # Documentación del proyecto
├── templates/         # Plantillas HTML
│   ├── index.html     # Página principal
│   └── contacto.html  # Página de contacto
└── static/           # Archivos estáticos
    └── style.css     # Estilos CSS
```

## 🛠️ Instalación y configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Instalación local

1. **Clona el repositorio** (o descarga los archivos):
   ```bash
   git clone https://github.com/tu-usuario/calzado-bless.git
   cd calzado-bless
   ```

2. **Crea un entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```

5. **Abre tu navegador** y visita: `http://localhost:5000`

## 🌐 Despliegue en producción

### Opción 1: Render (Recomendado - Gratis)

1. **Crea una cuenta** en [Render.com](https://render.com)

2. **Conecta tu repositorio GitHub** al panel de Render

3. **Crea un nuevo Web Service** con estos ajustes:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3.8+

4. **Variables de entorno** (opcional):
   ```
   FLASK_ENV=production
   SECRET_KEY=tu_clave_secreta_aqui
   ```

5. **Despliega** y obtendrás una URL pública automáticamente

### Opción 2: Railway

1. **Crea una cuenta** en [Railway.app](https://railway.app)

2. **Conecta tu repositorio GitHub**

3. **Railway detectará automáticamente** que es una aplicación Flask

4. **Configura las variables de entorno** si es necesario

5. **Despliega** con un solo clic

### Opción 3: Heroku (Plan gratuito limitado)

1. **Instala Heroku CLI**

2. **Crea un archivo `Procfile`** en la raíz del proyecto:
   ```
   web: gunicorn app:app
   ```

3. **Despliega con comandos**:
   ```bash
   heroku login
   heroku create tu-app-calzado-bless
   git push heroku main
   heroku open
   ```

## 🤖 Funcionalidades del Chatbot

El chatbot integrado puede responder a las siguientes consultas:

- **Misión de la empresa**: Pregunta sobre "misión"
- **Visión empresarial**: Pregunta sobre "visión"
- **Descuentos y promociones**: Pregunta sobre "descuento" o "promoción"
- **Productos disponibles**: Pregunta sobre "productos" o "calzado"
- **Proveedores**: Pregunta sobre "proveedores" o "marcas"
- **Saludos y ayuda**: Responde a saludos y solicitudes de ayuda

### Ejemplos de preguntas:
- "¿Cuál es su misión?"
- "¿Tienen descuentos?"
- "¿Qué productos manejan?"
- "¿Cuáles son sus proveedores?"

## 📧 Configuración del formulario de contacto

El formulario de contacto actualmente almacena los mensajes en memoria. Para funcionalidad completa de email:

1. **Configura las variables de entorno**:
   ```python
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 587
   MAIL_USERNAME = 'tu-email@gmail.com'
   MAIL_PASSWORD = 'tu-contraseña-de-app'
   ```

2. **Modifica `app.py`** para enviar emails reales (código comentado incluido)

## 🎨 Personalización

### Cambiar colores y estilos

Edita `static/style.css` para personalizar:

- **Colores principales**: Variables CSS en la parte superior
- **Tipografías**: Cambiar `font-family` en el selector universal
- **Espaciados**: Modificar padding y margin según necesidad

### Agregar nuevas secciones

1. **Modifica `templates/index.html`** para agregar HTML
2. **Actualiza `static/style.css`** para los estilos
3. **Modifica `app.py`** si necesitas nueva funcionalidad backend

### Personalizar información de la empresa

Edita el diccionario `EMPRESA_INFO` en `app.py`:

```python
EMPRESA_INFO = {
    'nombre': 'Tu Empresa',
    'mision': 'Tu misión...',
    'vision': 'Tu visión...',
    # ... más campos
}
```

## 🔧 Desarrollo

### Estructura de rutas

- `/` - Página principal
- `/contacto` - Página de contacto (GET/POST)
- `/chatbot` - API del chatbot (POST, JSON)

### Agregar nuevas rutas

```python
@app.route('/nueva-ruta')
def nueva_funcion():
    return render_template('nueva-plantilla.html')
```

### Debugging

Para desarrollo, la aplicación se ejecuta con `debug=True`. En producción, esto se desactiva automáticamente.

## 📱 Compatibilidad

- ✅ Chrome, Firefox, Safari, Edge (últimas versiones)
- ✅ Dispositivos móviles (responsive design)
- ✅ Tablets y dispositivos de tamaño medio
- ✅ Accesibilidad básica implementada

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes problemas con la instalación o despliegue:

1. **Revisa los logs** de tu plataforma de hosting
2. **Verifica las dependencias** en `requirements.txt`
3. **Asegúrate** de que Python 3.8+ esté instalado
4. **Consulta la documentación** de Flask: [Flask Documentation](https://flask.palletsprojects.com/)

## 🎯 Próximas mejoras

- [ ] Integración con base de datos para almacenar contactos
- [ ] Panel de administración
- [ ] Catálogo de productos con imágenes
- [ ] Sistema de inventario básico
- [ ] Integración con WhatsApp Business API
- [ ] Optimización SEO avanzada
- [ ] Analytics y métricas

