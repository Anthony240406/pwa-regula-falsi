# backend/utils.py

def f(x, N):
    """Función objetivo para √N: f(x) = x² − N"""
    return x**2 - N

def regula_falsi_modificada(N, a, b, error_tolerado, max_iter=100):
    """
    Regula Falsi modificado para hallar la raíz de f(x)=0 en [a,b].
    Devuelve (raíz, tabla) donde tabla = [[i, a, b, x, f(x), error], ...].
    """
    tabla = []
    fa, fb = f(a, N), f(b, N)
    if fa * fb > 0:
        return None, tabla

    for i in range(1, max_iter+1):
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x, N)
        error = abs(fx)
        tabla.append([i, round(a,6), round(b,6), round(x,6), round(fx,6), round(error,6)])

        if error < error_tolerado:
            return x, tabla

        if fa * fx < 0:
            b, fb = x, fx
            fa /= 2
        else:
            a, fa = x, fx
            fb /= 2

    return x, tabla
