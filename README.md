# Calzado Bless - Tienda Online

## Introducción

**Calzado Bless** es una página web que presenta una tienda online de calzado. Esta plataforma permite a los usuarios ver un catálogo completo de zapatos, sandalias y calzado deportivo de diferentes categorías (hombres, mujeres, niños y niñas), agregar productos al carrito de compras y gestionar sus compras de manera sencilla.

La página está diseñada para ofrecer una experiencia de compra cómoda y profesional, donde los clientes pueden navegar por diferentes tipos de calzado, ver detalles de cada producto y realizar compras de forma intuitiva desde cualquier dispositivo (computadora, tablet o celular).

## Despliegue en Render.com con Flask

### ¿Qué es Render.com?

**Render.com** es un servicio en la nube que permite poner páginas web en línea de manera fácil y gratuita. Es como un "hosting" moderno que hace que tu página web esté disponible en internet para que cualquier persona pueda visitarla desde cualquier lugar del mundo, simplemente escribiendo una dirección web en su navegador.

### ¿Cómo funciona en este proyecto?

Este proyecto utiliza **Flask**, que es una tecnología que permite crear páginas web dinámicas. Cuando se sube el proyecto a Render.com:

1. **Detección automática**: Render reconoce que es un proyecto Flask al encontrar el archivo `requirements.txt` (que lista las herramientas necesarias) y `app.py` (el archivo principal).

2. **Configuración automática**: El servicio instala automáticamente todas las herramientas necesarias y configura el servidor para que la página funcione correctamente.

3. **Generación del enlace**: Una vez configurado, Render proporciona un enlace público (como `https://tu-tienda.onrender.com`) que permite acceder a la página desde cualquier navegador.

### Acceso al sitio

Una vez publicado en Render.com, la página estará disponible las 24 horas del día a través del enlace proporcionado por el servicio, permitiendo que los clientes puedan visitar la tienda en cualquier momento.

## Funcionalidades principales

### Para los clientes:
- **Catálogo de productos**: Visualización de todos los tipos de calzado disponibles con imágenes de alta calidad
- **Categorías organizadas**: Calzado separado por categorías (Elegante, Hombre, Mujer, Niños, Niñas, Sandalias)
- **Carrito de compras**: Agregar y eliminar productos del carrito de manera fácil
- **Diseño responsivo**: La página se adapta perfectamente a celulares, tablets y computadoras
- **Interfaz intuitiva**: Navegación sencilla y clara para usuarios de todas las edades
- **Información de contacto**: Página dedicada para comunicarse con la tienda

### Para el administrador:
- **Gestión de productos**: Control total sobre el catálogo de productos
- **Actualizaciones fáciles**: Posibilidad de agregar nuevos productos modificando archivos
- **Mantenimiento sencillo**: Estructura organizada que facilita futuras mejoras

### Origen de los recursos utilizados:

Es importante aclarar que este proyecto fue desarrollado utilizando recursos existentes que fueron adaptados y personalizados:

- **Diseño base**: El diseño inicial se descargó de una página web externa y se guardó en el computador como punto de partida.
- **Adaptación personalizada**: Ese diseño se modificó completamente y se adaptó basándose en otras referencias para ajustarse a las necesidades específicas del proyecto.
- **Bootstrap**: Framework de diseño obtenido de fuentes externas para crear interfaces modernas y responsivas.
- **Iconos y elementos gráficos**: Recursos visuales tomados de bibliotecas públicas y sitios especializados.
- **Plantillas de referencia**: Se consultaron diferentes fuentes para mejorar la estructura y funcionalidad.

## Tecnologías utilizadas

- **Flask**: Tecnología de servidor que permite crear páginas web dinámicas y manejar las funcionalidades del carrito de compras.
- **HTML/CSS**: Lenguajes para crear la estructura visual y el diseño de la página web.
- **Bootstrap**: Framework de diseño obtenido de fuentes externas que facilita crear interfaces profesionales y responsivas.
- **JavaScript**: Permite las interacciones dinámicas como agregar productos al carrito y efectos visuales.
- **Render.com**: Plataforma en la nube que permite publicar la página web para que esté disponible en internet.
- **WebP**: Formato de imágenes optimizado que hace que las fotos de productos carguen más rápido.

