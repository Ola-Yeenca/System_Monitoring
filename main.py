import psutil
import time
from plyer import notification
import logging
import tkinter as tk
from tkinter import messagebox
import threading

# Logging configuration
LOG_FILE = "system_monitoring.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Global variable to indicate if the monitoring is running or stopped
monitoring_running = False

def monitor_system(interval=60, cpu_threshold=80, memory_threshold=80, disk_threshold=80):
    """Monitors the system for problems."""
    global monitoring_running

    while monitoring_running:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent

        # Calculate network usage percentage
        net_io = psutil.net_io_counters()
        total_bytes_sent = net_io.bytes_sent
        total_bytes_recv = net_io.bytes_recv
        time.sleep(interval)
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent - total_bytes_sent
        bytes_recv = net_io.bytes_recv - total_bytes_recv
        network_usage = 100.0 * (bytes_sent + bytes_recv) / (interval * 1_000_000)  # Convert to Mbps

        # Log the metrics
        logging.info(f"CPU usage: {cpu_usage}% | Memory usage: {memory_usage}% | "
                     f"Disk usage: {disk_usage}% | Network usage: {network_usage:.2f}% Mbps")

        # If any metric exceeds the threshold, send a system notification
        if cpu_usage > cpu_threshold or memory_usage > memory_threshold or disk_usage > disk_threshold:
            message = f"CPU usage: {cpu_usage}% | Memory usage: {memory_usage}% | " \
                      f"Disk usage: {disk_usage}% | Network usage: {network_usage:.2f}% Mbps"
            send_system_notification(message)

        # Update the GUI with the system metrics using the thread-safe method
        root.after(0, update_gui, cpu_usage, memory_usage, disk_usage, network_usage)

def send_system_notification(message):
    notification_title = "System Monitoring Alert"
    notification_text = message

    try:
        notification.notify(title=notification_title, message=notification_text)
        logging.info("System notification sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send system notification. Error: {e}")

def start_monitoring():
    global monitoring_running
    if not monitoring_running:
        monitoring_running = True
        monitor_thread = threading.Thread(target=monitor_system)
        monitor_thread.start()
        run_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

def stop_monitoring():
    global monitoring_running
    if monitoring_running:
        monitoring_running = False
        run_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

def update_gui(cpu_usage, memory_usage, disk_usage, network_usage):
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    memory_label.config(text=f"Memory Usage: {memory_usage}%")
    disk_label.config(text=f"Disk Usage: {disk_usage}%")
    network_label.config(text=f"Network Usage: {network_usage:.2f}% Mbps")

if __name__ == "__main__":
    # Create the Tkinter root window
    root = tk.Tk()
    root.title("System Monitoring")

    # Create labels to display the system metrics
    cpu_label = tk.Label(root, text="CPU Usage: -")
    cpu_label.pack()
    memory_label = tk.Label(root, text="Memory Usage: -")
    memory_label.pack()
    disk_label = tk.Label(root, text="Disk Usage: -")
    disk_label.pack()
    network_label = tk.Label(root, text="Network Usage: -")
    network_label.pack()

    # Create "Run" button
    run_button = tk.Button(root, text="Run Monitoring", command=start_monitoring)
    run_button.pack()

    # Create "Stop" button
    stop_button = tk.Button(root, text="Stop Monitoring", command=stop_monitoring, state=tk.DISABLED)
    stop_button.pack()

    # Create a function to handle closing the window
    def on_close():
        if messagebox.askokcancel("Quit", "Do you want to stop monitoring and quit?"):
            stop_monitoring()
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Run the Tkinter event loop
    root.mainloop()
