import matplotlib.pyplot as plt

def plot_schedule(head, sequence, algo_name):
    plt.plot([head] + sequence, marker='o', linestyle='-')
    plt.title(f"{algo_name} Disk Scheduling")
    plt.xlabel("Requests")
    plt.ylabel("Seek Position")
    plt.grid()
    plt.show()
