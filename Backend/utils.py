# backend/utils.py

import math

def f(x, N):
    return x*x - N

def regula_falsi_modificado_illinois(N, error_exp, max_iter=100):
    """
    Regula Falsi modificado (método de Illinois).
    - Si un extremo (a o b) queda fijo dos veces,
      usamos f_extremo := f(extremo) / 2 para "inclinar"
      la recta y romper el estancamiento.
    Tabla: [n, a, b, x_n, f(x_n), salto].
    """
    eps   = 10**(-error_exp)
    tabla = []

    # 1) Intervalo inicial [floor(sqrt), ceil(sqrt)] ó [0,max(1,N)]
    a0, b0 = math.floor(math.sqrt(N)), math.ceil(math.sqrt(N))
    if f(a0,N)*f(b0,N) < 0:
        a, b = float(a0), float(b0)
    else:
        a, b = 0.0, max(1.0, N)
        if f(a,N)*f(b,N) > 0:
            return None, tabla

    # Pesos para Illinois
    wa, wb      = 1.0, 1.0   # multiplicadores de f(a), f(b)
    last_fixed  = None       # 'a' o 'b'
    x_prev      = a

    # 2) Iteración 0: solo extremos
    tabla.append([0, f"{a:.15f}", f"{b:.15f}", "–", "–", "–"])

    # 3) Iteraciones siguientes
    for n in range(1, max_iter+1):
        # Aplico el factor al extremo fijo si procede
        fa, fb = f(a,N) * wa, f(b,N) * wb

        # Cálculo del punto de intersección (Illinois)
        x_n = (a*fb - b*fa) / (fb - fa)
        fxn   = f(x_n, N)
        salto = abs(x_n - x_prev)

        tabla.append([
            n,
            f"{a:.15f}",
            f"{b:.15f}",
            f"{x_n:.15f}",
            f"{fxn:.15f}",
            f"{salto:.15f}"
        ])

        # Criterio de paro
        if salto < eps:
            return x_n, tabla

        # Decidir qué extremo se mueve
        if fa * fxn < 0:
            # la raíz está en [a, x_n] → fijamos b, movemos a
            fixed, moving = 'b', 'a'
            a = x_n
        else:
            # la raíz está en [x_n, b] → fijamos a, movemos b
            fixed, moving = 'a', 'b'
            b = x_n

        # Si el mismo extremo vuelve a fijarse, dividimos su peso por 2
        if last_fixed == fixed:
            if fixed == 'a':
                wa *= 0.5
            else:
                wb *= 0.5
        else:
            # si cambiamos de extremo fijo, restauramos pesos
            wa, wb = 1.0, 1.0

        last_fixed = fixed
        x_prev     = x_n

    # Si no converge antes de max_iter, devolvemos la última aproximación
    return x_n, tabla

regula_falsi_modificada = regula_falsi_modificado_illinois