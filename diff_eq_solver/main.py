from solver.euler import euler
from util.plotter import plot_solution
import numpy as np

def get_user_input():
    print("Differential Equation Solver")
    print("Currently supported methods: Euler\n")

    method = input("Select method [euler]: ").strip().lower()
    if method != "euler":
        print("Only 'euler' method is currently implemented.")
        method = "euler"

    print("\nExample: dy/dt = f(t, y).")
    print("Let’s define f(t, y). You can use Python syntax.")
    print("Example: -9.8 (for constant acceleration) or y - t")

    f_str = input("Enter function f(t, y): ")
    try:
        f = eval("lambda t, y: " + f_str)
        test = f(0, 1)  # test if it works
    except Exception as e:
        print("Invalid function. Error:", e)
        return None, None, None, None, None

    y0 = float(input("Enter initial value y(0): "))
    t0 = float(input("Enter start time t0: "))
    t_end = float(input("Enter end time t_end: "))
    n_points = int(input("Enter number of time steps: "))

    t = np.linspace(t0, t_end, n_points)
    return f, y0, t, method

def main():
    f, y0, t, method = get_user_input()
    if not f:
        print("Exiting...")
        return

    if method == "euler":
        y = euler(f, y0, t)
        plot_solution(t, y, title="Euler Method Solution")

if __name__ == "__main__":
    main()