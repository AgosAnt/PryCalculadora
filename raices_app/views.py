
import base64
import io

from django.shortcuts import render
from .forms import RootForm
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        raise ValueError('No hay cambio de signo en el intervalo')
    table = []
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        f_c = f(c)
        error = abs(b - a) / 2.0
        table.append({'iter': i, 'approx': c, 'f(c)': f_c, 'error': error})
        if abs(f_c) < tol or error < tol:
            return c, table
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
    return c, table

def newton_method(f, fprime, x0, tol, max_iter):
    table = []
    xn = x0
    for i in range(1, max_iter + 1):
        fx = f(xn)
        fpx = fprime(xn)
        if fpx == 0:
            raise ValueError('Derivada cero en iteración')
        xn1 = xn - fx / fpx
        error = abs(xn1 - xn)
        table.append({'iter': i, 'approx': xn1, 'f(x)': fx, 'error': error})
        if abs(fx) < tol or error < tol:
            return xn1, table
        xn = xn1
    return xn, table

def newton_modified_method(f, fprime, fprime2, x0, tol, max_iter):
    table = []
    xn = x0
    for i in range(1, max_iter + 1):
        fx = f(xn)
        fpx = fprime(xn)
        fppx = fprime2(xn)
        denom = fpx**2 - fx * fppx
        if denom == 0:
            raise ValueError('Denominador cero en iteración')
        xn1 = xn - (fx * fpx) / denom
        error = abs(xn1 - xn)
        table.append({'iter': i, 'approx': xn1, 'f(x)': fx, 'error': error})
        if abs(fx) < tol or error < tol:
            return xn1, table
        xn = xn1
    return xn, table

def plot_polynomial(f, root, interval=None):
    plt.close()
    fig, ax = plt.subplots()
    if interval:
        x_vals = np.linspace(interval[0], interval[1], 400)
    else:
        x_vals = np.linspace(root - 5, root + 5, 400)
    y_vals = [f(x) for x in x_vals]
    ax.plot(x_vals, y_vals, label='Polinomio')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.plot(root, f(root), 'ro', label='Raíz')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def index(request):
    result = None
    table = None
    img = None
    if request.method == 'POST':
        form = RootForm(request.POST)
        if form.is_valid():
            expr = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            tol = form.cleaned_data['tolerancia']
            max_iter = form.cleaned_data['max_iter']
            try:
                x = sp.symbols('x')
                f_sympy = sp.sympify(expr)
                f = sp.lambdify(x, f_sympy, 'numpy')
                fprime_sympy = sp.diff(f_sympy, x)
                fprime = sp.lambdify(x, fprime_sympy, 'numpy')
                fprime2_sympy = sp.diff(fprime_sympy, x)
                fprime2 = sp.lambdify(x, fprime2_sympy, 'numpy')

                if metodo == 'biseccion':
                    a = form.cleaned_data['a']
                    b = form.cleaned_data['b']
                    root, table = bisection_method(f, a, b, tol, max_iter)
                    interval = (a, b)
                elif metodo == 'newton':
                    x0 = form.cleaned_data['x0']
                    root, table = newton_method(f, fprime, x0, tol, max_iter)
                    interval = None
                else:
                    x0 = form.cleaned_data['x0']
                    root, table = newton_modified_method(f, fprime, fprime2, x0, tol, max_iter)
                    interval = None

                img = plot_polynomial(f, root, interval)
                result = root
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = RootForm()
    return render(request, 'raices_app/index.html', {'form': form, 'result': result, 'table': table, 'img': img})
