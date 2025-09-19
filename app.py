from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambiar en producción

# Datos de la empresa
EMPRESA_INFO = {
    'nombre': 'Calzado Bless Puerto López',
    'mision': 'Somos una empresa colombiana dedicada a la distribución de calzado de calidad, enfocada en productos cómodos que brinden salud a los pies y cumplan con estándares de excelencia.',
    'vision': 'Para el 2030 ser reconocida a nivel departamental como una de las más competitivas en el mercado local, ofreciendo una experiencia de compra excepcional.',
    'descuento': '20% de descuento en la segunda compra',
    'productos': 'Calzado de diferentes estilos para toda la familia',
    'proveedores': [
        'Estilos Chelita', 'Camary', 'Lesmar', 'Veras sport', 'Llanero Shoes',
        'Kanguro', 'Flexrun', 'Zapatillas Vanessa', 'Zapatillas Jose',
        'Chacon shoes', 'Petroleo', 'Merak', 'Nahomy', 'Manantial'
    ]
}

# Base de datos de productos con información completa y actualizada
PRODUCTOS_DB = {
    # Hombre
    'zapato_clasico_blanco': {
        'nombre': 'Zapato Clásico Blanco',
        'categoria': 'hombre',
        'precio': 150000,
        'color': 'blanco',
        'tallas': [38, 39, 40, 41, 42, 43, 44],
        'descripcion': 'Deportivo y cómodo para uso diario',
        'material': 'Cuero genuino',
        'imagen': 'hombre.webp',
        'palabras_clave': ['blanco', 'clasico', 'hombre', 'deportivo', 'comodo', 'diario']
    },
    'zapato_casual_negro': {
        'nombre': 'Zapato Casual Negro',
        'categoria': 'mujer',
        'precio': 199900,
        'color': 'negro',
        'tallas': [35, 36, 37, 38, 39, 40],
        'descripcion': 'Perfecto para actividades deportivas',
        'material': 'Sintético deportivo',
        'imagen': 'hombre2.webp',
        'palabras_clave': ['negro', 'casual', 'mujer', 'deportivo', 'actividades']
    },
    'zapato_deportivo_premium': {
        'nombre': 'Zapato Deportivo Premium',
        'categoria': 'hombre',
        'precio': 229900,
        'color': 'negro',
        'tallas': [38, 39, 40, 41, 42, 43, 44],
        'descripcion': 'Ideal para ocasiones especiales',
        'material': 'Cuero premium',
        'imagen': 'hombre3.webp',
        'palabras_clave': ['negro', 'deportivo', 'premium', 'hombre', 'especial', 'lujo']
    },
    'zapato_deportivo_mujer': {
        'nombre': 'Zapato Deportivo Mujer',
        'categoria': 'mujer',
        'precio': 199900,
        'color': 'multicolor',
        'tallas': [35, 36, 37, 38],
        'descripcion': 'Cómodo para el día a día',
        'material': 'Textil y cuero',
        'imagen': 'hombre4.webp',
        'palabras_clave': ['multicolor', 'negro', 'blanco', 'deportivo', 'mujer', 'comodo', 'diario']
    },
    'zapato_sport_azul': {
        'nombre': 'Zapato Sport Azul',
        'categoria': 'hombre',
        'precio': 219900,
        'color': 'azul',
        'tallas': [38, 39, 40, 41, 42],
        'descripcion': 'Estilo deportivo urbano',
        'material': 'Sintético',
        'imagen': 'hombre5.webp',
        'palabras_clave': ['azul', 'sport', 'hombre', 'urbano', 'moderno']
    },
    'zapato_urbano_rosa': {
        'nombre': 'Zapato Urbano Rosa',
        'categoria': 'mujer',
        'precio': 199900,
        'color': 'rosa',
        'tallas': [35, 36, 37, 38, 39],
        'descripcion': 'Moderno y versátil',
        'material': 'Cuero sintético',
        'imagen': 'hombre6.webp',
        'palabras_clave': ['rosa', 'urbano', 'mujer', 'moderno', 'versatil']
    },
    'zapato_executive_marron': {
        'nombre': 'Zapato Executive',
        'categoria': 'hombre',
        'precio': 239900,
        'color': 'multicolor',
        'tallas': [38, 39, 40, 41, 42],
        'descripcion': 'Para el profesional moderno',
        'material': 'Cuero ejecutivo',
        'imagen': 'hombre7.webp',
        'palabras_clave': ['multicolor', 'ejecutivo', 'hombre', 'profesional', 'trabajo']
    },
    'zapato_formal_marron': {
        'nombre': 'Zapato Formal Marrón',
        'categoria': 'elegante',
        'precio': 149900,
        'color': 'marrón',
        'tallas': [38, 39, 40, 41, 42, 43, 44],
        'descripcion': 'Zapato con partes de cuero y gamuza',
        'material': 'Cuero y gamuza',
        'imagen': 'Elegante2.webp',
        'palabras_clave': ['marron', 'formal', 'elegante', 'cuero', 'gamuza']
    },
    
    # Elegantes
    'zapato_elegante_clasico': {
        'nombre': 'Zapato Elegante Clásico',
        'categoria': 'elegante',
        'precio': 219900,
        'color': 'marrón',
        'tallas': [38, 39, 40, 41, 42],
        'descripcion': 'Sofisticación en cada paso',
        'material': 'Cuero de lujo',
        'imagen': 'Elegante.webp',
        'palabras_clave': ['marron', 'elegante', 'clasico', 'sofisticado', 'lujo']
    },
    'zapato_elegante_formal': {
        'nombre': 'Zapato Elegante Formal',
        'categoria': 'elegante',
        'precio': 249900,
        'color': 'marrón',
        'tallas': [38, 39, 40, 41, 42],
        'descripcion': 'Para ocasiones especiales',
        'material': 'Charol premium',
        'imagen': 'Elegante3.webp',
        'palabras_clave': ['marron', 'elegante', 'formal', 'especial', 'premium']
    },
    'zapato_elegante_marron': {
        'nombre': 'Zapato Elegante Marrón',
        'categoria': 'elegante',
        'precio': 239900,
        'color': 'marrón',
        'tallas': [38, 39, 40, 41, 42],
        'descripcion': 'Pureza y elegancia',
        'material': 'Cuero marrón',
        'imagen': 'Elegante4.webp',
        'palabras_clave': ['marron', 'elegante', 'pureza', 'moderno']
    },
    'zapato_elegante_luxury': {
        'nombre': 'Zapato Elegante Luxury',
        'categoria': 'elegante',
        'precio': 295500,
        'color': 'marrón',
        'tallas': [39, 40, 41, 42, 43],
        'descripcion': 'El máximo en elegancia',
        'material': 'Cuero italiano',
        'imagen': 'Elegante5.webp',
        'palabras_clave': ['marron', 'elegante', 'luxury', 'maximo', 'italiano']
    },
    'zapato_elegante_deluxe': {
        'nombre': 'Zapato Elegante Deluxe',
        'categoria': 'elegante',
        'precio': 199900,
        'color': 'marrón',
        'tallas': [38, 39, 40, 41, 42, 43],
        'descripcion': 'Calidad superior',
        'material': 'Cuero deluxe',
        'imagen': 'Elegante6.webp',
        'palabras_clave': ['marron', 'elegante', 'deluxe', 'superior', 'calidad']
    },
    
    # Infantiles
    'zapato_nina_rosa': {
        'nombre': 'Zapato Niña Rosa',
        'categoria': 'infantil',
        'precio': 75000,
        'color': 'rosa',
        'tallas': [21, 22, 23, 24, 25, 26, 27, 28],
        'descripcion': 'Dulce y cómodo para niñas',
        'material': 'Sintético infantil',
        'imagen': 'niña.webp',
        'palabras_clave': ['rosa', 'nina', 'infantil', 'dulce', 'comodo', 'niña']
    },
    'zapato_nina_colorido': {
        'nombre': 'Zapato Niña Colorido',
        'categoria': 'infantil',
        'precio': 68000,
        'color': 'multicolor',
        'tallas': [22, 23, 24, 25, 26, 27, 28, 29],
        'descripcion': 'Divertido y alegre',
        'material': 'Textil colorido',
        'imagen': 'niña2.webp',
        'palabras_clave': ['multicolor', 'nina', 'infantil', 'divertido', 'alegre', 'niña']
    },
    'zapato_nina_princess': {
        'nombre': 'Zapato Niña Princess',
        'categoria': 'infantil',
        'precio': 88000,
        'color': 'rosa',
        'tallas': [24, 25, 26, 27, 28, 29, 30],
        'descripcion': 'Para pequeñas princesas',
        'material': 'Sintético brillante',
        'imagen': 'niña3.webp',
        'palabras_clave': ['rosa', 'nina', 'princess', 'infantil', 'princesa', 'niña']
    },
    'zapato_nino_negro': {
        'nombre': 'Zapato Niño Negro',
        'categoria': 'infantil',
        'precio': 76000,
        'color': 'negro',
        'tallas': [23, 24, 25, 26, 27, 28, 29],
        'descripcion': 'Resistente y cómodo',
        'material': 'Sintético resistente',
        'imagen': 'niño.webp',
        'palabras_clave': ['negro', 'nino', 'infantil', 'resistente', 'comodo', 'niño']
    },
    'zapato_nino_principes': {
        'nombre': 'Zapato Niño Príncipes',
        'categoria': 'infantil',
        'precio': 75000,
        'color': 'marrón',
        'tallas': [25, 26, 27, 28, 29, 30],
        'descripcion': 'Para pequeños príncipes',
        'material': 'Deportivo infantil',
        'imagen': 'niño2.webp',
        'palabras_clave': ['marron', 'nino', 'principes', 'infantil', 'principe', 'niño']
    },
    
    # Calzado Abierto
    'sandalia_elegante': {
        'nombre': 'Sandalia Elegante',
        'categoria': 'abierto',
        'precio': 179900,
        'color': 'negro',
        'tallas': [35, 36, 37, 38, 39, 40],
        'descripcion': 'Frescas y cómodas',
        'material': 'Cuero transpirable',
        'imagen': 'Zapato_abierto.webp',
        'palabras_clave': ['negro', 'sandalia', 'abierto', 'elegante', 'fresco', 'verano']
    },
    'sandalia_wedges': {
        'nombre': 'Sandalia WEDGES',
        'categoria': 'abierto',
        'precio': 219900,
        'color': 'marrón',
        'tallas': [35, 36, 37, 38, 39, 40],
        'descripcion': 'Para actividades al aire libre',
        'material': 'Sintético deportivo',
        'imagen': 'Zapato_abierto2.webp',
        'palabras_clave': ['marron', 'sandalia', 'wedges', 'abierto', 'aire', 'libre']
    },
    'sandalia_casual': {
        'nombre': 'Sandalia Casual',
        'categoria': 'abierto',
        'precio': 189000,
        'color': 'blanco',
        'tallas': [35, 36, 37, 38, 39, 40],
        'descripcion': 'Perfectas para el verano',
        'material': 'Sintético ligero',
        'imagen': 'Zapato_abierto3.webp',
        'palabras_clave': ['blanco', 'sandalia', 'casual', 'abierto', 'verano', 'ligero']
    }
}

