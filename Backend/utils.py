# backend/utils.py

import math

def f(x, N):
    """Función objetivo: x² − N"""
    return x**2 - N

def regula_falsi_modificada(N, error_exp, max_iter=100):
    """
    Regula-Falsi modificado con:
      - Intervalo inicial [a0,b0] = [floor(√N), ceil(√N)] si f(a0)*f(b0)<0,
        o bien [0, max(1,N)] en caso contrario.
      - Fórmula: x_{n+1} = ef - f(ef)*(ef - x_n)/(f(ef)-f(x_n))
      - Criterio de parada: |x_{n+1} - x_n| < 10^{-error_exp}
      - max_iter: número máximo de iteraciones
    Devuelve (raiz, tabla) o (None, []) si no hay intervalo válido.
    """
    eps = 10**(-error_exp)
    tabla = []

    # 1) Elegir intervalo inicial natural
    a0 = math.floor(math.sqrt(N))
    b0 = math.ceil(math.sqrt(N))
    fa0, fb0 = f(a0, N), f(b0, N)

    if fa0 * fb0 < 0:
        a, b = float(a0), float(b0)
        fa, fb = fa0, fb0
    else:
        # Fallback a [0, max(1,N)]
        a, b = 0.0, max(1.0, N)
        fa, fb = f(a, N), f(b, N)
        if fa * fb > 0:
            return None, tabla

    # x_n empieza en el extremo a
    x_n = a

    for i in range(1, max_iter+1):
        # 2) Regula Falsi
        # ponemos ef=b y x_n como variable
        ef, fx_n, fef = b, f(x_n, N), fb
        # fórmula: x_{n+1} = ef - f(ef)*(ef - x_n)/(f(ef)-f(x_n))
        x_np1 = ef - fef * (ef - x_n) / (fef - fx_n)

        # Calcular salto y valor de función
        salto = abs(x_np1 - x_n)
        fx_np1 = f(x_np1, N)
        # Guardar en tabla con 15 decimales
        tabla.append([
            i,
            f"{x_n:.15f}",
            f"{ef:.15f}",
            f"{x_np1:.15f}",
            f"{fx_np1:.15f}",
            f"{salto:.15f}",
        ])

        # 3) Criterio de parada en el cambio de x
        if salto < eps:
            return x_np1, tabla

        # 4) Actualizar extremos para siguiente iteración
        # si f(a)*f(x_{n+1}) < 0, la raíz está en [a, x_{n+1}], fijamos b=ef=x_n
        if fa * fx_np1 < 0:
            b, fb = x_n, fx_n
        else:
            a, fa = x_n, fx_n

        # Preparar siguiente ciclo
        x_n = x_np1

    # Si no converge en max_iter, devolvemos último x
    return x_n, tabla
