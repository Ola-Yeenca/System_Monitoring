# System Monitoring


System Monitoring is a Python script that allows you to monitor your system's resource usage in real-time. The script displays CPU usage, memory usage, disk usage, and network usage. It provides a Tkinter-based GUI interface for easy monitoring, real-time feedback, and notifications.

## Features

- Real-time monitoring of CPU usage, memory usage, disk usage, and network usage.
- GUI interface for easy interaction and monitoring.
- Start and stop monitoring with the click of a button.
- System notifications for high resource usage.

## Installation

1. Clone the repository to your local machine: [ git clone https://github.com/Ola-Yeenca/System_Monitoring.git]
   ```bash
   ```

2. Navigate to the project directory:
   ```bash
   cd System_Monitoring
   ```

3. Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Python script `main.py` to launch the System Monitoring GUI:
   ```bash
   python3 main.py #its important to use python3 for this project
   ```

2. A pop-up window will appear displaying the current system resource usage.

3. Click the "Run Monitoring" button to start monitoring the system. The GUI will update with real-time resource usage.

4. Click the "Stop Monitoring" button to stop the monitoring process.

## GUI Interface

The Tkinter-based GUI provides a user-friendly interface for monitoring your system's resource usage. The GUI displays the following information:

- CPU Usage: The percentage of CPU utilization.
- Memory Usage: The percentage of memory (RAM) utilization.
- Disk Usage: The percentage of disk space utilization.
- Network Usage: The network usage in Mbps.

## System Notifications

If any of the monitored resources exceed their specified thresholds, a system notification will be triggered to alert the user. The notification will provide details of the high resource usage and help identify potential performance issues.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvement, feel free to submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

--------