@app.route('/')
def index():
    """Página principal con información de la empresa"""
    return render_template('index.html', empresa=EMPRESA_INFO)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    """Página de contacto con formulario"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        mensaje = request.form.get('mensaje')
        
        if nombre and correo and mensaje:
            # Aquí puedes agregar lógica para enviar email o guardar en base de datos
            flash('¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.', 'success')
            return redirect(url_for('contacto'))
        else:
            flash('Por favor, completa todos los campos.', 'error')
    
    return render_template('contacto.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """API del chatbot inteligente para responder preguntas sobre productos"""
    data = request.get_json()
    pregunta = data.get('pregunta', '').lower().strip()
    
    # Manejar consultas sobre contacto o asesores
    if any(palabra in pregunta for palabra in ['contacto', 'asesor', 'ayuda humana', 'hablar', 'urgente', 'telefono', 'whatsapp']):
        return jsonify({
            'respuesta': redirigir_contacto(),
            'accion': 'redirigir_contacto'  # Señal para el frontend
        })
    
    # Si es un comando de menú numérico
    if pregunta.isdigit():
        return jsonify({'respuesta': procesar_menu_numerico(int(pregunta))})
    
    # Menú principal si no se entiende la pregunta o si pide ayuda
    if not pregunta or any(palabra in pregunta for palabra in ['hola', 'menu', 'menú', 'ayuda', 'help', 'opciones']):
        return jsonify({'respuesta': mostrar_menu_principal()})
    
    # Procesar diferentes tipos de consultas
    respuesta = procesar_consulta_inteligente(pregunta)
    
    # Si no encontró nada relevante, sugerir contacto
    if "No estoy seguro de entender" in respuesta:
        return jsonify({
            'respuesta': respuesta,
            'sugerir_contacto': True  # Señal para mostrar botón de contacto
        })
    
    return jsonify({'respuesta': respuesta})

def mostrar_menu_principal():
    """Muestra el menú principal del chatbot"""
    menu = """🤖 ¡Hola! Soy el asistente virtual de Calzado Bless Puerto López

