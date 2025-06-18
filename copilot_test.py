import platform
import subprocess

def get_unix_uptime():
    """
    Returns the system uptime for Unix-like systems in a human-readable format.
    """
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"System uptime: {hours} hours {minutes} minutes"
    except Exception as e:
        return f"Error fetching Unix uptime: {e}"

def get_windows_uptime():
    """
    Returns the system uptime for Windows systems in a human-readable format.
    """
    try:
        result = subprocess.run(
            ["net", "stats", "srv"],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.splitlines():
            if "Statistics since" in line:
                return f"System uptime since: {line.split('since', 1)[1].strip()}"
        return "Could not determine uptime."
    except Exception as e:
        return f"Error fetching Windows uptime: {e}"

def print_system_uptime():
    """
    Detects the OS and prints the system uptime using the appropriate method.
    """
    system = platform.system()
    if system in ("Linux", "Darwin"):
        print(get_unix_uptime())
    elif system == "Windows":
        print(get_windows_uptime())
    else:
        print("Unsupported OS for uptime check.")

if __name__ == "__main__":
    print_system_uptime()
