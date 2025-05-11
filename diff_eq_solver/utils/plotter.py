import matplotlib.pyplot as plt

def plot_solution(t, y, title="Differential Equation Solution"):
    plt.plot(t, y, label='y(t)')
    plt.xlabel('Time')
    plt.ylabel('y')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()