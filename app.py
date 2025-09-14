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
    """API del chatbot para responder preguntas"""
    data = request.get_json()
    pregunta = data.get('pregunta', '').lower()
    
    respuesta = "No entiendo tu pregunta. Puedes preguntarme sobre nuestra misión, visión o descuentos disponibles."
    
    if 'mision' in pregunta or 'misión' in pregunta:
        respuesta = f"📍 Nuestra misión: {EMPRESA_INFO['mision']}"
    elif 'vision' in pregunta or 'visión' in pregunta:
        respuesta = f"🔮 Nuestra visión: {EMPRESA_INFO['vision']}"
    elif 'descuento' in pregunta or 'promocion' in pregunta or 'promoción' in pregunta:
        respuesta = f"🎉 Promoción actual: {EMPRESA_INFO['descuento']}"
    elif 'producto' in pregunta or 'calzado' in pregunta:
        respuesta = f"👟 Nuestros productos: {EMPRESA_INFO['productos']}"
    elif 'proveedor' in pregunta or 'marcas' in pregunta or 'marca' in pregunta:
        proveedores_lista = ', '.join(EMPRESA_INFO['proveedores'])
        respuesta = f"🏪 Nuestros proveedores: {proveedores_lista}"
    elif 'hola' in pregunta or 'buenos' in pregunta or 'buenas' in pregunta:
        respuesta = "¡Hola! 👋 Soy el asistente virtual de Calzado Bless Puerto López. Puedes preguntarme sobre nuestra misión, visión, descuentos, productos o proveedores."
    elif 'ayuda' in pregunta or 'help' in pregunta:
        respuesta = "Puedo ayudarte con información sobre:\n• Misión de la empresa\n• Visión empresarial\n• Descuentos y promociones\n• Productos disponibles\n• Nuestros proveedores"
    
    return jsonify({'respuesta': respuesta})

@app.errorhandler(404)
def page_not_found(e):
    """Página de error 404"""
    return render_template('index.html', empresa=EMPRESA_INFO), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)