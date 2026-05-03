import psutil
import tim
from datetime import datetime
import json
from collections import deque
import platform

class NetworkMonitor:
    def __init__(self, max_history=60):
        """Initialize network monitor with history buffer"""
        self.max_history = max_history
        self.network_history = deque(maxlen=max_history)
        self.cpu_history = deque(maxlen=max_history)
        self.memory_history = deque(maxlen=max_history)
        
    def get_network_stats(self):
        """Get current network statistics"""
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv,
            'errin': net_io.errin,
            'errout': net_io.errout,
            'dropin': net_io.dropin,
            'dropout': net_io.dropout
        }
    
    def get_system_stats(self):
        """Get system CPU and memory statistics"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        return {
            'cpu_percent': cpu_percent,
            'memory_percent': memory.percent,
            'memory_used_gb': memory.used / (1024**3),
            'memory_total_gb': memory.total / (1024**3),
            'memory_available_gb': memory.available / (1024**3)
        }
    
    def get_active_connections(self):
        """Get active network connections"""
        connections = psutil.net_connections()
        active_connections = []
        
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                active_connections.append({
                    'local_addr': conn.laddr.ip if conn.laddr else 'N/A',
                    'local_port': conn.laddr.port if conn.laddr else 'N/A',
                    'remote_addr': conn.raddr.ip if conn.raddr else 'N/A',
                    'remote_port': conn.raddr.port if conn.raddr else 'N/A',
                    'status': conn.status
                })
        
        return active_connections[:10]  # Return top 10 connections
    
    def get_interface_stats(self):
        """Get statistics for each network interface"""
        interfaces = psutil.net_if_stats()
        interface_data = []
        
        for iface_name, iface_stat in interfaces.items():
            interface_data.append({
                'name': iface_name,
                'is_up': iface_stat.isup,
                'mtu': iface_stat.mtu,
                'speed': iface_stat.speed,
                'duplex': iface_stat.duplex
            })
        
        return interface_data
    
    def get_running_processes(self):
        """Get top processes by network usage"""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'num_threads']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'threads': proc.info['num_threads']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        return sorted(processes, key=lambda x: x['threads'], reverse=True)[:10]
    
    def collect_metrics(self):
        """Collect all metrics and store in history"""
        timestamp = datetime.now().isoformat()
        
        network_stats = self.get_network_stats()
        system_stats = self.get_system_stats()
        
        metric = {
            'timestamp': timestamp,
            'network': network_stats,
            'system': system_stats
        }
        
        self.network_history.append(metric)
        
        return metric
    
    def get_dashboard_data(self):
        """Compile all data for dashboard display"""
        current_metric = self.collect_metrics()
        
        dashboard_data = {
            'timestamp': current_metric['timestamp'],
            'system': {
                'cpu_percent': current_metric['system']['cpu_percent'],
                'memory_percent': current_metric['system']['memory_percent'],
                'memory_used_gb': round(current_metric['system']['memory_used_gb'], 2),
                'memory_total_gb': round(current_metric['system']['memory_total_gb'], 2)
            },
            'network': {
                'bytes_sent': current_metric['network']['bytes_sent'],
                'bytes_recv': current_metric['network']['bytes_recv'],
                'packets_sent': current_metric['network']['packets_sent'],
                'packets_recv': current_metric['network']['packets_recv']
            },
            'active_connections': self.get_active_connections(),
            'interfaces': self.get_interface_stats(),
            'top_processes': self.get_running_processes(),
            'history': list(self.network_history)
        }
        
        return dashboard_data
    
    def print_dashboard(self):
        """Print formatted dashboard"""
        data = self.get_dashboard_data()
        
        print("\n" + "="*80)
        print("NETWORK MONITORING DASHBOARD".center(80))
        print("="*80)
        print(f"Timestamp: {data['timestamp']}\n")
        
        # System Stats
        print("SYSTEM STATISTICS".ljust(40) + "│")
        print("-" * 80)
        print(f"CPU Usage: {data['system']['cpu_percent']}%")
        print(f"Memory Usage: {data['system']['memory_percent']}%")
        print(f"Memory: {data['system']['memory_used_gb']}GB / {data['system']['memory_total_gb']}GB\n")
        
        # Network Stats
        print("NETWORK STATISTICS".ljust(40) + "│")
        print("-" * 80)
        print(f"Bytes Sent: {data['network']['bytes_sent'] / (1024**3):.2f} GB")
        print(f"Bytes Received: {data['network']['bytes_recv'] / (1024**3):.2f} GB")
        print(f"Packets Sent: {data['network']['packets_sent']}")
        print(f"Packets Received: {data['network']['packets_recv']}\n")
        
        # Network Interfaces
        print("NETWORK INTERFACES".ljust(40) + "│")
        print("-" * 80)
        for iface in data['interfaces'][:5]:
            status = "UP" if iface['is_up'] else "DOWN"
            print(f"{iface['name']}: {status}")
        
        # Active Connections
        print("\nACTIVE CONNECTIONS (Top 5)".ljust(40) + "│")
        print("-" * 80)
        for conn in data['active_connections'][:5]:
            print(f"{conn['local_addr']}:{conn['local_port']} → {conn['remote_addr']}:{conn['remote_port']}")
        
        print("\n" + "="*80 + "\n")


def main():
    """Main function to run the monitoring dashboard"""
    monitor = NetworkMonitor()
    
    print("Starting Network Monitoring Dashboard...")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            monitor.print_dashboard()
            time.sleep(5)  # Update every 5 seconds
    
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped. Goodbye!")


if __name__ == "__main__":
    main()
