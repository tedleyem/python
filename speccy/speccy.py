import platform
import psutil
import datetime

# convert bytes to human-readable 
def get_size(bytes_val, suffix="B"):
    factor = 1024
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi"]:
        if bytes_val < factor:
            return f"{bytes_val:.2f}{unit}{suffix}"
        bytes_val /= factor
    return f"{bytes_val:.2f}P{suffix}"

def show_specs():
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    # System
    print("---------------------------------------")
    print(" 🖥️        System Information         ")
    print("---------------------------------------")
    print(f"OS: {uname.system} {uname.release}")
    print(f"Kernel: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Node: {uname.node}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Boot Time: {bt.strftime('%Y-%m-%d %H:%M:%S')}")
    #print("\n")

    # CPU
    cpu_freq = psutil.cpu_freq()
    print("---------------------------------------")
    print(" 🧠           CPU Information          ")
    print("---------------------------------------")
    print(f"Processor: {platform.processor()}")
    print(f"Cores (Physical): {psutil.cpu_count(logical=False)} ")
    print(f"Threads (Logical): {psutil.cpu_count(logical=True)}")
    print(f"Max Freq: {cpu_freq.max:.2f}Mhz")
    print(f"Current Freq: {cpu_freq.current:.2f}Mhz")
    print(f"Total Usage: {psutil.cpu_percent(interval=1)}%")
    #print("\n")

    # RAM/MEMORY 
    mem = psutil.virtual_memory()
    print("---------------------------------------")
    print(" 💾         Memory (RAM) Info         ")
    print("---------------------------------------")
    print(f"Total: {get_size(mem.total)}")
    print(f"Available: {get_size(mem.available)}")
    print(f"Used: {get_size(mem.used)}")
    print(f"Usage: {mem.percent}%")
    #print("\n")

    # STORAGE
    print("---------------------------------------")
    print(" 💿          Storage Devices          ")
    print("---------------------------------------")
    partitions = psutil.disk_partitions()
    for i, part in enumerate(partitions):
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"Device {i+1}: {part.device}")
            print(f"  Mountpoint: {part.mountpoint}")
            print(f"  FS Type: {part.fstype}")
            print(f"  Size: {get_size(usage.total)} (Used: {get_size(usage.used)} / Free: {get_size(usage.free)})")
            print(f"  Usage: {usage.percent}%")
            print("-" * 39)
        except PermissionError:
            # Skip devices that are not accessible.
            continue
    #print("\n")

if __name__ == "__main__":
    show_specs()