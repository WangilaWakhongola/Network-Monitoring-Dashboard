\# Network Monitoring Dashboard



A real-time enterprise-grade network monitoring system that tracks system performance, network statistics, and active connections.



\## Features



✅ \*\*Real-Time Network Monitoring\*\*

\- Track bytes sent/received

\- Monitor packet statistics

\- Detect network errors



✅ \*\*System Performance Tracking\*\*

\- CPU usage percentage

\- Memory usage and availability

\- System resource monitoring



✅ \*\*Active Connections Display\*\*

\- Real-time connection status

\- Local and remote address tracking

\- Connection state monitoring



✅ \*\*Network Interface Management\*\*

\- Monitor all network interfaces

\- Track interface status (UP/DOWN)

\- Display MTU and speed information



✅ \*\*Process Monitoring\*\*

\- Track top running processes

\- Thread count monitoring

\- Resource usage analysis



✅ \*\*Historical Data\*\*

\- Maintains 60-second history buffer

\- Time-series data collection

\- Trend analysis capabilities



\## Requirements



\- Python 3.7+

\- psutil library



\## Installation



1\. \*\*Clone the repository\*\*

```bash

git clone https://github.com/WangilaWakhongola/network-monitoring-dashboard.git

cd network-monitoring-dashboard

```



2\. \*\*Create a virtual environment (optional but recommended)\*\*

```bash

python -m venv venv



\# On Windows:

venv\\Scripts\\activate



\# On macOS/Linux:

source venv/bin/activate

```



3\. \*\*Install dependencies\*\*

```bash

pip install -r requirements.txt

```



\## Usage



\*\*Run the monitoring dashboard:\*\*

```bash

python network\_monitor.py

```



The dashboard will display:

\- Current system statistics (CPU, Memory)

\- Network statistics (bytes sent/received, packets)

\- Active network interfaces

\- Top 5 active connections

\- Top 10 running processes



Updates occur every 5 seconds. Press `Ctrl+C` to stop.



\## Project Structure



```

network-monitoring-dashboard/

├── network\_monitor.py      # Main monitoring application

├── requirements.txt        # Python dependencies

├── README.md              # This file

└── .gitignore            # Git ignore file

```



\## How It Works



\### NetworkMonitor Class



The `NetworkMonitor` class provides methods to:



\- \*\*get\_network\_stats()\*\* - Returns current network I/O statistics

\- \*\*get\_system\_stats()\*\* - Returns CPU and memory usage

\- \*\*get\_active\_connections()\*\* - Lists established network connections

\- \*\*get\_interface\_stats()\*\* - Retrieves network interface information

\- \*\*get\_running\_processes()\*\* - Gets top processes by thread count

\- \*\*collect\_metrics()\*\* - Gathers all metrics with timestamp

\- \*\*get\_dashboard\_data()\*\* - Compiles complete dashboard data

\- \*\*print\_dashboard()\*\* - Displays formatted dashboard output



\### Data Collection



The system collects metrics every 5 seconds and maintains a rolling history of the last 60 data points (5 minutes of data).



\## Example Output



```

================================================================================

NETWORK MONITORING DASHBOARD

================================================================================

Timestamp: 2025-01-15T10:30:45.123456



SYSTEM STATISTICS

CPU Usage: 25.5%

Memory Usage: 45.2%

Memory: 7.2GB / 16GB



NETWORK STATISTICS

Bytes Sent: 15.3 GB

Bytes Received: 42.1 GB

Packets Sent: 1250000

Packets Received: 3500000



NETWORK INTERFACES

eth0: UP

wlan0: UP

lo: UP



ACTIVE CONNECTIONS (Top 5)

192.168.1.100:54321 → 8.8.8.8:443

192.168.1.100:54322 → 142.250.185.46:443

192.168.1.100:54323 → 1.1.1.1:53



================================================================================

```



\## Use Cases



\- \*\*Enterprise Network Administration\*\* - Monitor network health across systems

\- \*\*Cybersecurity\*\* - Detect unusual network activity and connections

\- \*\*System Troubleshooting\*\* - Diagnose performance issues

\- \*\*Network Analysis\*\* - Analyze bandwidth usage and patterns

\- \*\*Infrastructure Monitoring\*\* - Track system resources in real-time



\## Future Enhancements



\- \[ ] Web-based dashboard with Flask/Django

\- \[ ] Real-time graphs and visualizations

\- \[ ] Alert system for anomalies

\- \[ ] Historical data export (CSV/JSON)

\- \[ ] Network traffic analysis

\- \[ ] Threat detection algorithms

\- \[ ] Multi-system monitoring

\- \[ ] Database integration for long-term storage



\## Technologies Used



\- \*\*Python 3\*\* - Core programming language

\- \*\*psutil\*\* - System and network monitoring library

\- \*\*Collections\*\* - Efficient data structure handling



\## Performance



\- Lightweight and efficient monitoring

\- Minimal CPU overhead

\- Works on Windows, macOS, and Linux

\- Real-time updates with 5-second intervals



\## Troubleshooting



\*\*"Permission denied" errors:\*\*

\- On Linux/macOS, you may need root privileges for some network stats

\- Run with `sudo python network\_monitor.py`



\*\*Missing psutil module:\*\*

```bash

pip install psutil

```



\*\*No active connections showing:\*\*

\- Some systems may restrict access to connection data

\- Try running with elevated privileges



\## Contributing



Feel free to fork and submit pull requests for improvements!



\## License



This project is open source and available for educational and commercial use.



\## Author



Emmanuel Wakhongola

\- GitHub: \[@WangilaWakhongola](https://github.com/WangilaWakhongola)

\- Email: wangilawakhongola@gmail.com



\## Contact



For questions or issues, please open an issue on GitHub or contact me directly.



---



\*\*Last Updated:\*\* January 2025

\*\*Version:\*\* 1.0.0

