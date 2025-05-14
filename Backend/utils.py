import math

def f(x, N):
    """Función objetivo para √N: f(x) = x² − N"""
    return x**2 - N

def regula_falsi_modificada(N, error_exp, max_iter=100):
    """
    Regula Falsi modificado para hallar la raíz de x² = N.
    - N: número cuya raíz buscamos.
    - error_exp: exponente x, eps = 10^{-x}.
    - max_iter: iteraciones máximas.
    Devuelve (raiz, tabla) o (None, []) si intervalo inválido.
    """
    eps = 10 ** (-error_exp)
    tabla = []

    # 1) Intentamos cotas naturales [floor(sqrt(N)), ceil(sqrt(N))]
    a0 = math.floor(math.sqrt(N))
    b0 = math.ceil(math.sqrt(N))
    fa0, fb0 = f(a0, N), f(b0, N)

    if fa0 * fb0 < 0:
        a, b = float(a0), float(b0)
        fa, fb = fa0, fb0
    else:
        # Fallback a [0, max(1, N)]
        a, b = 0.0, max(1.0, N)
        fa, fb = f(a, N), f(b, N)
        if fa * fb > 0:
            return None, tabla

    x = a
    for i in range(1, max_iter + 1):
        # Regula Falsi
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x, N)
        err = abs(fx)
        tabla.append([i,
                      round(a, 6),
                      round(b, 6),
                      round(x, 6),
                      round(fx, 6),
                      round(err, 6)])
        if err < eps:
            return x, tabla

        # Actualización modificada
        if fa * fx < 0:
            b, fb = x, fx
            fa /= 2
        else:
            a, fa = x, fx
            fb /= 2

    return x, tabla
