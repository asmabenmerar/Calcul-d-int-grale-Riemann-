import numpy as np
import matplotlib.pyplot as plt

def riemann_sum(f, a, b, n):
    """
    Calcule l'intégrale d'une fonction par la méthode de Riemann basique
    """
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    x_points = x[:-1]  # Points à gauche par défaut
    somme = np.sum(f(x_points) * dx)
    return somme

if __name__ == "__main__":
    f = lambda x: x**2
    resultat = riemann_sum(f, 0, 2, 10)
    print(f"Intégrale approchée : {resultat:.4f}")