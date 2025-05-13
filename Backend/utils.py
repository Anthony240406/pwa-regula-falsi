# backend/utils.py

def f(x, N):
    """Función objetivo para √N: f(x) = x² − N"""
    return x**2 - N

def regula_falsi_modificada(N, a, b, error_exp, max_iter=100):
    """
    Regula Falsi modificado para hallar la raíz de f(x)=0 en [a,b].
    Devuelve (raíz, tabla) donde tabla = [[i, a, b, x, f(x), error], ...].
    """
    eps = 10 ** (-error_exp)
    tabla = []
    fa, fb = f(a, N), f(b, N)

    # --- Paso a/b: inicialización estilo bisección ---
    if fa * fb > 0:
        return None, tabla
        # mismo signo → x0 = a, ef = b
        x0, ef = a, b
        fx0, fef = fa, fb
    else:
        # distinto signo → x0 = b, ef = a
        x0, ef = b, a
        fx0, fef = fb, fa

    n = 0
    while n < max_iter:
        # (e) Regula Falsi: nuevo punto en x0
        x1 = (x0 * fef - ef * fx0) / (fef - fx0)
        fx1 = f(x1, N)
        error = abs(fx1)
        tabla.append([n + 1,
                      round(x0, 6),
                      round(ef, 6),
                      round(x1, 6),
                      round(fx1, 6),
                      round(error, 6)])

        # (d) Criterio de paro
        if error < eps:
            return x1, tabla

        # (f) n <- n + 1
        n += 1

        # (b) y (c): decidir nuevo par (x0, ef)
        # reemplazamos el extremo variable x0:
        if fx0 * fx1 < 0:
            # la raíz está entre x0 y x1 → fijo ef, variable x0 = x1
            x0, fx0 = x1, fx1
            # reducimos fef a la mitad (modificado)
            fef /= 2
        else:
            # la raíz está entre x1 y ef → fijo x0, variable ef = x1
            ef, fef = x1, fx1
            fx0 /= 2

    # Si agotamos iteraciones:
    return x, tabla