📋 **MENÚ PRINCIPAL**

**Consultas de Productos:**
1️⃣ Ver todos los productos disponibles
2️⃣ Buscar por categoría (hombre, mujer, infantil, elegante, abierto)
3️⃣ Buscar por color
4️⃣ Consultar tallas disponibles
5️⃣ Buscar por precio

**Información de la Empresa:**
6️⃣ Misión y visión
7️⃣ Promociones y descuentos
8️⃣ Nuestros proveedores

**Ayuda:**
9️⃣ Hablar con un asesor
🔍 También puedes escribir directamente lo que buscas

Ejemplo: "zapatos negros talla 42" o "sandalias para niña"

Escribe el número de opción o describe lo que necesitas 👟✨"""
    
    return menu

def procesar_menu_numerico(opcion):
    """Procesa las opciones numéricas del menú"""
    opciones = {
        1: mostrar_todos_productos,
        2: lambda: "🏷️ **Categorías disponibles:**\n\n👨 **Hombre** - Zapatos clásicos, deportivos, formales\n👩 **Mujer** - Zapatos casuales, deportivos, urbanos\n💎 **Elegante** - Zapatos sofisticados para ocasiones especiales\n👶 **Infantil** - Calzado para niños y niñas\n🌊 **Abierto** - Sandalias y calzado fresco\n\nEscribe la categoría que te interesa o un número del menú principal.",
        3: lambda: "🎨 **Colores disponibles:**\n\n⚫ Negro\n🤎 Marrón\n⚪ Blanco\n🔵 Azul\n🌸 Rosa\n🌈 Multicolor\n\nEscribe el color que buscas o combínalo con otras palabras.",
        4: mostrar_tallas_disponibles,
        5: mostrar_rangos_precios,
        6: mostrar_info_empresa,
        7: lambda: f"🎉 **PROMOCIONES ACTUALES:**\n\n✨ {EMPRESA_INFO['descuento']}\n\n💡 Válido en toda nuestra colección. No olvides preguntar por otros descuentos especiales.\n\n¿Te interesa algún producto en particular?",
        8: mostrar_proveedores,
        9: redirigir_contacto
    }
    
    return opciones.get(opcion, lambda: "❌ Opción no válida. Escribe un número del 1 al 9 o describe lo que buscas.")()

def procesar_consulta_inteligente(pregunta):
    """Procesa consultas en lenguaje natural de forma inteligente"""
    # Buscar productos por diferentes criterios
    resultados = buscar_productos_inteligente(pregunta)
    
    if resultados:
        if len(resultados) == 1:
            return mostrar_producto_detallado(resultados[0])
        else:
            return mostrar_lista_productos(resultados, pregunta)
    
    # Consultas sobre información de la empresa
    if any(palabra in pregunta for palabra in ['mision', 'misión', 'vision', 'visión']):
        return mostrar_info_empresa()
    
    if any(palabra in pregunta for palabra in ['descuento', 'promocion', 'promoción', 'oferta']):
        return f"🎉 **PROMOCIÓN ACTUAL:**\n\n✨ {EMPRESA_INFO['descuento']}\n\n¿Te interesa algún producto específico para aplicar el descuento?"
    
    if any(palabra in pregunta for palabra in ['proveedor', 'marca', 'marcas']):
        return mostrar_proveedores()
    
    # Si contiene palabras relacionadas con tallas
    if any(palabra in pregunta for palabra in ['talla', 'tallas', 'numero', 'número', 'medida']):
        return mostrar_tallas_disponibles()
    
    # Si no encuentra nada específico, ofrecer ayuda
    return no_entiendo_respuesta()

def buscar_productos_inteligente(consulta):
    """Busca productos usando criterios inteligentes"""
    resultados = []
    palabras_consulta = consulta.lower().split()
    
    for producto_id, producto in PRODUCTOS_DB.items():
        puntos = 0
        
        # Buscar en nombre del producto
        nombre_palabras = producto['nombre'].lower().split()
        for palabra in palabras_consulta:
            if any(palabra in nombre_palabra for nombre_palabra in nombre_palabras):
                puntos += 3
        
        # Buscar en palabras clave
        for palabra in palabras_consulta:
            if any(palabra in keyword for keyword in producto['palabras_clave']):
                puntos += 2
        
        # Buscar por categoría
        if producto['categoria'] in consulta:
            puntos += 2
        
        # Buscar por color
        if producto['color'] in consulta:
            puntos += 2
        
        # Buscar tallas específicas
        for palabra in palabras_consulta:
            if palabra.isdigit():
                talla = int(palabra)
                if talla in producto['tallas']:
                    puntos += 2
        
        # Buscar por precio (rangos aproximados)
        if any(palabra in consulta for palabra in ['barato', 'economico', 'económico', 'infantil']):
            if 50000 <= producto['precio'] <= 100000:
                puntos += 2
        elif any(palabra in consulta for palabra in ['caro', 'premium', 'lujo', 'luxury']):
            if producto['precio'] >= 200000:
                puntos += 2
        elif any(palabra in consulta for palabra in ['medio', 'promedio', 'estándar', 'estandar']):
            if 150000 <= producto['precio'] <= 200000:
                puntos += 2
        
        if puntos >= 2:  # Umbral mínimo de relevancia
            resultados.append((producto, puntos))
    
    # Ordenar por relevancia
    resultados.sort(key=lambda x: x[1], reverse=True)
    return [producto for producto, puntos in resultados[:10]]  # Máximo 10 resultados

def mostrar_producto_detallado(producto):
    """Muestra información detallada de un producto específico"""
    tallas_str = ", ".join(map(str, producto['tallas']))
    precio_formateado = f"${producto['precio']:,}".replace(',', '.')
    
    return f"""✨ **{producto['nombre']}**

