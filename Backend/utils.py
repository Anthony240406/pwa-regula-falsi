# backend/utils.py

import math

def f(x, N):
    return x*x - N

def regula_falsi_modificada(N, error_exp, max_iter=100):
    eps = 10**(-error_exp)
    tabla = []

    # 1) Intervalo inicial natural [floor(sqrt(N)), ceil(sqrt(N))]
    a0, b0 = math.floor(math.sqrt(N)), math.ceil(math.sqrt(N))
    if f(a0, N)*f(b0, N) < 0:
        a, b = float(a0), float(b0)
    else:
        a, b = 0.0, max(1.0, N)
        if f(a, N)*f(b, N) > 0:
            return None, tabla

    # 2) Fila n=0
    x_prev = a
    tabla.append([0, f"{x_prev:.15f}", f"{f(x_prev,N):.15f}", "–"])

    # 3) Iteraciones
    for n in range(1, max_iter+1):
        fa, fb = f(a,N), f(b,N)
        x_n = (a*fb - b*fa)/(fb - fa)
        salto = abs(x_n - x_prev)
        fxn   = f(x_n, N)

        # Añadir la fila **y comprobar paro** inmediatamente
        tabla.append([n, f"{x_n:.15f}", f"{fxn:.15f}", f"{salto:.15f}"])
        if salto < eps:
            return x_n, tabla   # ¡Cortar aquí, sin más iteraciones!

        # Actualizar cotas
        if fa * fxn < 0:
            b = x_n
        else:
            a = x_n

        x_prev = x_n

    return x_prev, tabla
