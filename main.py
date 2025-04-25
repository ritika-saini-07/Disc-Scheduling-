import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from traditional_algorithms.fcfs import fcfs
from traditional_algorithms.sstf import sstf
from traditional_algorithms.look import look
from traditional_algorithms.scan import scan
from traditional_algorithms.cscan import c_scan

class DiskSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Based Disk Scheduler")
        self.root.geometry("520x500")

        tk.Label(root, text="Enter Disk Requests (comma-separated):").pack(pady=5)
        self.entry_requests = tk.Entry(root, width=50)
        self.entry_requests.pack(pady=5)

        tk.Label(root, text="Enter Head Start Position:").pack(pady=5)
        self.entry_head = tk.Entry(root, width=10)
        self.entry_head.pack(pady=5)

        tk.Label(root, text="Enter Disk Size:").pack(pady=5)
        self.entry_disk_size = tk.Entry(root, width=10)
        self.entry_disk_size.insert(0, "200")  # default disk size
        self.entry_disk_size.pack(pady=5)

        tk.Label(root, text="Direction (left/right):").pack(pady=5)
        self.entry_direction = tk.Entry(root, width=10)
        self.entry_direction.insert(0, "right")
        self.entry_direction.pack(pady=5)

        tk.Label(root, text="Select Algorithm:").pack(pady=5)
        self.algo_var = tk.StringVar(value="FCFS")
        tk.OptionMenu(root, self.algo_var, "FCFS", "SSTF", "LOOK", "SCAN", "CSCAN").pack(pady=5)

        tk.Button(root, text="Run Scheduler", command=self.run_scheduler).pack(pady=10)

    def run_scheduler(self):
        try:
            requests = list(map(int, self.entry_requests.get().split(',')))
            head_start = int(self.entry_head.get())
            disk_size = int(self.entry_disk_size.get())
            direction = self.entry_direction.get().lower()

            algo = self.algo_var.get()

            if algo == "FCFS":
                sequence, seek_time = fcfs(requests, head_start)
            elif algo == "SSTF":
                sequence, seek_time = sstf(requests, head_start)
            elif algo == "LOOK":
                sequence, seek_time = look(requests, head_start, direction)
            elif algo == "SCAN":
                sequence, seek_time = scan(requests, head_start, disk_size, direction)
            elif algo == "CSCAN":
                sequence, seek_time = c_scan(requests, head_start, disk_size)

            messagebox.showinfo("Results", f"Execution Order: {sequence}\nTotal Seek Time: {seek_time}")

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