📝 **Descripción:** {producto['descripcion']}
🏷️ **Categoría:** {producto['categoria'].title()}
🎨 **Color:** {producto['color'].title()}
📏 **Tallas disponibles:** {tallas_str}
🧵 **Material:** {producto['material']}
💰 **Precio:** {precio_formateado}

🎉 ¡Recuerda que tienes 20% de descuento en tu segunda compra!

¿Te interesa este producto? ¿Necesitas más información o quieres ver otros similares?

Escribe "contacto" para hablar con un asesor."""

def mostrar_lista_productos(productos, consulta_original):
    """Muestra una lista de productos encontrados"""
    if len(productos) > 5:
        mensaje = f"🔍 **Encontré {len(productos)} productos para '{consulta_original}'** (mostrando los 5 más relevantes):\n\n"
        productos = productos[:5]
    else:
        mensaje = f"🔍 **Encontré {len(productos)} productos para '{consulta_original}':**\n\n"
    
    for i, producto in enumerate(productos, 1):
        precio_formateado = f"${producto['precio']:,}".replace(',', '.')
        tallas_str = ", ".join(map(str, producto['tallas']))
        mensaje += f"{i}. **{producto['nombre']}**\n"
        mensaje += f"   � {precio_formateado} | 🎨 {producto['color'].title()} | 📏 Tallas: {tallas_str}\n\n"
    
    mensaje += "💡 **Escribe el nombre del zapato que te interesa para ver más detalles**, o refina tu búsqueda.\n\n"
    mensaje += "¿Necesitas ayuda de un asesor? Escribe \"contacto\""
    
    return mensaje

def mostrar_todos_productos():
    """Muestra todos los productos organizados por categoría"""
    categorias = {}
    for producto in PRODUCTOS_DB.values():
        cat = producto['categoria']
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(producto)
    
    mensaje = "👟 **TODOS NUESTROS PRODUCTOS:**\n\n"
    
    iconos_categoria = {
        'hombre': '👨',
        'mujer': '👩',
        'elegante': '💎',
        'infantil': '👶',
        'abierto': '🌊'
    }
    
    for categoria, productos in categorias.items():
        icono = iconos_categoria.get(categoria, '👟')
        mensaje += f"{icono} **{categoria.upper()}**\n"
        for producto in productos:
            precio = f"${producto['precio']:,}".replace(',', '.')
            mensaje += f"• {producto['nombre']} - {precio}\n"
        mensaje += "\n"
    
    mensaje += "💡 Escribe el nombre del producto que te interesa o busca por color, talla, etc."
    return mensaje

def mostrar_tallas_disponibles():
    """Muestra todas las tallas disponibles por categoría"""
    return """📏 **TALLAS DISPONIBLES:**

