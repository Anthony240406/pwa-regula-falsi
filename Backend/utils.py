# backend/utils.py

import math

def f(x, N):
    return x*x - N

def regula_falsi_modificada(N, error_exp, max_iter=100):
    """
    Devuelve (raiz, tabla) donde:
      tabla es lista de [n, x_n, f(x_n), salto]:
        - n = 0,1,2,...
        - salto = |x_n - x_{n-1}| o "–" si n=0
    """
    eps = 10**(-error_exp)
    tabla = []

    # 1) Escogemos cotas iniciales [3,4] para N=10, o fallback [0,max(1,N)]
    a0 = math.floor(math.sqrt(N))
    b0 = math.ceil(math.sqrt(N))
    fa0, fb0 = f(a0, N), f(b0, N)
    if fa0 * fb0 < 0:
        a, b = float(a0), float(b0)
    else:
        a, b = 0.0, max(1.0, N)
        fa0, fb0 = f(a, N), f(b, N)
        if fa0 * fb0 > 0:
            return None, tabla

    # 2) Fila n=0
    x_n = a
    tabla.append([
        0,
        f"{x_n:.15f}",
        f"{f(x_n, N):.15f}",
        "–"
    ])

    # 3) Iteraciones
    for n in range(1, max_iter+1):
        # punto ef siempre b y punto var x_n
        fa, fb = f(a, N), f(b, N)
        x_np1 = (a*fb - b*fa) / (fb - fa)

        # salto entre iteraciones
        salto = abs(x_np1 - x_n)
        fx_np1 = f(x_np1, N)

        # añadir fila n
        tabla.append([
            n,
            f"{x_np1:.15f}",
            f"{fx_np1:.15f}",
            f"{salto:.15f}"
        ])

        # criterio de paro: salto < eps
        if salto < eps:
            return x_np1, tabla

        # actualizar extremos según signo
        if fa * fx_np1 < 0:
            b = x_np1
        else:
            a = x_np1

        x_n = x_np1

    return x_n, tabla