## Proceso de desarrollo

### Punto de partida
El desarrollo comenzó con una **plantilla descargada** de una página web existente que sirvió como base inicial. Esta plantilla se guardó en el computador y se usó como fundamento para el proyecto.

### Personalización y adaptación
- **Modificación del diseño**: La plantilla original se modificó completamente para adaptarla a las necesidades específicas de una tienda de calzado.
- **Integración de referencias**: Se consultaron múltiples fuentes y referencias para mejorar tanto el diseño como la funcionalidad.
- **Ajustes de usabilidad**: Se realizaron mejoras en la navegación, organización de productos y experiencia del usuario.
- **Optimizaciones técnicas**: Se implementaron mejoras en velocidad de carga, adaptación móvil y funcionalidades del carrito.

### Resultado final
El producto final es una página web completamente personalizada que, aunque partió de una base externa, fue transformada para crear una experiencia única y profesional para la tienda Calzado Bless.

## Estructura del proyecto

```
calzado-bless/
├── app.py                  # Archivo principal que controla toda la página web
├── requirements.txt        # Lista de herramientas necesarias para que funcione
├── README.md              # Este archivo con la documentación
│
├── templates/             # Carpeta con las páginas web
│   ├── index.html         # Página principal con el catálogo
│   └── contacto.html      # Página de contacto
│
└── static/               # Carpeta con recursos visuales
    ├── css/              # Archivos de diseño y colores
    │   ├── main.css      # Estilos principales
    │   ├── components.css # Estilos de componentes específicos
    │   └── responsive.css # Adaptación para móviles y tablets
    │
    ├── favicon/          # Icono que aparece en la pestaña del navegador
    │   └── favicon.ico
    │
    ├── logo/            # Logotipos de la tienda
    │   ├── logo.webp
    │   └── logo2.webp
    │
    └── zapatos/         # Imágenes de todos los productos
        ├── Elegante.webp
        ├── hombre.webp
        ├── niña.webp
        ├── Zapato_abierto.webp
        └── ... (más imágenes de productos)
```

### Explicación de cada parte:

- **app.py**: Es el "cerebro" de la página. Controla qué se muestra cuando alguien visita la tienda y maneja las funciones del carrito de compras.

- **templates/**: Contiene las páginas que ven los usuarios. Como tener diferentes "páginas" de un libro, cada archivo HTML es una sección diferente de la tienda.

- **static/css/**: Son los archivos que definen cómo se ve la página (colores, tamaños, disposición de elementos). Es como el "diseñador" que hace que todo se vea bonito y organizado.

- **static/zapatos/**: Almacena todas las fotografías de los productos. Cada imagen está optimizada para cargar rápido sin perder calidad.

- **static/logo/ y favicon/**: Contienen los elementos de marca de la tienda (logos e íconos).

## Uso de la página

### Para visitantes y clientes:

1. **Acceder al sitio**: Visitar la dirección web proporcionada por Render.com desde cualquier navegador.

2. **Navegar el catálogo**: 
   - Ver todos los productos en la página principal
   - Filtrar por categorías (Elegante, Hombre, Mujer, Niños, etc.)
   - Observar las imágenes y detalles de cada producto

3. **Realizar compras**:
   - Hacer clic en "Agregar al carrito" en los productos deseados
   - Ver el carrito de compras con todos los productos seleccionados
   - Eliminar productos del carrito si es necesario
   - Proceder con el proceso de compra

4. **Contactar la tienda**:
   - Ir a la página de "Contacto"
   - Llenar el formulario con consultas o pedidos especiales
   - Enviar mensajes directamente a los administradores

### Para administradores:

1. **Gestionar productos**: Agregar nuevas imágenes a la carpeta `static/zapatos/` para incluir nuevos productos.

2. **Actualizar información**: Modificar textos, precios o descripciones editando los archivos correspondientes.

3. **Revisar mensajes**: Verificar los mensajes de contacto enviados por los clientes a través del formulario.

4. **Monitorear el sitio**: Usar las herramientas de Render.com para ver estadísticas de visitas y rendimiento.

---

*Esta página web está diseñada para ser fácil de usar, rápida de cargar y accesible desde cualquier dispositivo, proporcionando una experiencia de compra profesional y confiable.*




