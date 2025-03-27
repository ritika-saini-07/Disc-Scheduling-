import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from traditional_algorithms.fcfs import fcfs
from traditional_algorithms.sstf import sstf

from models.ai_scheduler import AIScheduler

class DiskSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Based Disk Scheduler")
        self.root.geometry("500x400")

        # Labels and Inputs
        tk.Label(root, text="Enter Disk Requests (comma-separated):").pack(pady=5)
        self.entry_requests = tk.Entry(root, width=50)
        self.entry_requests.pack(pady=5)

        tk.Label(root, text="Enter Head Start Position:").pack(pady=5)
        self.entry_head = tk.Entry(root, width=10)
        self.entry_head.pack(pady=5)

        # Algorithm Selection
        tk.Label(root, text="Select Algorithm:").pack(pady=5)
        self.algo_var = tk.StringVar(value="FCFS")
        tk.OptionMenu(root, self.algo_var, "FCFS", "SSTF", "AI-Based").pack(pady=5)

        # Buttons
        tk.Button(root, text="Run Scheduler", command=self.run_scheduler).pack(pady=10)

    def run_scheduler(self):
        try:
            requests = list(map(int, self.entry_requests.get().split(',')))
            head_start = int(self.entry_head.get())
            algo = self.algo_var.get()

            if algo == "FCFS":
                sequence, seek_time = fcfs(requests, head_start)
            elif algo == "SSTF":
                sequence, seek_time = sstf(requests, head_start)
            elif algo == "AI-Based":
                ai_scheduler = AIScheduler()
                sequence = ai_scheduler.predict(requests)
                seek_time = sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))

            # Display results
            messagebox.showinfo("Results", f"Execution Order: {sequence}\nTotal Seek Time: {seek_time}")

            # Plot results
            plt.figure(figsize=(6,4))
            plt.plot([head_start] + sequence, marker='o', linestyle='-')
            plt.title(f"{algo} Disk Scheduling")
            plt.xlabel("Requests")
            plt.ylabel("Seek Position")
            plt.grid()
            plt.show()

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiskSchedulerApp(root)
    root.mainloop()
