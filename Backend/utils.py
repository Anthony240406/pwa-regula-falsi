# backend/utils.py

import math

def f(x, N):
    """Función objetivo: x² − N"""
    return x*x - N

def regula_falsi_modificada(N, error_exp, max_iter=100):
    """
    Regula-Falsi modificado con:
      - Intervalo inicial [floor(sqrt(N)), ceil(sqrt(N))] si válido,
        o bien [0, max(1,N)] si no.
      - Criterio de parada |x_n - x_{n-1}| < 10^{-error_exp}.
      - Se devuelve (raiz, tabla) donde tabla es una lista de filas
        [n, x_n, f(x_n), salto].
    """
    eps = 10**(-error_exp)
    tabla = []

    # 1) Escoger intervalo inicial
    a0 = math.floor(math.sqrt(N))
    b0 = math.ceil(math.sqrt(N))
    if f(a0, N) * f(b0, N) < 0:
        a, b = float(a0), float(b0)
    else:
        a, b = 0.0, max(1.0, N)
        if f(a, N) * f(b, N) > 0:
            return None, tabla

    # 2) Fila n = 0
    x_prev = a
    tabla.append([
        0,
        f"{x_prev:.15f}",
        f"{f(x_prev, N):.15f}",
        "–"
    ])

    # Inicializar x_n para evitar referencias antes de asignación
    x_n = x_prev

    # 3) Iteraciones n = 1,2,...
    for n in range(1, max_iter+1):
        fa, fb = f(a, N), f(b, N)
        # Fórmula de Regula-Falsi
        x_n = (a * fb - b * fa) / (fb - fa)
        salto = abs(x_n - x_prev)
        fxn   = f(x_n, N)

        # Añadir la fila de la iteración
        tabla.append([
            n,
            f"{x_n:.15f}",
            f"{fxn:.15f}",
            f"{salto:.15f}"
        ])

        # Criterio de parada: salto < eps
        if salto < eps:
            return x_n, tabla

        # Actualizar extremos para la siguiente iteración
        if fa * fxn < 0:
            b = x_n
        else:
            a = x_n

        x_prev = x_n

    # Si no converge en max_iter, devuelve la última aproximación
    return x_n, tabla
