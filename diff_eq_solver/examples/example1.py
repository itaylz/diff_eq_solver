from solver.euler import euler
from util.plotter import plot_solution
import numpy as np

# Example: dy/dt = -9.8 (falling object under gravity), y(0) = 100
def f(t, y):
    return -9.8

y0 = 100
t = np.linspace(0, 5, 100)

y = euler(f, y0, t)
plot_solution(t, y, title="Free Fall: Euler Method")