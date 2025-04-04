import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n <= 0 or n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser un número par y positivo.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)      # Puntos del intervalo
    fx = f(x)                         # Evaluamos la función en esos puntos
    
    # Aplicamos la regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    return integral

# Función que representa la fuerza del resorte (k * x)
def trabajo_resorte(x):
    k = 200  # Constante del resorte en N/m
    return k * x

# Parámetros
a = 0.1  # Límite inferior (m)
b = 0.3  # Límite superior (m)
n_valores = [6, 10, 20, 30]  # Subintervalos para aproximación

# Solución analítica: Trabajo = 0.5 * k * (b² - a²)
solucion_analitica = 0.5 * 200 * (b**2 - a**2)

# Resultados numéricos y errores
resultados = []
errores = []

print("Resultados usando la Regla de Simpson:\n")
for n in n_valores:
    resultado_num = simpson_rule(trabajo_resorte, a, b, n)
    resultados.append(resultado_num)
    error = abs(resultado_num - solucion_analitica)
    errores.append(error)
    print(f"n = {n:<2}: Trabajo ≈ {resultado_num:.4f} J | Error = {error:.4e} J")

print(f"\nSolución analítica: {solucion_analitica:.4f} J")

# --- Gráfica de la función y área aproximada con n = 30 ---
x_vals = np.linspace(a, b, 100)
y_vals = trabajo_resorte(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$Trabajo(x) = kx$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área bajo la curva")
plt.scatter(np.linspace(a, b, 31), trabajo_resorte(np.linspace(a, b, 31)), 
            color="red", label="Puntos Simpson")
plt.xlabel("x (m)")
plt.ylabel("Fuerza (N)")
plt.title("Trabajo realizado por el resorte (Regla de Simpson)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("trabajo_resorte_simpson.png")
plt.show()

# --- Gráfica del error vs número de subintervalos ---
plt.figure(figsize=(7, 4))
plt.plot(n_valores, errores, marker='o', linestyle='--', color='purple')
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto (J)")
plt.title("Error en la aproximación del trabajo")
plt.grid(True)
plt.tight_layout()
plt.savefig("error_trabajo_resorte.png")
plt.show()
