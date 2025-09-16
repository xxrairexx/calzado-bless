/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#3498db',      // Azul principal (similar a tu CSS actual)
          secondary: '#2980b9',    // Azul más oscuro
          accent: '#f39c12',       // Naranja acento
          'accent-dark': '#e67e22', // Naranja secundario
          dark: '#2c3e50',         // Gris oscuro
          light: '#f8f9fa',        // Color claro de fondo
          neutral: '#ecf0f1',      // Neutro claro
          success: '#27ae60',      // Verde para éxito
          warning: '#f1c40f',      // Amarillo para advertencias
          danger: '#e74c3c'        // Rojo para errores
        }
      },
      fontFamily: {
        sans: ['"Segoe UI"', 'Tahoma', 'Geneva', 'Verdana', 'sans-serif']
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'bounce-in': 'bounceIn 0.6s ease-out'
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        bounceIn: {
          '0%': { transform: 'scale(0.3)', opacity: '0' },
          '50%': { transform: 'scale(1.05)' },
          '70%': { transform: 'scale(0.9)' },
          '100%': { transform: 'scale(1)', opacity: '1' }
        }
      },
      boxShadow: {
        'brand': '0 4px 14px 0 rgba(52, 152, 219, 0.39)',
        'brand-lg': '0 10px 30px 0 rgba(52, 152, 219, 0.3)',
        'accent': '0 4px 14px 0 rgba(243, 156, 18, 0.39)',
        'accent-lg': '0 10px 30px 0 rgba(243, 156, 18, 0.3)'
      }
    }
  },
  plugins: []
}