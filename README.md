# Calculadora de Raíces de Polinomios con Métodos Numéricos

Esta aplicación web permite calcular las raíces de funciones polinómicas utilizando tres métodos numéricos clásicos:

- Método de Bisección  
- Método de Newton-Raphson  
- Método de Newton-Raphson Modificado

El sistema está desarrollado en Python con el framework Django, e incorpora herramientas como NumPy, SymPy y Matplotlib para el análisis y visualización matemática.

---

## Funcionalidades

- Ingreso de funciones polinómicas personalizadas (ej. `x**3 - x - 2`)  
- Selección de método numérico desde un formulario amigable  
- Solicitud de parámetros según el método:
  - Bisección: extremos [a, b], tolerancia, iteraciones máximas  
  - Newton-Raphson y Modificado: valor inicial x₀, tolerancia, iteraciones máximas  
- Tabla de iteraciones con:
  - Número de iteración  
  - Aproximación de la raíz  
  - Error relativo  
  - Evaluaciones de la función  
- Gráfica interactiva de la función, con intervalos destacados  
- Validación y manejo de errores (intervalos inválidos, división por cero, etc.)

---

## Métodos numéricos implementados

### Bisección

Método basado en el Teorema del Valor Intermedio. Requiere un intervalo donde exista un cambio de signo en la función. Convergencia garantizada si la función es continua.

### Newton-Raphson

Método iterativo que utiliza derivadas para encontrar la raíz. Requiere un valor inicial cercano a la raíz. Puede fallar si la derivada se anula o si el punto inicial no está bien elegido.

### Newton-Raphson Modificado

Versión optimizada del método anterior, donde la derivada no se recalcula en cada paso. Esto reduce el costo computacional en ciertas funciones polinómicas.

---

## Tecnologías utilizadas

- Python 3.10 o superior  
- Django 4.x  
- NumPy  
- SymPy  
- Matplotlib  
- HTML5, CSS3, Bootstrap (para el diseño de la interfaz)

---

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPO.git
   cd TU_REPO


////
CREAR UN ENTORNO VIRTUAL --
python -m venv venv

 -- ACTIVARLO
.\venv\Scripts\activate

 -- INSTALAR DEPENDENCIAS
pip install -r requirements.txt

 -- EJECUTAR SERVIDOR
python manage.py runserver

 -- ACCEDER EN EL NAVEGADOR
http://127.0.0.1:8000/

#Estructura del proyecto
Proyecto/
├── app/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── forms.py
│   └── ...
├── Proyecto/
├── venv/
├── manage.py
├── requirements.txt
└── README.md

DENTRO DE NUESTRAS VALIDACIONES
- Se comprueba si el intervalo ingresado en bisección tiene cambio de signo.

- Se valida que no haya divisiones por cero en Newton-Raphson.

- Se limita el número de iteraciones para evitar bucles infinitos.

- Se muestran mensajes claros en caso de errores o entradas inválidas.
