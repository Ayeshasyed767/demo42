import os
import platform
import subprocess

def print_system_uptime():
    system = platform.system()
    uptime = ""
    try:
        if system == "Linux" or system == "Darwin":
            # For Unix-like systems
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
            uptime = f"System uptime: {uptime_seconds // 3600:.0f} hours {(uptime_seconds % 3600) // 60:.0f} minutes"
        elif system == "Windows":
            # For Windows
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    uptime = f"System uptime since: {line.split('since', 1)[1].strip()}"
                    break
            else:
                uptime = "Could not determine uptime."
        else:
            uptime = "Unsupported OS for uptime check."
    except Exception as e:
        uptime = f"Error fetching uptime: {e}"
    print(uptime)

if __name__ == "__main__":
    print_system_uptime()
