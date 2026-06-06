import os
import time
import platform
import psutil
from datetime import datetime

class SystemPulse:
    def __init__(self):
        self.system_os = platform.system()
        self.release = platform.release()
        self.architecture = platform.machine()

    def gather_telemetry(self):
        """Fetches advanced live system hardware analytics."""
        cores_utilized = psutil.cpu_percent(interval=1, percpu=True)
        avg_cpu_load = sum(cores_utilized) / len(cores_utilized)
        memory = psutil.virtual_memory()
        disk = os.path.disk_usage('/')
        
        metrics = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "os_environment": f"{self.system_os} {self.release} ({self.architecture})",
            "cpu_metrics": {
                "overall_utilization_pct": round(avg_cpu_load, 2),
                "core_breakdown_pct": cores_utilized,
                "frequency_mhz": round(psutil.cpu_freq().current, 2) if psutil.cpu_freq() else "N/A"
            },
            "memory_metrics": {
                "total_gb": round(memory.total / (1024**3), 2),
                "used_gb": round(memory.used / (1024**3), 2),
                "available_gb": round(memory.available / (1024**3), 2),
                "utilization_pct": memory.percent
            },
            "storage_metrics": {
                "total_capacity_gb": round(disk.total / (1024**3), 2),
                "used_space_gb": round(disk.used / (1024**3), 2),
                "free_space_gb": round(disk.free / (1024**3), 2),
                "utilization_pct": round((disk.used / disk.total) * 100, 2)
            }
        }
        return metrics

    def display_dashboard(self, data):
        """Renders an enterprise-grade terminal monitoring interface."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f" SYSTEM PULSE ANALYTICS ENGINE — LIVE TELEMETRY ")
        print("=" * 60)
        print(f" [TIMESTAMP]   {data['timestamp']}")
        print(f" [ENVIRONMENT] {data['os_environment']}")
        print("-" * 60)
        print(f" 🟢 CPU UTILIZATION:   {data['cpu_metrics']['overall_utilization_pct']}% [@ {data['cpu_metrics']['frequency_mhz']} MHz]")
        print(f"    Core Array Distribution: {data['cpu_metrics']['core_breakdown_pct']}\n")
        print(f" 🔵 MEMORY METRICS:    {data['memory_metrics']['utilization_pct']}% Utilized")
        print(f"    Allocation Maps:     {data['memory_metrics']['used_gb']}GB Used / {data['memory_metrics']['total_gb']}GB Total\n")
        print(f" 🟡 STORAGE TOPOLOGY:  {data['storage_metrics']['utilization_pct']}% Capacity Reached")
        print(f"    Volume Index:        {data['storage_metrics']['used_space_gb']}GB Allocated / {data['storage_metrics']['total_capacity_gb']}GB Free")
        print("=" * 60)
        print(" [STATUS] Pipeline running optimally. Press Ctrl+C to terminate.")

if __name__ == "__main__":
    pulse = SystemPulse()
    try:
        # Run a brief test cycle for execution logging
        telemetry_data = pulse.gather_telemetry()
        pulse.display_dashboard(telemetry_data)
    except KeyboardInterrupt:
        print("\n[INFO] Data logging stream cleanly closed by operator.")