👶 **INFANTIL (Niños y Niñas):** 21, 22, 23, 24, 25, 26, 27, 28, 29, 30

👩👨 **ADULTOS (Hombre y Mujer):** 35, 36, 37, 38, 39, 40, 41, 42, 43, 44

💡 **Consejo:** Escribe algo como "zapatos talla 38" para ver qué productos tenemos en tu talla.

¿Buscas alguna talla en particular? Puedo ayudarte a encontrar productos disponibles."""

def mostrar_rangos_precios():
    """Muestra los rangos de precios disponibles"""
    return """💰 **RANGOS DE PRECIOS:**

💚 **INFANTIL:** $50.000 - $100.000
(Calzado para niños y niñas, cómodo y resistente)

💛 **ESTÁNDAR:** $150.000 - $200.000
(Excelente variedad para hombre y mujer)

💜 **PREMIUM:** $200.000 - $250.000
(Calzado elegante y de alta calidad)

💎 **LUXURY:** Más de $250.000
(Zapatos de lujo con materiales premium)

🎉 ¡Recuerda el 20% de descuento en tu segunda compra!

💡 Escribe algo como "zapatos económicos" o "zapatos premium" para filtrar por precio."""

def mostrar_info_empresa():
    """Muestra información de la empresa"""
    return f"""🏢 **INFORMACIÓN DE LA EMPRESA**

