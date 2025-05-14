# backend/utils.py

import math

def f(x, N):
    return x*x - N

def regula_falsi_modificada(N, error_exp, max_iter=100):
    """
    Devuelve (raiz, tabla) donde tabla es lista de filas:
      [n, x_n, f(x_n), salto]
    con salto = "–" para n=0, o |x_n - x_{n-1}|.
    """
    eps = 10**(-error_exp)
    tabla = []

    # 1) Escoger [a0,b0] = [floor(sqrt(N)), ceil(sqrt(N))] si f(a0)*f(b0)<0
    a0 = math.floor(math.sqrt(N))
    b0 = math.ceil(math.sqrt(N))
    if f(a0, N) * f(b0, N) < 0:
        a, b = float(a0), float(b0)
    else:
        a, b = 0.0, max(1.0, N)
        if f(a, N) * f(b, N) > 0:
            return None, tabla

    # n = 0
    x_prev = a
    tabla.append([
      0,
      f"{x_prev:.15f}",
      f"{f(x_prev, N):.15f}",
      "–"
    ])

    # iteraciones n = 1,2,...
    for n in range(1, max_iter+1):
        fa, fb = f(a, N), f(b, N)
        x_n = (a*fb - b*fa) / (fb - fa)
        salto = abs(x_n - x_prev)
        fxn   = f(x_n, N)

        tabla.append([
          n,
          f"{x_n:.15f}",
          f"{fxn:.15f}",
          f"{salto:.15f}"
        ])

        if salto < eps:
            return x_n, tabla

        # actualizar extremos
        if fa * fxn < 0:
            b = x_n
        else:
            a = x_n

        x_prev = x_n

    return x_prev, tabla
