# backend/utils.py

def f(x, N):
    """Función objetivo para √N: f(x) = x² − N"""
    return x**2 - N

def regula_falsi_modificada(N, a, b, error_exp, max_iter=100):
    """
    Regula Falsi modificado para hallar la raíz de f(x)=0 en [a,b].
    - N: número al que queremos la raíz
    - a, b: cotas iniciales
    - error_exp: exponente x para tolerancia eps = 10^{-x}
    - max_iter: iteraciones máximas
    Devuelve (raiz, tabla), donde tabla = [[i, a, b, x, f(x), error], …].
    Si el intervalo inicial no encierra raíz, devuelve (None, []).
    """
    eps = 10 ** (-error_exp)
    tabla = []

    fa, fb = f(a, N), f(b, N)
    # Si f(a) y f(b) tienen mismo signo, no hay cambio de signo → error
    if fa * fb > 0:
        return None, tabla

    # Inicializamos x para que siempre exista al final
    x = a

    for i in range(1, max_iter + 1):
        # Punto de Regula Falsi
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x, N)
        error = abs(fx)
        tabla.append([i, round(a, 6), round(b, 6),
                         round(x, 6), round(fx, 6), round(error, 6)])

        # Criterio de paro
        if error < eps:
            return x, tabla

        # Actualización modificada de extremos
        if fa * fx < 0:
            b, fb = x, fx
            # Dividimos fa para acelerar el método modificado
            fa /= 2
        else:
            a, fa = x, fx
            fb /= 2

    # Si no convergió en max_iter, devolvemos la última aproximación
    return x, tabla