**📍 {EMPRESA_INFO['nombre']}**

🎯 **NUESTRA MISIÓN:**
{EMPRESA_INFO['mision']}

🔮 **NUESTRA VISIÓN:**
{EMPRESA_INFO['vision']}

✨ **¿Por qué elegirnos?**
• Calzado de calidad garantizada
• Productos cómodos para la salud de tus pies
• Atención personalizada
• Envío a domicilio disponible

¿Te gustaría conocer nuestros productos o hablar con un asesor?"""

def mostrar_proveedores():
    """Muestra información de proveedores"""
    proveedores_lista = '\n'.join([f"• {proveedor}" for proveedor in EMPRESA_INFO['proveedores']])
    return f"""🏪 **NUESTROS PROVEEDORES DE CONFIANZA:**

{proveedores_lista}

✅ Todos nuestros proveedores están certificados y garantizan la calidad de nuestros productos.

🤝 Trabajamos con las mejores marcas para ofrecerte calzado de excelente calidad a precios justos.

¿Te interesa alguna marca en particular?"""

def redirigir_contacto():
    """Redirige a contacto para hablar con un asesor"""
    return """👨‍💼 **HABLAR CON UN ASESOR**

🎯 Te conectaré con uno de nuestros asesores especializados para una atención personalizada.

📞 **Opciones de contacto:**
• WhatsApp: Atención inmediata
• Formulario web: Respuesta en menos de 2 horas
• Visita en tienda: Puerto López, Colombia

[🔗 Ir a la página de contacto](/contacto)

⚡ **¿Urgente?** Escribe "urgente" y te daré nuestro WhatsApp directo."""

def no_entiendo_respuesta():
    """Respuesta cuando no se entiende la consulta"""
    return """🤔 No estoy seguro de entender exactamente lo que buscas.

💡 **Puedes intentar:**
• Ser más específico: "zapatos negros hombre talla 42"
• Usar palabras simples: "sandalias niña rosa"
• Elegir una opción del menú: escribe "menú"

🆘 **O puedo conectarte con un asesor humano** - escribe "contacto"

¿Qué te gustaría saber sobre nuestro calzado? 👟"""

@app.errorhandler(404)
def page_not_found(e):
    """Página de error 404"""
    return render_template('index.html', empresa=EMPRESA_INFO), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)