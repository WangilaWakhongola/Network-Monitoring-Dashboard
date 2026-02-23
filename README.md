Network Monitoring Dashboard
A real-time, enterprise-grade network monitoring system that tracks system performance, network statistics, and active connections with a 60-second historical data buffer.

https://img.shields.io/badge/python-3.7%252B-blue
https://img.shields.io/badge/platform-windows%2520%257C%2520macos%2520%257C%2520linux-lightgrey
https://img.shields.io/badge/license-MIT-green

📋 Overview
This powerful monitoring tool provides comprehensive visibility into your system's network activity and resource utilization. Designed for both system administrators and security professionals, it delivers real-time insights with minimal overhead.

✨ Key Features
Network Monitoring
Traffic Analysis: Track bytes sent/received in real-time

Packet Statistics: Monitor packet counts and error rates

Interface Management: View all network interfaces with status, MTU, and speed

System Performance
CPU Monitoring: Real-time usage percentage tracking

Memory Analytics: Usage, availability, and utilization rates

Process Management: Top processes by thread count and resource consumption

Connection Tracking
Active Connections: Real-time display of established connections

Address Resolution: Local and remote endpoint tracking

Connection States: Monitor connection status and transitions

Data Persistence
Historical Buffer: Maintains 60 seconds of time-series data

Trend Analysis: Track metrics over time for pattern identification

Rolling Updates: Continuous data collection with efficient memory usage

🚀 Quick Start
Prerequisites
Python 3.7 or higher

pip package manager

One-Minute Setup
bash
# Clone the repository
git clone https://github.com/WangilaWakhongola/network-monitoring-dashboard.git
cd network-monitoring-dashboard

# Install the only dependency
pip install psutil

# Launch the dashboard
python network_monitor.py
Press Ctrl+C to stop the monitoring session.

📦 Installation Options
Standard Installation
bash
# Create and activate virtual environment (recommended)
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
Docker Support (Coming Soon)
bash
# Future enhancement: Docker deployment
# docker build -t network-monitor .
# docker run network-monitor
🏗️ Architecture
Project Structure
text
network-monitoring-dashboard/
├── network_monitor.py      # Core monitoring application
├── requirements.txt        # Dependency manifest
├── README.md              # Documentation
└── .gitignore            # Version control exclusions
Core Components
The NetworkMonitor class encapsulates all monitoring functionality:

Method	Description
get_network_stats()	Retrieves current network I/O statistics
get_system_stats()	Captures CPU and memory utilization
get_active_connections()	Lists established network connections
get_interface_stats()	Enumerates network interfaces and status
get_running_processes()	Identifies top processes by thread count
collect_metrics()	Aggregates all metrics with timestamp
get_dashboard_data()	Compiles complete dashboard dataset
print_dashboard()	Renders formatted console output
Data Flow
Metrics collection every 5 seconds

Historical buffer maintains 60 data points (5 minutes)

Real-time dashboard updates with each collection cycle

Thread-safe data structures ensure consistency

💻 Usage Examples
Basic Monitoring
python
from network_monitor import NetworkMonitor

monitor = NetworkMonitor()
dashboard_data = monitor.get_dashboard_data()
monitor.print_dashboard()
Programmatic Access
python
# Access individual metrics
stats = monitor.collect_metrics()
print(f"CPU: {stats['system']['cpu_percent']}%")
print(f"Bytes Sent: {stats['network']['bytes_sent']}")
Sample Output
text
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
Packets Sent: 1,250,000
Packets Received: 3,500,000

NETWORK INTERFACES
eth0: UP (MTU: 1500, Speed: 1000Mb/s)
wlan0: UP (MTU: 1500, Speed: 433Mb/s)
lo: UP (MTU: 65536)

ACTIVE CONNECTIONS (Top 5)
192.168.1.100:54321 → 8.8.8.8:443 (ESTABLISHED)
192.168.1.100:54322 → 142.250.185.46:443 (ESTABLISHED)
192.168.1.100:54323 → 1.1.1.1:53 (ESTABLISHED)

TOP PROCESSES (By Thread Count)
1. chrome.exe (45 threads)
2. python.exe (12 threads)
3. explorer.exe (25 threads)

================================================================================
🔧 Advanced Configuration
Custom Update Intervals
Modify the collection frequency in network_monitor.py:

python
# Change from default 5 seconds
UPDATE_INTERVAL = 10  # Update every 10 seconds
Historical Buffer Size
Adjust the number of retained data points:

python
# Change from default 60 points
MAX_HISTORY = 120  # Keep 10 minutes of data (120 * 5 seconds)
🛠️ Use Cases
Network Administration
Bandwidth Monitoring: Track usage patterns and identify bottlenecks

Interface Health: Monitor link status and error rates

Capacity Planning: Analyze trends for infrastructure scaling

Security Operations
Threat Detection: Identify unusual connection patterns

Incident Response: Real-time visibility during security events

Forensic Analysis: Historical data for post-incident investigation

Development & Testing
Application Profiling: Monitor network behavior of applications

Performance Testing: Validate network efficiency under load

Debugging: Identify connection issues during development

⚠️ Troubleshooting
Common Issues
Problem	Solution
Permission denied errors	Run with elevated privileges: sudo python network_monitor.py (Linux/macOS)
Missing psutil module	Install dependency: pip install psutil
No connections showing	Check firewall settings; run as administrator/root
Inaccurate statistics	Verify network interface selection; check for virtualization overhead
System Requirements
Minimum: 512MB RAM, 100MB disk space

Recommended: 2GB RAM, 500MB disk space

Network: Read access to network interfaces

🔮 Roadmap
Version 1.1 (Q2 2025)
Web-based dashboard using Flask

Real-time visualization with Chart.js

CSV/JSON data export

Configurable alert thresholds

Version 2.0 (Q4 2025)
Multi-system distributed monitoring

Machine learning-based anomaly detection

PostgreSQL database integration

REST API for data access

Mobile-responsive web interface

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Please ensure your code follows PEP 8 standards and includes appropriate tests.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Emmanuel Wakhongola

GitHub: @WangilaWakhongola

Email: wangilawakhongola@gmail.com

LinkedIn: Emmanuel Wakhongola

🙏 Acknowledgments
psutil - Cross-platform system monitoring library

Python Software Foundation - For the amazing language and ecosystem

Open source community - For continuous inspiration and support

Version: 1.0.0 | Last Updated: January 2025 | Status: Active Development
